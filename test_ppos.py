
def test_crond_running(Process, Service, Socket, Command):
    assert Service("crond").is_enabled
    assert Service("crond").is_running

def test_java_running(Process, Service, Socket, Command):
    java = Process.get(comm="java")
    assert java.user == "jboss"
    assert java.group == "jboss"

def test_munin_running(Process, Service, Socket, Command):
    assert Service("munin-node").is_enabled
    assert Service("munin-node").is_running

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql-9.4").is_enabled
    assert Service("postgresql-9.4").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://0.0.0.0:5432").is_listening
    assert Socket("tcp://::1:5432").is_listening

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

# netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:4949",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://0.0.0.0:443",
"tcp://0.0.0.0:8443",
"tcp://0.0.0.0:4447",
"tcp://0.0.0.0:10050",
"tcp://127.0.0.1:9990",
"tcp://127.0.0.1:9999",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:8080",
"tcp://:::22",
"tcp://:::5432",

    ):  
        socket = host.socket(spec)
        assert socket.is_listening


