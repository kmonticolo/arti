#centos
def test_oracle_running(Process, Service, Socket, Command):
    assert Service("oracle-xe").is_enabled
    assert Service("oracle-xe").is_running

def test_rsyslogd_running(Process, Service, Socket, Command):
    assert Service("rsyslog").is_enabled
    assert Service("rsyslog").is_running

def test_crond_running(Process, Service, Socket, Command):
    assert Service("crond").is_enabled
    assert Service("crond").is_running

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

def test_tuned_running(Process, Service, Socket, Command):
    assert Service("tuned").is_enabled
    assert Service("tuned").is_running


def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening


# netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:10050",
"tcp://127.0.0.1:4200",
"tcp://127.0.0.1:4201",
"tcp://127.0.0.1:4203",
"tcp://0.0.0.0:1099",
"tcp://127.0.0.1:4204",
"tcp://0.0.0.0:61613",
"tcp://0.0.0.0:37166",
"tcp://0.0.0.0:4949",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:25",
"tcp://:::10080",
"tcp://:::8199",
"tcp://127.0.0.1:8200",
"tcp://:::8201",
"tcp://:::8202",
"tcp://:::1521",
"tcp://:::61234",
"tcp://:::22",
"tcp://:::58616",
"tcp://::1:25",
"tcp://:::8186",
"tcp://:::8187",
"tcp://:::8188",
"tcp://:::8189",
"tcp://:::8190",
"tcp://:::8191",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


