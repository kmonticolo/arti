#centos
def test_firewalld_running(Process, Service, Socket, Command):
    assert Service("firewalld").is_enabled
    assert Service("firewalld").is_running

# disabled requiretty in sudoers
def test_firewalld_unchanged(Command):
    command = Command('sudo md5sum /etc/firewalld/zones/public.xml')
    assert command.stdout.rstrip() == '1542409df1003196d5d68df81e164d72  /etc/firewalld/zones/public.xml'
    assert command.rc == 0

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

def test_oracle_running(Process, Service, Socket, Command):
    assert Service("oracle-xe").is_enabled
    assert Service("oracle-xe").is_running
    assert Socket("tcp://0.0.0.0:1521").is_listening

def test_tnslsnr_running(Process, Service, Socket, Command):
    proc= Process.get(comm="tnslsnr")
    assert proc.user == "oracle"
    assert proc.group == "dba"
    assert Socket("tcp://0.0.0.0:1521").is_listening

def test_java_running(Process, Service, Socket, Command):
    java = Process.filter(user="vcs", ppid='1', comm="java")

# su - vcs
# cd /home/vcs/apache-openejb-4.5.0-sim
# nohup ./bin/openejb start &
def test_openejb_running(Process, Service, Socket, Command):
    openejb = Process.get(user="vcs", ppid='1', comm="openejb")
    assert openejb.user == "vcs"
    assert openejb.group == "vcs"
    assert Socket("tcp://127.0.0.1:4200").is_listening 
    assert Socket("tcp://127.0.0.1:4201 ").is_listening
    assert Socket("tcp://127.0.0.1:4203").is_listening 
    assert Socket("tcp://0.0.0.0:1099").is_listening
    assert Socket("tcp://127.0.0.1:4204").is_listening
    assert Socket("tcp://0.0.0.0:61613").is_listening

def test_vcs_running(Process, Service, Socket, Command):
    assert Service("vcs").is_enabled
    assert Service("vcs").is_running

# /app/CommunicationModule/bin/ep2_server status
#def test_ep2_server_running(Command):
    #command = Command('/app/CommunicationModule/bin/ep2_server status|grep -c STARTED.*STARTED$')
    #assert command.stdout.rstrip() == '1'
    #assert command.rc == 0

def test_si_config_server_running(Command):
    command = Command('/app/CommunicationModule/bin/si-config-server status')
    assert command.stdout.rstrip() == 'Si Config Server is running'
    assert command.rc == 0


#dopisac standalone
# sudo su - jboss
# cd /app/jboss
# ./bin/start_tms.sh ; tail -F standalone/log/server.log
#po tym service vcs start

# boss    14124  0.1  0.0 113176  1544 pts/0    S    20:55   0:00 /bin/sh ./bin/standalone.sh -b 0.0.0.0 --debug 9797

def test_hostSimulator_running(Process, Service, Socket, Command):
    assert Service("hostSimulator").is_enabled
    assert Service("hostSimulator").is_running

def test_rsyslogd_running(Process, Service, Socket, Command):
    assert Service("rsyslog").is_enabled
    assert Service("rsyslog").is_running

def test_crond_running(Process, Service, Socket, Command):
    assert Service("crond").is_enabled
    assert Service("crond").is_running

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
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:10080",
"tcp://0.0.0.0:8199",
"tcp://0.0.0.0:8201",
"tcp://0.0.0.0:8202",
"tcp://0.0.0.0:1521",
"tcp://0.0.0.0:61234",
"tcp://0.0.0.0:8186",
"tcp://0.0.0.0:8187",
"tcp://0.0.0.0:8188",
"tcp://0.0.0.0:8189",
"tcp://0.0.0.0:8190",
"tcp://0.0.0.0:8191",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening
