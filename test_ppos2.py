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
    assert command.stdout.rstrip() == '502f24eec3f58a46838c9eb5a271f3a1  /etc/ufw/user.rules'
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

def test_nginxconf_unchanged(Command):
    command = Command('sudo md5sum /etc/nginx/sites-enabled/ppos2')
    assert command.stdout.rstrip() == '5f6e287767d57ec1b82d1c4072448235  /etc/nginx/sites-enabled/ppos2'
    assert command.rc == 0

def test_pproxy_docker_compose_deploy_unchanged(Command):
    command = Command('sudo md5sum /home/pproxy/pp-releaseprd/docker-compose-deploy.yml')
    assert command.stdout.rstrip() == 'd4a61109f2273be9691e9c464e71be65  /home/pproxy/pp-releaseprd/docker-compose-deploy.yml'
    assert command.rc == 0

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_ppos2_nginx_conf(host):
    conf = host.file("/etc/nginx/sites-enabled/ppos2")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.contains("listen 443 ssl;")
    assert conf.contains("server_name ppos2.novelpay.pl;")
    assert conf.contains("server_name ppos2.novelpay.pl;")
    assert conf.contains("access_log   /var/log/nginx/lot_access.log;")
    assert conf.contains("server_name ppos2.novelpay.pl;")
    assert conf.contains("error_log    /var/log/nginx/lot_error.log error;")
    assert conf.contains("root /opt/ppos/web/html;")
    assert conf.contains("index index.html;")
    assert conf.contains("ssl_certificate_key /etc/nginx/ssl/novelpay.key;")
    assert conf.contains("ssl_certificate     /etc/nginx/ssl/novelpay.pem;")
    assert conf.contains("ssl_client_certificate /etc/nginx/ssl/ca.crt;")
    assert conf.contains("ssl_protocols TLSv1.1 TLSv1.2;")
    assert conf.contains("ssl_prefer_server_ciphers on;")
    assert conf.contains("ssl_ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS;")
    assert conf.contains("ssl_dhparam /etc/nginx/ssl/dhparam.pem;")
    assert conf.contains("ssl_verify_client optional;")
    assert conf.contains("add_header Strict-Transport-Security max-age=31536000;")
    assert conf.contains("ssl_certificate_key /etc/nginx/ssl/novelpay.key;")
    assert conf.contains("ssl_certificate     /etc/nginx/ssl/novelpay.pem;")
    assert conf.contains("ssl_client_certificate /etc/nginx/ssl/ca.crt;")
    assert conf.contains("ssl_protocols TLSv1.1 TLSv1.2;")
    assert conf.contains("ssl_prefer_server_ciphers on;")
    assert conf.contains("ssl_ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS;")
    assert conf.contains("ssl_dhparam /etc/nginx/ssl/dhparam.pem;")
    assert conf.contains("ssl_verify_client optional;")
    assert conf.contains("add_header Strict-Transport-Security max-age=31536000;")
    assert conf.contains("try_files $uri $uri/ /index.html =404;")
    assert conf.contains("add_header Cache-Control must-revalidate; # Indicate that the resource must be revalidated at each access")
    assert conf.contains("etag on;")
    assert conf.contains("location /pos-api {")
    assert conf.contains("proxy_set_header Host $host;")
    assert conf.contains("proxy_set_header X-Real-IP $remote_addr;")
    assert conf.contains("proxy_set_header X-Certificate-Verified $ssl_client_verify;")
    assert conf.contains("proxy_set_header X-Certificate-Dn $ssl_client_s_dn;")
    assert conf.contains(" proxy_pass http://127.0.0.1:8080/ppos/pos-api;")
    assert conf.contains("location /pos-api2 {")
    assert conf.contains("proxy_set_header Host $host;")
    assert conf.contains("proxy_set_header X-Real-IP $remote_addr;")
    assert conf.contains("proxy_pass http://127.0.0.1:8080/ppos/pos-api;")
    assert conf.contains("location /REST {")
    assert conf.contains("proxy_set_header Host $host;")
    assert conf.contains("proxy_set_header X-Real-IP $remote_addr;")
    assert conf.contains("proxy_pass http://127.0.0.1:8080/ppos/REST;")
    assert conf.contains("location /learning {")
    assert conf.contains("alias /opt/ppos/learning;")
    assert conf.contains("auth_basic \"Learning Area\";")
    assert conf.contains("auth_basic_user_file /opt/ppos/conf/loearning.pwd;")
    assert conf.contains("listen 80;")
    assert conf.contains("server_name testlot.novelpay.pl;")
    assert conf.contains("return 301 https://$host$request_uri;")


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

def test_wildfly_standalone_running(Process, Service, Socket, Command):
    standalone = Process.get(user="%s" %username, comm="standalone.sh")
    assert standalone.user == "%s" % username
    assert standalone.group == "%s" % username
    java = Process.get(user="%s" %username, comm="java", ppid=standalone.pid)
    assert java.user == "%s" % username
    assert java.group == "%s" % username
    assert Socket("tcp://0.0.0.0:8443").is_listening
    assert Socket("tcp://0.0.0.0:41616").is_listening
    assert Socket("tcp://127.0.0.1:9990").is_listening
    assert Socket("tcp://0.0.0.0:8080").is_listening

@pytest.mark.parametrize("package", [
    ("ppos-application-0.9.1-SNAPSHOT.war")
])

def test_is_package_deployed(host, package):
    pkg = host.run("sudo -u %s /opt/wildfly-15.0.0.Final/bin/jboss-cli.sh -c --controller=127.0.0.1 \"deployment-info --name=%s\" | grep %s | awk '{print $NF}'" % (username, package, package))
    assert pkg.stdout.rstrip() == 'OK'
    assert pkg.rc == 0

def test_count_java_process(host):
    javas = host.process.filter(user="%s" % username, comm="java", fname="java")
    assert len(javas) == 1

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
"tcp://0.0.0.0:41616",
"tcp://0.0.0.0:8080",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:8081", # pproxy docker
"tcp://127.0.0.53:53",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://0.0.0.0:8443",
"tcp://0.0.0.0:443",
"tcp://0.0.0.0:9090", # pproxy docker
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:35621",
"tcp://127.0.0.1:9990",
"tcp://0.0.0.0:35623",
"tcp://10.103.0.1:27017",
"tcp://0.0.0.0:5005" # pproxy docker
    ):  
        socket = host.socket(spec)
        assert socket.is_listening
