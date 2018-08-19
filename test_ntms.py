def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/iptables/rules.v4')
    assert command.stdout.rstrip() == '2103744b296b904068ec39defa201b71  /etc/iptables/rules.v4'
    assert command.rc == 0
    command = Command('sudo md5sum /etc/ufw/before.init')
    assert command.stdout.rstrip() == 'cd7783526a1a2b25581cecd3c2daa1a4  /etc/ufw/before.init'
    assert command.rc == 0
    command = Command('sudo md5sum /etc/ufw/before.rules')
    assert command.stdout.rstrip() == 'ba34f926d08b14b2ba22aadc5d077a5b  /etc/ufw/before.rules'
    assert command.rc == 0

def test_apache2_running(Process, Service, Socket, Command):
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running
    assert Socket("tcp://:::80").is_listening
    assert Socket("tcp://:::443").is_listening

def test_apache_validate(Command):
    command = Command('sudo apache2ctl -t')
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

    cron= Process.get(comm="cron")
    assert cron.user == "root"
    assert cron.group == "root"

def test_java_running(Process, Service, Socket, Command):
    cron = Process.filter(comm="java")

def test_wildfly_running(Process, Service, Socket, Command):
    standalone = Process.get(user="jboss", ppid='1', comm="standalone.sh")
    assert standalone.user == "jboss"
    assert standalone.group == "jboss"

    wildfly = Process.get(ppid=standalone.pid)
    assert wildfly.user == "jboss"
    assert wildfly.group == "jboss"
    assert wildfly.comm == "java"
    assert Socket("tcp://127.0.0.1:10000").is_listening
    assert Socket("tcp://0.0.0.0:8090").is_listening
    assert Socket("tcp://127.0.0.1:62626").is_listening
    assert Socket("tcp://0.0.0.0:8453").is_listening

def test_munin_running(Process, Service, Socket, Command):
    assert Service("munin-node").is_enabled
    assert Service("munin-node").is_running

    munin= Process.get(comm="munin-node")
    assert munin.user == "root"

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

def test_pg_isready_output(Command):
    command = Command('/usr/bin/pg_isready')
    assert command.stdout.rstrip() == '/var/run/postgresql:5432 - accepting connections'
    assert command.rc == 0

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://127.0.0.1:10000",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://0.0.0.0:8090",
"tcp://0.0.0.0:10050",
"tcp://127.0.0.1:62626",
"tcp://0.0.0.0:8453",
"tcp://:::80",
"tcp://:::4949",
"tcp://:::22",
"tcp://:::5432",
"tcp://:::443",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


