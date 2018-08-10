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
# disable when firewalld is in use
#def test_ufw(Command):
#    command = Command('sudo ufw status | grep -qw active')
#    assert command.rc == 0

def test_firewalld_running(Process, Service, Socket, Command):
    assert Service("firewalld").is_enabled
    assert Service("firewalld").is_running

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/iptables-save')
    assert command.stdout.rstrip() == '9df0f21749cd1fae03e9bef0b8182867  /etc/iptables-save'
    assert command.rc == 0

def test_gssproxy_running(Process, Service, Socket, Command):
    assert Service("gssproxy").is_running
    gssproxy= Process.get(comm="munin-node")
    assert gssproxy.user == "root"
    assert gssproxy.group == "root"

def test_crond_running(Process, Service, Socket, Command):
    assert Service("crond").is_enabled
    assert Service("crond").is_running

def test_tuned_running(Process, Service, Socket, Command):
    assert Service("tuned").is_enabled
    assert Service("tuned").is_running

def test_chronyd_running(Process, Service, Socket, Command):
    assert Service("chronyd").is_enabled
    assert Service("chronyd").is_running

def test_munin_running(Process, Service, Socket, Command):
    assert Service("munin-node").is_enabled
    assert Service("munin-node").is_running

    munin= Process.get(comm="munin-node")
    assert munin.user == "root"
    assert munin.group == "root"
    #assert Socket("tcp://:::4949").is_listening

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.filter(ppid=nginxmaster.pid)
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://:::80").is_listening

    command = Command('sudo nginx -t')
    assert command.rc == 0


def test_ora11g_running(Process, Service, Socket, Command):
    proc= Process.filter(comm="oracle")
    #assert Socket("tcp://:::26053").is_listening
    assert Socket("tcp://167.114.54.60:1521").is_listening

def test_oracle_running(Process, Service, Socket, Command):

    proc= Process.get(comm="tnslsnr")
    assert proc.user == "oracle"
    assert proc.group == "oinstall"

    assert Socket("tcp://:::1521").is_listening

#def test_ufw_running(Process, Service, Socket, Command):
    #assert Service("ufw").is_enabled
    #assert Service("ufw").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

#fail2ban.service                           enabled 
#def test_fail2ban_running(Process, Service, Socket, Command):
#    assert Service("fail2ban").is_enabled
#    assert Service("fail2ban").is_running

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
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:4949",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:25",
"tcp://:::25381",
"tcp://:::80",
"tcp://:::1521",
"tcp://:::22",
"tcp://::1:25",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


##procesy
#root@beryl:/home/kamilm# netstat -alnp|grep LIST|head -20
