# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
#root postgres adam mlickiewicz art kamilm


#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'f07b19adab82b8d320aa88896d84c998  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_samba_ad_dc_running(Process, Service, Socket, Command):
    assert Service("samba-ad-dc").is_enabled
    assert Service("samba-ad-dc").is_running

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

def test_pg_isready_output(Command):
    command = Command('/usr/bin/pg_isready')
    assert command.stdout.rstrip() == '/var/run/postgresql:5432 - accepting connections'
    assert command.rc == 0

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

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0


def test_website(Command):
    command = Command('curl -sSfk http://diament.artifact.pl -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0


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


## systemctl list-unit-files | grep enabled
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
#haveged.service                            enabled 
#lvm2-monitor.service                       enabled 
#munin-node.service                         enabled 
#networking.service                         enabled 
#nfs-kernel-server.service                  enabled 
#nfs-server.service                         enabled 
#nginx.service                              enabled 
#postgresql.service                         enabled 
#pppd-dns.service                           enabled 
#resolvconf.service                         enabled 
#rsyslog.service                            enabled 
#ssh.service                                enabled 
#sshd.service                               enabled 
#sssd.service                               enabled 
#strongswan.service                         enabled 
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
#
#systemctl list-units --type=service --state=active


# root@lynx:/home/kamilm# ls /var/spool/cron/crontabs/
# brak

# na kazdym firewall ufw ufw status

## root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
## netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'

#tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      7869/postgres   
#tcp        0      0 127.0.0.1:5433          0.0.0.0:*               LISTEN      7868/postgres   
#tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN      1009/nginx -g daemo
#tcp        0      0 0.0.0.0:445             0.0.0.0:*               LISTEN      2238/smbd       
#tcp        0      0 0.0.0.0:36321           0.0.0.0:*               LISTEN      -               
#tcp        0      0 0.0.0.0:2049            0.0.0.0:*               LISTEN      -               
#tcp        0      0 0.0.0.0:10050           0.0.0.0:*               LISTEN      7860/zabbix_agentd
#tcp        0      0 0.0.0.0:38212           0.0.0.0:*               LISTEN      886/rpc.mountd  
#tcp        0      0 0.0.0.0:139             0.0.0.0:*               LISTEN      2238/smbd       
#tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      883/rpcbind     
#tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1009/nginx -g daemo
#tcp        0      0 0.0.0.0:37360           0.0.0.0:*               LISTEN      886/rpc.mountd  
#tcp        0      0 0.0.0.0:4949            0.0.0.0:*               LISTEN      1053/perl       
#tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      856/sshd        
#tcp        0      0 0.0.0.0:46902           0.0.0.0:*               LISTEN      886/rpc.mountd  
#tcp6       0      0 ::1:5432                :::*                    LISTEN      7869/postgres   
#tcp6       0      0 ::1:5433                :::*                    LISTEN      7868/postgres   
#tcp6       0      0 :::35547                :::*                    LISTEN      -               
#tcp6       0      0 :::55004                :::*                    LISTEN      886/rpc.mountd  
#tcp6       0      0 :::445                  :::*                    LISTEN      2238/smbd       
#
##
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://127.0.0.1:5432",
"tcp://127.0.0.1:5433",
"tcp://0.0.0.0:443",
"tcp://0.0.0.0:445",
"tcp://0.0.0.0:2049",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:139",
"tcp://0.0.0.0:111",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:4949",
"tcp://0.0.0.0:22",
"tcp://:::445",
"tcp://:::2049",
"tcp://:::139",
"tcp://:::111",
"tcp://:::80",
"tcp://:::22"
    ):
        socket = host.socket(spec)
        assert socket.is_listening


#procesy
