# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
##
#root:x:0:0:root:/root:/bin/bash
#adam:x:1000:1000:adam,,,:/home/adam:/bin/bash
#postgres:x:112:119:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
# jboss
#kamilm:x:1003:1003:Kamil M,,,:/home/kamilm:/bin/bash
#
#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'adb25e57e9f83547e77a59a9404db4d0  /etc/ufw/user.rules'
    assert command.rc == 0

def test_mongod_running(Process, Service, Socket, Command):
    assert Service("mongodb").is_enabled
    assert Service("mongodb").is_running

    mongod = Process.get(comm="mongod")
    assert mongod.user == "mongodb"
    assert mongod.group == "nogroup"
    assert Socket("tcp://127.0.0.1:27017").is_listening

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
    assert Socket("tcp://167.114.54.59:443").is_listening
    assert Socket("tcp://:::80").is_listening

def test_activemq_running(Process, Service, Socket, Command):
    assert Service("activemq").is_enabled
    assert Service("activemq").is_running
    #amq = Process.get(comm="java")
    #assert amq.user == "root"
    #assert amq.group == "root"
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
    assert Socket("tcp://:::9090").is_listening

def test_psad_running(Process, Service, Socket, Command):
    assert Service("psad").is_enabled
    assert Service("psad").is_running

    psad = Process.filter(comm="psad")

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

    cron = Process.get(comm="cron")
    assert cron.user == "root"
    assert cron.group == "root"

def test_munin_running(Process, Service, Socket, Command):
    assert Service("munin-node").is_enabled
    assert Service("munin-node").is_running

    munin= Process.get(comm="munin-node")
    assert munin.user == "root"
    assert munin.group == "root"
    assert Socket("tcp://:::4949").is_listening

def test_java_running(Process, Service, Socket, Command):
    java = Process.filter(comm="java")
    assert Socket("tcp://0.0.0.0:1100").is_listening
    assert Socket("tcp://0.0.0.0:61613").is_listening
    assert Socket("tcp://0.0.0.0:61614").is_listening
    assert Socket("tcp://0.0.0.0:61616").is_listening
    assert Socket("tcp://0.0.0.0:1883").is_listening
    assert Socket("tcp://0.0.0.0:8161").is_listening
    assert Socket("tcp://0.0.0.0:5672").is_listening
    assert Socket("tcp://:::9090").is_listening

    #assert Socket("tcp://0.0.0.0:8443").is_listening
    #assert Socket("tcp://127.0.0.1:9990").is_listening

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

#fail2ban.service                           enabled 
def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

# systemctl list-unit-files | grep enabled
#
#root@lynx:/home/kamilm# systemctl list-unit-files | grep enabled



#root@spinel:/home/kamilm#  ls /var/spool/cron/crontabs/


# na kazdym firewall ufw ufw status

# root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
# netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'

##
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://127.0.0.1:27017",
"tcp://0.0.0.0:1100",
"tcp://0.0.0.0:61613",
"tcp://0.0.0.0:61614",
"tcp://0.0.0.0:61616",
"tcp://0.0.0.0:80",
"tcp://167.114.54.59:53",
"tcp://127.0.0.1:53",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:25",
"tcp://127.0.0.1:953",
"tcp://0.0.0.0:1883",
"tcp://0.0.0.0:443",
"tcp://0.0.0.0:8161",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:5672",
"tcp://:::80",
"tcp://:::4949",
"tcp://:::53",
"tcp://:::22",
"tcp://:::25",
"tcp://::1:953",
"tcp://:::9090",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


##procesy
#root@beryl:/home/kamilm# netstat -alnp|grep LIST|head -20
