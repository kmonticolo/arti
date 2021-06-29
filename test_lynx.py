def test_ufw(Command):
    command = Command('sudo ufw status | grep -w "Status: active"')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'e0e092cdbb1dfbf2fe28233c87f98995  /etc/ufw/user.rules'
    assert command.rc == 0

def test_mongod_running(Process, Service, Socket, Command):
    assert Service("mongod").is_enabled
    assert Service("mongod").is_running

    mongod = Process.get(comm="mongod")
    assert mongod.user == "mongodb"
    assert mongod.group == "mongodb"

    assert Socket("tcp://127.0.0.1:27017").is_listening

def test_bind_running(Process, Service, Socket, Command):
    assert Service("bind9").is_enabled
    assert Service("bind9").is_running

    named = Process.get(comm="named")
    assert named.user == "bind"
    assert named.group == "bind"

    assert Socket("tcp://127.0.0.1:53").is_listening
    assert Socket("tcp://167.114.54.62:53").is_listening
    assert Socket("tcp://127.0.0.1:953").is_listening

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.filter(ppid=nginxmaster.pid)
    assert Socket("tcp://0.0.0.0:443").is_listening
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://:::443").is_listening
    assert Socket("tcp://:::80").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_apache2_running(Process, Service, Socket, Command):
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running
    assert Socket("tcp://:::80").is_listening

def test_apache_validate(Command):
    command = Command('sudo apache2ctl -t')
    assert command.rc == 0

def test_apache2_conf000default(host):
    conf = host.file("/etc/apache2/sites-enabled/000-default.conf")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.contains("DocumentRoot /opt/orthphoto.net/www/html")
    assert conf.contains("Options Indexes FollowSymLinks MultiViews")
    assert conf.contains("AllowOverride All")
    assert conf.contains("Require all granted")
    assert conf.contains("ErrorDocument 403 /opt/orthphoto.net/www/error/403.html")
    assert conf.contains("ErrorLog ${APACHE_LOG_DIR}/error.log")
    assert conf.contains("CustomLog ${APACHE_LOG_DIR}/access.log combined")
    assert conf.contains("ErrorDocument 403 /")

def test_orthphoto_website(Command):
    command = Command('curl -sSf "https://www.orthphoto.net" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_killall_certbot(Command):
    command = Command('sudo killall certbot 2>/dev/null')

def test_certbot_dry_run(Command):
    command = Command('sudo certbot --dry-run renew')
    assert command.rc == 0

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://127.0.0.1:5432").is_listening

def test_pg_isready_output(Command):
    command = Command('/usr/bin/pg_isready')
    assert command.stdout.rstrip() == '/var/run/postgresql:5432 - accepting connections'
    assert command.rc == 0

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running

    postgres = Process.filter(comm="zabbix_agentd")

    assert Socket("tcp://0.0.0.0:10050").is_listening


def test_postfix_running(Process, Service, Socket, Command):
    assert Service("postfix").is_enabled
    assert Service("postfix").is_running

    postfix = Process.get(comm="master")

    assert Socket("tcp://0.0.0.0:25").is_listening

def test_mysql_running(Process, Service, Socket, Command):
    assert Service("mysql").is_enabled
    assert Service("mysql").is_running

    mysql = Process.get(comm="mysqld_safe")
    assert mysql.user == "root"
    assert mysql.group == "root"

    assert Socket("tcp://0.0.0.0:3306").is_listening

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://167.114.54.62:53",
"tcp://127.0.0.1:53",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:5432",
"tcp://0.0.0.0:25",
"tcp://127.0.0.1:953",
"tcp://0.0.0.0:443",
"tcp://0.0.0.0:10050",
"tcp://127.0.0.1:27017",
"tcp://0.0.0.0:3306",
"tcp://0.0.0.0:80",
"tcp://:::22",
"tcp://:::25",
"tcp://:::443",
"tcp://0.0.0.0:10080",
"tcp://:::80"
    ):
        socket = host.socket(spec)
        assert socket.is_listening
