
def test_crond_running(Process, Service, Socket, Command):
    assert Service("crond").is_enabled
    assert Service("crond").is_running

def test_chronyd_running(Process, Service, Socket, Command):
    assert Service("chronyd").is_enabled
    assert Service("chronyd").is_running


def test_firewalld_running(Process, Service, Socket, Command):
    assert Service("firewalld").is_enabled
    assert Service("firewalld").is_running


def test_java_running(Process, Service, Socket, Command):
    cron = Process.filter(comm="java")

def test_munin_running(Process, Service, Socket, Command):
    assert Service("munin-node").is_enabled
    assert Service("munin-node").is_running


def test_postfix_running(Process, Service, Socket, Command):
    assert Service("postfix").is_enabled
    assert Service("postfix").is_running

    postfix = Process.get(comm="master")

    assert Socket("tcp://127.0.0.1:25").is_listening
#

def test_testlot_website(Command):
    command = Command('curl -s https://testlot.novelpay.pl |grep "POS Lot"')
    assert command.rc == 0


def test_tuned_running(Process, Service, Socket, Command):
    assert Service("tuned").is_enabled
    assert Service("tuned").is_running


def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening


def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:4949",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:25",
"tcp://0.0.0.0:10050",
"tcp://:::8080",
"tcp://:::1521",
"tcp://:::22",
"tcp://:::45656",
"tcp://::1:25",
"tcp://:::10050",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


