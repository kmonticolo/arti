# z test_alpha

#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '4e5ef832a9a4a51a712b5538906a86cd  /etc/ufw/user.rules'

    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://127.0.0.1:5432").is_listening
    assert Socket("tcp://::1:5432").is_listening

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_zabbix_server_running(Process, Service, Socket, Command):
    assert Service("zabbix-server").is_enabled
    assert Service("zabbix-server").is_running
    assert Socket("tcp://0.0.0.0:10051").is_listening

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_zookeeper_running(Process, Service, Socket, Command):
    assert Service("zookeeper").is_enabled
    assert Service("zookeeper").is_running

def test_zookeeper_conf_unchanged(Command):
    command = Command('sudo md5sum /opt/zookeeper/conf/zoo.cfg')
    assert command.stdout.rstrip() == '9881e316b8148213a089953c408b91e2  /opt/zookeeper/conf/zoo.cfg'
    assert command.rc == 0

def test_mysql_running(Process, Service, Socket, Command):
    assert Service("mysql").is_enabled
    assert Service("mysql").is_running

    mysql = Process.get(comm="mysqld_safe")
    assert mysql.user == "root"
    assert mysql.group == "root"

    assert Socket("tcp://127.0.0.1:3306").is_listening

#fail2ban.service                           enabled
def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

###

def test_activemq_running(Process, Service, Socket, Command):
    assert Service("activemq").is_enabled
    assert Service("activemq").is_running
    assert Socket("tcp://0.0.0.0:1100").is_listening
    assert Socket("tcp://0.0.0.0:61613").is_listening
    assert Socket("tcp://0.0.0.0:61614").is_listening
    assert Socket("tcp://0.0.0.0:61616").is_listening
    assert Socket("tcp://0.0.0.0:1883").is_listening
    assert Socket("tcp://0.0.0.0:8161").is_listening
    assert Socket("tcp://0.0.0.0:5672").is_listening

# z beryl
#bind
def test_bind_running(Process, Service, Socket, Command):
    assert Service("bind9").is_enabled
    assert Service("bind9").is_running

    named = Process.get(comm="named")
    assert named.user == "bind"
    assert named.group == "bind"

    assert Socket("tcp://127.0.0.1:53").is_listening
    assert Socket("tcp://167.114.54.62:53").is_listening
    assert Socket("tcp://127.0.0.1:953").is_listening

# z test_alpha

def test_pg_isready_output(Command):
    command = Command('/usr/bin/pg_isready')
    assert command.stdout.rstrip() == '/var/run/postgresql:5432 - accepting connections'
    assert command.rc == 0

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.get(ppid=nginxmaster.pid)
    assert nginxworker.user == "www-data"
    assert nginxworker.group == "www-data"
    assert nginxworker.comm == "nginx"
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

# z test_db

def test_postfix_running(Process, Service, Socket, Command):
    assert Service("postfix").is_enabled
    assert Service("postfix").is_running

    postfix = Process.get(comm="master")

    assert Socket("tcp://127.0.0.1:25").is_listening

# z test_draco
def test_jenkins_running(Process, Service, Socket, Command):
    assert Service("jenkins").is_enabled
    assert Service("jenkins").is_running
    assert Socket("tcp://0.0.0.0:9090").is_listening

def test_jenkins_website(Command):
    command = Command('curl -sSf "https://qantms.artifact.pl/jenkins/" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '403' or  command.stdout.rstrip() == '000'
    assert command.rc == 22

# z test_ntms

def test_wildfly_running(Process, Service, Socket, Command):
    standalone = Process.get(user="jboss", comm="standalone.sh")
    assert standalone.user == "jboss"
    assert standalone.group == "jboss"

    wildfly = Process.get(ppid=standalone.pid)
    assert wildfly.user == "jboss"
    assert wildfly.group == "jboss"
    assert wildfly.comm == "java"
    assert Socket("tcp://127.0.0.1:10000").is_listening
    assert Socket("tcp://0.0.0.0:8090").is_listening # backend do apache
    assert Socket("tcp://127.0.0.1:61616").is_listening
    assert Socket("tcp://0.0.0.0:8453").is_listening

    # z test_pavo
def test_activemq_running(Process, Service, Socket, Command):
    assert Service("activemq").is_enabled
    assert Service("activemq").is_running
    assert Socket("tcp://0.0.0.0:1100").is_listening
    assert Socket("tcp://0.0.0.0:61613").is_listening
    assert Socket("tcp://0.0.0.0:61614").is_listening
    assert Socket("tcp://0.0.0.0:61616").is_listening
    assert Socket("tcp://0.0.0.0:1883").is_listening
    assert Socket("tcp://0.0.0.0:8161").is_listening
    assert Socket("tcp://0.0.0.0:5672").is_listening


def test_jenkins_running(Process, Service, Socket, Command):
    assert Service("jenkins").is_enabled
    assert Service("jenkins").is_running
    assert Socket("tcp://0.0.0.0:9090").is_listening

def test_psad_running(Process, Service, Socket, Command):
    assert Service("psad").is_enabled
    assert Service("psad").is_running

    psad = Process.filter(comm="psad")

# z test_ppos
import pytest
username = "jboss"

def test_user_exists(host):
    user = host.user("%s" % username)
    assert user.name == "%s" % username
    assert user.group == "%s" % username
    assert user.home == "/home/%s" % username

def test_user_home_exists(host):
    user_home = host.file("/home/%s" % username)
    assert user_home.exists
    assert user_home.is_directory
