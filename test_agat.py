# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
# adam root mmursztyn postgres kamilm


#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'd42f0f311ada611dfda81b1af37189d0  /etc/ufw/user.rules'

    assert command.rc == 0

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

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://127.0.0.1:5432").is_listening
    assert Socket("tcp://::1:5432").is_listening

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_zabbix_server_running(Process, Service, Socket, Command):
    assert Service("zabbix-server").is_enabled
    assert Service("zabbix-server").is_running
    assert Socket("tcp://0.0.0.0:10051").is_listening


def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening


def test_mysql_running(Process, Service, Socket, Command):
    assert Service("mysql").is_enabled
    assert Service("mysql").is_running

    mysql = Process.get(comm="mysqld_safe")
    assert mysql.user == "root"
    assert mysql.group == "root"

    assert Socket("tcp://127.0.0.1:3306").is_listening

#fail2ban.service                           enabled 
def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running


# systemctl list-unit-files | grep enabled
#
#root@lynx:/home/kamilm# systemctl list-unit-files | grep enabled
## acpid.path                                 enabled 
#accounts-daemon.service                    enabled 
#atd.service                                enabled 
#autovt@.service                            enabled 
#cgmanager.service                          enabled 
#cgproxy.service                            enabled 
#cron.service                               enabled 
#dbus-org.freedesktop.thermald.service      enabled 
#dns-clean.service                          enabled 
#fail2ban.service                           enabled 
#friendly-recovery.service                  enabled 
#getty@.service                             enabled 
#lvm2-monitor.service                       enabled 
#munin-node.service                         enabled 
#networking.service                         enabled 
#postgresql.service                         enabled 
#pppd-dns.service                           enabled 
#resolvconf.service                         enabled 
#rsyslog.service                            enabled 
#ssh.service                                enabled 
#sshd.service                               enabled 
#syslog.service                             enabled 
#systemd-timesyncd.service                  enabled 
#thermald.service                           enabled 
#ufw.service                                enabled 
#unattended-upgrades.service                enabled 
#ureadahead.service                         enabled 
#zabbix-agent.service                       enabled 
#zabbix-server.service                      enabled 
#acpid.socket                               enabled 
#apport-forward.socket                      enabled 
#dm-event.socket                            enabled 
#lvm2-lvmetad.socket                        enabled 
#lvm2-lvmpolld.socket                       enabled 
#uuidd.socket                               enabled 
#remote-fs.target                           enabled 
#apt-daily-upgrade.timer                    enabled 
#apt-daily.timer                            enabled 
#
#systemctl list-units --type=service --state=active


# root@lynx:/home/kamilm# ls /var/spool/cron/crontabs/
# brak

# na kazdym firewall ufw ufw status

# root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
##
#tcp        0      0 0.0.0.0:4949            0.0.0.0:*               LISTEN      969/perl        
#tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      887/sshd        
#tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      979/postgres    
#tcp        0      0 0.0.0.0:10050           0.0.0.0:*               LISTEN      970/zabbix_agentd
#tcp        0      0 0.0.0.0:10051           0.0.0.0:*               LISTEN      27578/zabbix_server
#tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      4360/mysqld     
#tcp6       0      0 :::22                   :::*                    LISTEN      887/sshd        
#tcp6       0      0 ::1:5432                :::*                    LISTEN      979/postgres    
#tcp6       0      0 :::10051                :::*                    LISTEN      27578/zabbix_server
#tcp6       0      0 :::80                   :::*                    LISTEN      1289/apache2    
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:4949",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:5432",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:10051",
"tcp://127.0.0.1:3306",
"tcp://:::22",
"tcp://::1:5432",
"tcp://:::10051",
"tcp://:::80"
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


#procesy
#/usr/sbin/apache2 -k start
#postgres
#/usr/bin/mysqld_safe
#/usr/bin/fail2ban-server
#/usr/sbin/zabbix_server
#
