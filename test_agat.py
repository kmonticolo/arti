# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
# adam root mmursztyn postgres kamilm


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

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:5432",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:10051",
"tcp://127.0.0.1:3306",
"tcp://:::22",
"tcp://::1:5432",
"tcp://:::10051",
"tcp://:::80"
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


#procesy
#/usr/sbin/apache2 -k start
#postgres
#/usr/bin/mysqld_safe
#/usr/bin/fail2ban-server
#/usr/sbin/zabbix_server
#
