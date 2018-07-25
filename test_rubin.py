# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
# adam root postgres kamilm jboss


#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

    cron = Process.get(comm="cron")
    assert cron.user == "root"
    assert cron.group == "root"

#def test_munin_running(Process, Service, Socket, Command):
#    assert Service("munin-node").is_enabled
#    assert Service("munin-node").is_running
#
#    munin= Process.get(comm="munin-node")
#    assert munin.user == "root"
#    assert munin.group == "root"
#
#    assert Socket("tcp://:::4949").is_listening
#
def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://127.0.0.1:5432").is_listening
    assert Socket("tcp://::1:5432").is_listening

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


# nexus
def test_nexus_running(Process, Service, Socket, Command):
    assert Service("nexus").is_enabled
    assert Service("nexus").is_running
    assert Socket("tcp://127.0.0.1:32000").is_listening
    assert Socket("tcp://0.0.0.0:8081").is_listening

# sonar
def test_sonar_running(Process, Service, Socket, Command):
    assert Service("sonar").is_enabled
    assert Service("sonar").is_running
    assert Socket("tcp://127.0.0.1:32001").is_listening
    assert Socket("tcp://:::9000").is_listening

def test_apache2_running(Process, Service, Socket, Command):
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running
    assert Socket("tcp://:::80").is_listening
    assert Socket("tcp://:::443").is_listening

def test_apache2_conf(host):
    conf = host.file("/etc/apache2/sites-enabled/default-ssl.conf")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.contains("VirtualHost repo.artifact.pl:443")
    assert conf.contains("SSLEngine on")
    assert conf.contains("SSLCertificateFile    /etc/apache2/SSL/artifact.pem")
    assert conf.contains("SSLCertificateKeyFile /etc/apache2/SSL/artifact.key")
    assert conf.contains("ProxyPass               http://localhost:9000/sonar")
    assert conf.contains("ProxyPassReverse        /sonar")
    assert conf.contains("ProxyPass.*http://localhost:8081/nexus")
    assert conf.contains("ProxyPassReverse.*/nexus")


# systemctl list-unit-files | grep enabled
##
##
#acpid.path                                 enabled 
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
#acpid.socket                               enabled 
#apport-forward.socket                      enabled 
#dm-event.socket                            enabled 
#lvm2-lvmetad.socket                        enabled 
#lvm2-lvmpolld.socket                       enabled 
#rpcbind.socket                             enabled 
#uuidd.socket                               enabled 
#nfs-client.target                          enabled 
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
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://127.0.0.1:5433",
"tcp://127.0.0.1:32000",
"tcp://127.0.0.1:32001",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:8081",
"tcp://:::22",
"tcp://:::5432",
"tcp://::1:5433",
"tcp://:::443",
"tcp://:::9000",
"tcp://:::80",
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
