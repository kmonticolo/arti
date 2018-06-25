# ubuntu 16.04

# userzy grep sh$ /etc/passwd
# root adam jboss op porgres kamilm

def test_mongod_running(Process, Service, Socket, Command):
    assert Service("mongod").is_enabled
    assert Service("mongod").is_running

    mongod = Process.get(comm="mongod")
    assert mongod.user == "mongodb"
    assert mongod.group == "mongodb"

    assert Socket("tcp://127.0.0.1:27017").is_listening

def test_bind_running(Process, Service, Socket, Command):
    assert Service("bind9").is_enabled
    assert Service("bind9").is_running

    named = Process.get(comm="named")
    assert named.user == "bind"
    assert named.group == "bind"

    assert Socket("tcp://127.0.0.1:53").is_listening
    assert Socket("tcp://167.114.54.62:53").is_listening
    assert Socket("tcp://127.0.0.1:953").is_listening

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

    named = Process.get(comm="cron")
    assert named.user == "root"
    assert named.group == "root"


# systemctl list-unit-files | grep enabled
#
#root@lynx:/home/kamilm# systemctl list-unit-files | grep enabled
#acpid.path                                 enabled
#accounts-daemon.service                    enabled
#atd.service                                enabled
#autovt@.service                            enabled
#bind9.service                              enabled ok
#cron.service                               enabled
#friendly-recovery.service                  enabled
#getty@.service                             enabled
#iscsi.service                              enabled
#iscsid.service                             enabled
#lvm2-monitor.service                       enabled
#lxcfs.service                              enabled
#lxd-containers.service                     enabled
#mongod.service                             enabled
#munin-node.service                         enabled
#networking.service                         enabled
#nginx.service                              enabled
#open-iscsi.service                         enabled
#open-vm-tools.service                      enabled
#postgresql.service                         enabled
#resolvconf.service                         enabled
#rsyslog.service                            enabled
#snapd.autoimport.service                   enabled
#snapd.core-fixup.service                   enabled
#snapd.seeded.service                       enabled
#snapd.service                              enabled
#snapd.system-shutdown.service              enabled
#ssh.service                                enabled
#sshd.service                               enabled
#syslog.service                             enabled
#systemd-timesyncd.service                  enabled
#ufw.service                                enabled
#unattended-upgrades.service                enabled
#ureadahead.service                         enabled
#vgauth.service                             enabled
#zabbix-agent.service                       enabled
#acpid.socket                               enabled
#apport-forward.socket                      enabled
#dm-event.socket                            enabled
#lvm2-lvmetad.socket                        enabled
#lvm2-lvmpolld.socket                       enabled
#lxd.socket                                 enabled
#snapd.socket                               enabled
#uuidd.socket                               enabled
#remote-fs.target                           enabled
#apt-daily-upgrade.timer                    enabled
#apt-daily.timer                            enabled
#certbot.timer                              enabled
#phpsessionclean.timer                      enabled
#snapd.snap-repair.timer                    enabled
#
#systemctl list-units --type=service --state=active


# root@lynx:/home/kamilm# ls /var/spool/cron/crontabs/
# adam  root

# na kazdym firewall ufw ufw status

# certbot od letsencrypt plugins nginx

# orthphonto.net.conf

# root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
#tcp        0      0 167.114.54.62:53        0.0.0.0:*               LISTEN      1352/named      
#tcp        0      0 127.0.0.1:53            0.0.0.0:*               LISTEN      1352/named      
#tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1346/sshd       
#tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      1553/postgres   
#tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      2560/master     
#tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN      1352/named      
#tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN      2254/nginx -g daemo
#tcp        0      0 0.0.0.0:10050           0.0.0.0:*               LISTEN      1546/zabbix_agentd
#tcp        0      0 127.0.0.1:27017         0.0.0.0:*               LISTEN      1353/mongod     
#tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      2011/mysqld     
#tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      2254/nginx -g daemo
#tcp6       0      0 :::4949                 :::*                    LISTEN      1564/perl       
#tcp6       0      0 :::22                   :::*                    LISTEN      1346/sshd       
#tcp6       0      0 ::1:5432                :::*                    LISTEN      1553/postgres   
#tcp6       0      0 :::25                   :::*                    LISTEN      2560/master     
#tcp6       0      0 :::443                  :::*                    LISTEN      2254/nginx -g daemo
#tcp6       0      0 :::10080                :::*                    LISTEN      2293/apache2    
#tcp6       0      0 :::80                   :::*                    LISTEN      2254/nginx -g daemo
#


