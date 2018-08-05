def test_apache2_running(Process, Service, Socket, Command):
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running
    assert Socket("tcp://:::80").is_listening
    assert Socket("tcp://:::443").is_listening


def test_mysql_running(Process, Service, Socket, Command):
    assert Service("mysql").is_enabled
    assert Service("mysql").is_running

    mysql = Process.get(comm="mysqld")
    assert mysql.user == "mysql"
    assert mysql.group == "mysql"

    assert Socket("tcp://127.0.0.1:3306").is_listening

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

    cron = Process.get(comm="cron")
    assert cron.user == "root"
    assert cron.group == "root"

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running


def test_lua_running(Process, Service, Socket, Command):
    lua = Process.get(comm="lua5.1")
    assert lua.user == "prosody"
    assert lua.group == "prosody"

def test_java_running(Process, Service, Socket, Command):
    cron = Process.filter(comm="java")

def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running


def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://127.0.0.1:3306",
"tcp://0.0.0.0:5322",
"tcp://0.0.0.0:41483",
"tcp://0.0.0.0:4369",
"tcp://0.0.0.0:5269",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:7000",
"tcp://127.0.0.1:25",
"tcp://127.0.0.1:42046",
"tcp://0.0.0.0:5280",
"tcp://0.0.0.0:8224",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:27010",
"tcp://0.0.0.0:389",
"tcp://0.0.0.0:5222",
"tcp://0.0.0.0:5223",
"tcp://0.0.0.0:5224",
"tcp://0.0.0.0:5000",
"tcp://:::5322",
"tcp://:::8080",
"tcp://:::80",
"tcp://:::8081",
"tcp://:::4369",
"tcp://:::61234",
"tcp://:::22",
"tcp://:::8091",
"tcp://:::8060",
"tcp://:::8061",
"tcp://:::10050",
"tcp://:::389",
"tcp://:::8005",
"tcp://:::8070",
"tcp://:::8007",
"tcp://:::5223",
"tcp://:::5224",
"tcp://:::9000",
"tcp://:::5000",

    ):  
        socket = host.socket(spec)
        assert socket.is_listening
