# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
#
#root:x:0:0:root:/root:/bin/bash
#adam:x:1000:1000:Adam Bartoszuk,,,:/home/adam:/bin/bash
#jboss:x:1001:1001:,,,:/home/jboss:/bin/bash
#postgres:x:106:114:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
#pjakubowski:x:1003:1003:Piotr Jakubowski,,,:/home/pjakubowski:/bin/bash
#tgalko:x:1004:1004:Tomasz Galko,,,:/home/tgalko:/bin/bash
#art:x:1005:1005::/home/art:/bin/bash
#mk:x:1006:1006:MK,,,:/home/mk:/bin/bash
#kamilm:x:1002:1002:Kamil M,,,:/home/kamilm:/bin/bash
#

#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'bdd631d20a97ea1598833e06c4c822f3  /etc/ufw/user.rules'
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
    assert conf.contains("ProxyPass       http://localhost:8080/lustro")

def test_apache2_conf002mirror_ssl(host):
    conf = host.file("/etc/apache2/sites-enabled/002-mirror-ssl.conf")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.contains("SSLEngine on")
    assert conf.contains("VirtualHost mirror.artifact.pl:443")
    assert conf.contains("ServerName mirror.artifact.pl")
    assert conf.contains("ServerAlias.*mirror.artifact.pl")
    assert conf.contains("DocumentRoot /var/www/mirror")
    assert conf.contains("SSLCertificateFile.*/etc/apache2/ssl/artifact.pem")
    assert conf.contains("SSLCertificateKeyFile.*/etc/apache2/ssl/artifact.key")

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_java_running(Process, Service, Socket, Command):
    cron = Process.filter(comm="java")

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://127.0.0.1:5432").is_listening
    assert Socket("tcp://::1:5432").is_listening

def test_pg_isready_output(Command):
    command = Command('/usr/bin/pg_isready')
    assert command.stdout.rstrip() == '/var/run/postgresql:5432 - accepting connections'
    assert command.rc == 0

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.filter(ppid=nginxmaster.pid)
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://:::80").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0


def test_mysql_running(Process, Service, Socket, Command):
    assert Service("mysql").is_enabled
    assert Service("mysql").is_running

    mysql = Process.get(comm="mysqld_safe")
    assert mysql.user == "root"
    assert mysql.group == "root"

    assert Socket("tcp://127.0.0.1:3306").is_listening

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

def test_gsm_wrapper(Process, Service, Socket, Command):
    wrapper = Process.get(user="jboss", ppid='1', comm="wrapper")
    assert wrapper.user == "jboss"
    assert wrapper.group == "jboss"

def test_gsm_wrapper_pid(host,Socket):
    conf = host.file("/opt/sms/bin/./sms_gsmsservice.pid")
    assert conf.user == "jboss"
    assert conf.group == "jboss"
    assert conf.mode == 0o664
    assert Socket("tcp://0.0.0.0:5012").is_listening

def test_activemq_running(Process, Service, Socket, Command):
    assert Service("activemq").is_enabled
    assert Service("activemq").is_running
    amq = Process.get(user="root", ppid='1', comm="java")
    assert amq.user == "root"
    assert amq.group == "root"
    assert Socket("tcp://0.0.0.0:5672").is_listening
    assert Socket("tcp://164.132.30.191:61613").is_listening
    assert Socket("tcp://0.0.0.0:61614").is_listening
    #assert Socket("tcp://0.0.0.0:61616").is_listening
    assert Socket("tcp://0.0.0.0:1883").is_listening
    assert Socket("tcp://0.0.0.0:8161").is_listening
    #assert Socket("tcp://127.0.0.1:61616").is_listening

def test_wildfly_running(Process, Service, Socket, Command):
    standalone = Process.get(user="jboss", ppid='1', comm="standalone.sh")
    assert standalone.user == "jboss"
    assert standalone.group == "jboss"

    wildfly = Process.get(ppid=standalone.pid)
    assert wildfly.user == "jboss"
    assert wildfly.group == "jboss"
    assert wildfly.comm == "java"
    assert Socket("tcp://127.0.0.1:9990").is_listening
    assert Socket("tcp://0.0.0.0:8080").is_listening
    assert Socket("tcp://0.0.0.0:8787").is_listening
    assert Socket("tcp://0.0.0.0:8443").is_listening

def test_zookeeper_running(Process, Service, Socket, Command):
    assert Service("zookeeper").is_enabled
    assert Service("zookeeper").is_running

def test_zookeeper_conf_unchanged(Command):
    command = Command('sudo md5sum /opt/zookeeper/conf/zoo.cfg')
    assert command.stdout.rstrip() == '6b5ee3cf3e8a13723cc5af4fbf2000c8  /opt/zookeeper/conf/zoo.cfg'
    assert command.rc == 0

def test_spinel_website(Command):
    command = Command('curl -sSf "http://spinel.artifact.pl/lustro" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '301'
    assert command.rc == 0

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://127.0.0.1:3306",
"tcp://164.132.30.191:61613",
"tcp://0.0.0.0:61614",
"tcp://0.0.0.0:8080",
#"tcp://0.0.0.0:61616",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:81",
"tcp://0.0.0.0:5012", # java sms
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://127.0.0.1:5433",
"tcp://0.0.0.0:8443",
"tcp://0.0.0.0:1883",
"tcp://127.0.0.1:32000", # java sms
"tcp://0.0.0.0:8161",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:5672",
"tcp://:::80",
"tcp://:::22",
"tcp://:::5432",
"tcp://::1:5433",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening
