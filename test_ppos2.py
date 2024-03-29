import pytest
username = "art"

def test_user_exists(host):
    user = host.user("%s" % username)
    assert user.name == "%s" % username
    assert user.group == "%s" % username
    assert user.home == "/home/%s" % username

def test_user_home_exists(host):
    user_home = host.file("/home/%s" % username)
    assert user_home.exists
    assert user_home.is_directory

def test_ufw(Command):
    command = Command('sudo ufw status | grep -w "Status: active"')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '5a628dd52d5eb8c0e741200eb495c648  /etc/ufw/user.rules'
    assert command.rc == 0

def test_dbdump_backup_output1(Command):
    command = Command('sudo tail -2 /home/art/db_dump.log |grep -c OK$')
    assert command.stdout.rstrip() == '2'
    assert command.rc == 0

def test_dbdump_backup_output2(Command):
    command = Command('sudo tail -2 /home/art/db_dump.log |grep -c $(date +%m%d).sql.gz:\ OK$')
    assert command.stdout.rstrip() == '1'
    assert command.rc == 0

def test_ulimit_unchanged(Command):
    command = Command('ulimit -n')
    assert command.stdout.rstrip() == '200000'
    assert command.rc == 0

def test_crond_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.filter(ppid=nginxmaster.pid)
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening

def test_pproxy_docker_compose_deploy_unchanged(Command):
    command = Command('sudo md5sum /home/pproxy/pp-releaseprd/docker-compose-deploy.yml')
    assert command.stdout.rstrip() == 'd4a61109f2273be9691e9c464e71be65  /home/pproxy/pp-releaseprd/docker-compose-deploy.yml'
    assert command.rc == 0

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_docker_compose_config(host):
    conf = host.file("/home/pproxy/pp-releaseprd/docker-compose-deploy.yml")
    assert conf.user == "pproxy"
    assert conf.group == "pproxy"
    assert conf.contains("version: \"3.7\"")
    assert conf.contains("services:")
    assert conf.contains("  payworld-proxy:")
    assert conf.contains("    restart: unless-stopped")
    assert conf.contains("    image: ${PROXY_BACKEND_IMAGE}")
    assert conf.contains("    container_name: payworld-proxy")
    assert conf.contains("    ports:")
    assert conf.contains("      - 0.0.0.0:8081:8080")
    assert conf.contains("      - 0.0.0.0:5005:5005")
    assert conf.contains("    env_file:")
    assert conf.contains("      - compose-setup.env")
    assert conf.contains("    environment:")
    assert conf.contains("      - PAYWORLDPROXY_SOAP_KEYSTOREFILE=file:/opt/keystore/payworld-proxy.p12")
    assert conf.contains("    volumes:")
    assert conf.contains("      - ${KEYSTORE_PATH}:/opt/keystore/payworld-proxy.p12")
    assert conf.contains("    networks:")
    assert conf.contains("      pnet:")
    assert conf.contains("  payworld-proxy-web:")
    assert conf.contains("    restart: unless-stopped")
    assert conf.contains("    image: ${PROXY_UI_IMAGE}")
    assert conf.contains("    container_name: payworld-proxy-web")
    assert conf.contains("    ports:")
    assert conf.contains("      - 0.0.0.0:9090:80")
    assert conf.contains("    environment:")
    assert conf.contains("      - NGINX_PORT=80")
    assert conf.contains("      - PP_RESTAPI_BASE=auto")
    assert conf.contains("      - PP_NGINX_BE_SCHEME=http")
    assert conf.contains("      - PP_NGINX_BE_FQDN=payworld-proxy:8080")
    assert conf.contains("    networks:")
    assert conf.contains("      pnet:")
    assert conf.contains("networks:")
    assert conf.contains("  pnet:")
    assert conf.contains("    driver: bridge")
    assert conf.contains("    ipam:")
    assert conf.contains("      driver: default")
    assert conf.contains("      config:")
    assert conf.contains("      - subnet:  10.103.0.1/16")

def test_bpost_website(Command):
    command = Command('curl -sSfk "https://bpost.novelpay.pl/pp/meta" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_ppos2_website(Command):
    command = Command('curl -sSfk "https://ppos2.novelpay.pl/pp/meta" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running
    postgres = Process.filter(comm="postgres")
    assert Socket("tcp://0.0.0.0:5432").is_listening

def test_pg_isready_output(Command):
    command = Command('/usr/bin/pg_isready')
    assert command.stdout.rstrip() == '/var/run/postgresql:5432 - accepting connections'
    assert command.rc == 0

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_mongod_running(Process, Service, Socket, Command):
    assert Service("mongod").is_enabled
    assert Service("mongod").is_running
    mongod = Process.get(comm="mongod")
    assert mongod.user == "mongodb"
    assert mongod.group == "mongodb"
    assert Socket("tcp://10.103.0.1:27017").is_listening

# netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:6080", # docker proxy
"tcp://0.0.0.0:9090", # pproxy docker
"tcp://0.0.0.0:10050", # zabbix agent
"tcp://0.0.0.0:6787", # docker proxy
"tcp://0.0.0.0:35621",
"tcp://0.0.0.0:35623",
"tcp://0.0.0.0:4200", # docker proxy
"tcp://10.103.0.1:27017", # mongodb
"tcp://0.0.0.0:6443", # docker proxy
"tcp://0.0.0.0:5005", # pproxy docker
"tcp://0.0.0.0:80", # nginx
"tcp://0.0.0.0:8081", # pproxy docker
"tcp://127.0.0.53:53",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432", # postgres
"tcp://0.0.0.0:443" # nginx
    ):  
        socket = host.socket(spec)
        assert socket.is_listening
