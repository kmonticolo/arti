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

def test_ufw(Command):
    command = Command('sudo ufw status | grep -w "Status: active"')
    assert command.rc == 0

def test_firewalld_unchanged(Command):
    command = Command('sudo md5sum /etc/firewalld/zones/public.xml')
    assert command.stdout.rstrip() == 'adbf9e35a1457739bef223badb0ae583  /etc/firewalld/zones/public.xml'
    assert command.rc == 0

def test_iptables_unchanged(Command):
    command = Command('sudo md5sum /etc/iptables-save')
    assert command.stdout.rstrip() == '9df0f21749cd1fae03e9bef0b8182867  /etc/iptables-save'
    assert command.rc == 0

def test_gssproxy_running(Process, Service, Socket, Command):
    assert Service("gssproxy").is_running
    gssproxy= Process.get(comm="gssproxy")
    assert gssproxy.user == "root"
    assert gssproxy.group == "root"

def test_crond_running(Process, Service, Socket, Command):
    assert Service("crond").is_enabled
    assert Service("crond").is_running

def test_tuned_running(Process, Service, Socket, Command):
    assert Service("tuned").is_enabled
    assert Service("tuned").is_running

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.filter(ppid=nginxmaster.pid)
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://:::80").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0



# startowanie
# sudo su - oracle
# [oracle@taurus ~]$ sqlplus '/ as sysdba'
# SQL> startup
# lsnrctl start
# lsnrctl status

def test_ora11g_running(Process, Service, Socket, Command):
    proc= Process.filter(comm="oracle")
    assert Socket("tcp://0.0.0.0:1521").is_listening

def test_oracle_running(Process, Service, Socket, Command):

    proc= Process.get(comm="tnslsnr")
    assert proc.user == "oracle"
    assert proc.group == "oinstall"

    assert Socket("tcp://0.0.0.0:1521").is_listening

def test_tuned_running(Process, Service, Socket, Command):
    assert Service("tuned").is_enabled
    assert Service("tuned").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:25",
"tcp://:::80",
"tcp://0.0.0.0:1521",
"tcp://:::22",
    ):
        socket = host.socket(spec)
        assert socket.is_listening
