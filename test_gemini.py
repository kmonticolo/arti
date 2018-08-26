# centos 7

# userzy grep sh$ /etc/passwd
# root adam dpiekarek oracle hklekowicz kamilm

def test_firewalld_running(Process, Service, Socket, Command):
    assert Service("firewalld").is_enabled
    assert Service("firewalld").is_running

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/iptables-save')
    assert command.stdout.rstrip() == '87e0f58ae87e893b300499435ea7599a  /etc/iptables-save'
    assert command.rc == 0

def test_ora11g_running(Process, Service, Socket, Command):
    proc= Process.filter(comm="oracle")
    assert Socket("tcp://:::32098").is_listening

def test_oracle_running(Process, Service, Socket, Command):

    proc= Process.get(comm="tnslsnr")
    assert proc.user == "oracle"
    assert proc.group == "oinstall"

    assert Socket("tcp://:::1521").is_listening

def test_munin_running(Process, Service, Socket, Command):
    assert Service("munin-node").is_enabled
    assert Service("munin-node").is_running

    munin= Process.get(comm="munin-node")
    assert munin.user == "root"
    assert munin.group == "root"

    assert Socket("tcp://0.0.0.0:4949").is_listening

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

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running

    agent = Process.filter(comm="zabbix_agentd")

    assert Socket("tcp://0.0.0.0:10050").is_listening


def test_postfix_running(Process, Service, Socket, Command):
    assert Service("postfix").is_enabled
    assert Service("postfix").is_running

    postfix = Process.get(comm="master")

    assert Socket("tcp://127.0.0.1:25").is_listening

#
## systemctl list-unit-files | grep enabled
#uditd.service                                enabled 
#autovt@.service                               enabled 
#chronyd.service                               enabled 
#crond.service                                 enabled 
#dbus-org.fedoraproject.FirewallD1.service     enabled 
#dbus-org.freedesktop.NetworkManager.service   enabled 
#dbus-org.freedesktop.nm-dispatcher.service    enabled 
#firewalld.service                             enabled 
#getty@.service                                enabled 
#irqbalance.service                            enabled 
#kdump.service                                 enabled 
#lvm2-monitor.service                          enabled 
#microcode.service                             enabled 
#munin-node.service                            enabled 
#NetworkManager-dispatcher.service             enabled 
#NetworkManager.service                        enabled 
#nginx.service                                 enabled 
#postfix.service                               enabled 
#rsyslog.service                               enabled 
#smartd.service                                enabled 
#sshd.service                                  enabled 
#sysstat.service                               enabled 
#systemd-readahead-collect.service             enabled 
#systemd-readahead-drop.service                enabled 
#systemd-readahead-replay.service              enabled 
#tuned.service                                 enabled 
#vgauthd.service                               enabled 
#vmtoolsd.service                              enabled 
#zabbix-agent.service                          enabled 
#dm-event.socket                               enabled 
#lvm2-lvmetad.socket                           enabled 
#lvm2-lvmpolld.socket                          enabled 
#rpcbind.socket                                enabled 
#default.target                                enabled 
#multi-user.target                             enabled 
#nfs-client.target                             enabled 
#remote-fs.target                              enabled 
#runlevel2.target                              enabled 
#runlevel3.target                              enabled 
#runlevel4.target                              enabled 
#
#
#root@lynx:/home/kamilm# systemctl list-unit-files | grep enabled
#systemctl list-units --type=service --state=active


# root@lynx:/home/kamilm# ls /var/spool/cron/crontabs/
# adam  root


#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

# orthphonto.net.conf

# root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
# netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
#"tcp://0.0.0.0:111",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:4949",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:25",
"tcp://0.0.0.0:10050",
#"tcp://:::111",
"tcp://:::80",
"tcp://:::1521",
"tcp://:::22",
"tcp://::1:25",
"tcp://:::32098"
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


