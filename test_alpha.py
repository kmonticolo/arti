
def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

    named = Process.get(comm="cron")
    assert named.user == "root"

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

def test_java_running(Process, Service, Socket, Command):
    cron = Process.filter(comm="java")


def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginx = Process.filter(comm="nginx")


def test_nginxvalidate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

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




# netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'
#
#
#def test_listening_socket(host):
#    listening = host.socket.get_listening_sockets()
#    for spec in (
#"tcp://0.0.0.0:22",
#    ):  
#        socket = host.socket(spec)
#        assert socket.is_listening
#
#
