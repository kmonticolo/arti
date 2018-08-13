# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
#
#root:x:0:0:root:/root:/bin/bash
#adam:x:1000:1000:Adam Bartoszuk,,,:/home/adam:/bin/bash
#postgres:x:106:114:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
#speech-dispatcher:x:119:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/sh
#jboss:x:1004:1004:,,,:/home/jboss:/bin/bash
#splunk:x:1005:1005:Splunk Server:/opt/splunk:/bin/bash
#kamilm:x:1001:1001:Kamil M,,,:/home/kamilm:/bin/bash
#

#bind
def test_bind_running(Process, Service, Socket, Command):
    assert Service("bind9").is_enabled
    assert Service("bind9").is_running

    named = Process.get(comm="named")
    assert named.user == "bind"
    assert named.group == "bind"

    assert Socket("tcp://127.0.0.1:53").is_listening
    assert Socket("tcp://167.114.54.62:53").is_listening
    assert Socket("tcp://127.0.0.1:953").is_listening

#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '50086536504b2ff04835a10e44cd48c9  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

    cron = Process.get(comm="cron")
    assert cron.user == "root"
    assert cron.group == "root"

def test_wildfly_ntms_running(Process, Service, Socket, Command):
    assert Service("wildfly-ntms").is_enabled
    assert Service("wildfly-ntms").is_running
    assert Socket("tcp://164.132.30.190:4747").is_listening
    assert Socket("tcp://0.0.0.0:5010").is_listening
    assert Socket("tcp://127.0.0.1:32001").is_listening
    assert Socket("tcp://0.0.0.0:5011").is_listening
    assert Socket("tcp://127.0.0.1:32002").is_listening
    assert Socket("tcp://164.132.30.190:18181").is_listening
    assert Socket("tcp://127.0.0.1:10000").is_listening
    assert Socket("tcp://0.0.0.0:8090").is_listening
    assert Socket("tcp://0.0.0.0:8453").is_listening
    assert Socket("tcp://0.0.0.0:9797").is_listening

def test_wildfly_vtms_running(Process, Service, Socket, Command):
    assert Service("wildfly-vtms").is_enabled
    assert Service("wildfly-vtms").is_running
    #assert Socket("tcp://0.0.0.0:41616").is_listening
    assert Socket("tcp://0.0.0.0:8080").is_listening
    assert Socket("tcp://0.0.0.0:8787").is_listening
    assert Socket("tcp://0.0.0.0:8443").is_listening
    assert Socket("tcp://127.0.0.1:9990").is_listening

def test_munin_running(Process, Service, Socket, Command):
    assert Service("munin-node").is_enabled
    assert Service("munin-node").is_running

    munin= Process.get(comm="munin-node")
    assert munin.user == "root"
    assert munin.group == "root"

    #assert Socket("tcp://:::4949").is_listening

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://127.0.0.1:5432").is_listening
    assert Socket("tcp://::1:5432").is_listening

def test_pg_isready_output(Command):
    command = Command('/usr/bin/pg_isready')
    assert command.stdout.rstrip() == '/var/run/postgresql:5432 - accepting connections'
    assert command.rc == 0

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_whoopsie_running(Process, Service, Socket, Command):
    assert Service("whoopsie").is_enabled
    assert Service("whoopsie").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.filter(comm="nginx", ppid=nginxmaster.pid)
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://:::80").is_listening

    command = Command('sudo nginx -t')
    assert command.rc == 0


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
##
#cups.service                               enabled 
#dbus-org.bluez.service                     enabled 
#dbus-org.freedesktop.Avahi.service         enabled 
#dbus-org.freedesktop.ModemManager1.service enabled 
#dbus-org.freedesktop.nm-dispatcher.service enabled 
#dbus-org.freedesktop.thermald.service      enabled 
#display-manager.service                    enabled 
#dns-clean.service                          enabled 
#fail2ban.service                           enabled 
#friendly-recovery.service                  enabled 
#getty@.service                             enabled 
#gpu-manager.service                        enabled 
#lightdm.service                            enabled 
#lvm2-monitor.service                       enabled 
#ModemManager.service                       enabled 
#munin-node.service                         enabled 
#network-manager.service                    enabled 
#networking.service                         enabled 
#NetworkManager-dispatcher.service          enabled 
#NetworkManager-wait-online.service         enabled 
#NetworkManager.service                     enabled 
#nginx.service                              enabled 
#postgresql.service                         enabled 
#pppd-dns.service                           enabled 
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
#thermald.service                           enabled 
#ufw.service                                enabled 
#unattended-upgrades.service                enabled 
#ureadahead.service                         enabled 
#whoopsie.service                           enabled 
#zabbix-agent.service                       enabled 
#acpid.socket                               enabled 
#apport-forward.socket                      enabled 
#avahi-daemon.socket                        enabled 
#cups.socket                                enabled 
#dm-event.socket                            enabled 
#lvm2-lvmetad.socket                        enabled 
#lvm2-lvmpolld.socket                       enabled 
#snapd.socket                               enabled 
#uuidd.socket                               enabled 
#remote-fs.target                           enabled 
#apt-daily-upgrade.timer                    enabled 
#apt-daily.timer                            enabled 
#snapd.snap-repair.timer                    enabled 
##
##systemctl list-units --type=service --state=active
#apport.service                     loaded active exited  LSB: automatic crash report generation
#atd.service                        loaded active running Deferred execution scheduler
#cloud-config.service               loaded active exited  Apply the settings specified in cloud-config
#cloud-final.service                loaded active exited  Execute cloud user/final scripts
#cloud-init-local.service           loaded active exited  Initial cloud-init job (pre-networking)
#cloud-init.service                 loaded active exited  Initial cloud-init job (metadata service crawler)
#console-setup.service              loaded active exited  Set console font and keymap
#cron.service                       loaded active running Regular background program processing daemon
#dbus.service                       loaded active running D-Bus System Message Bus
#fail2ban.service                   loaded active running Fail2Ban Service
#getty@tty1.service                 loaded active running Getty on tty1
#grub-common.service                loaded active exited  LSB: Record successful boot for GRUB
#ifup@enp1s0.service                loaded active exited  ifup for enp1s0
#irqbalance.service                 loaded active exited  LSB: daemon to balance interrupts for SMP systems
#iscsid.service                     loaded active running iSCSI initiator daemon (iscsid)
#keyboard-setup.service             loaded active exited  Set console keymap
#kmod-static-nodes.service          loaded active exited  Create list of required static device nodes for the current kernel
#lvm2-lvmetad.service               loaded active running LVM2 metadata daemon
#lvm2-monitor.service               loaded active exited  Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling
#lxcfs.service                      loaded active running FUSE filesystem for LXC
#lxd-containers.service             loaded active exited  LXD - container startup/shutdown
#mdadm.service                      loaded active running LSB: MD monitoring daemon
#networking.service                 loaded active exited  Raise network interfaces
#ondemand.service                   loaded active exited  LSB: Set the CPU Frequency Scaling governor to "ondemand"
#open-iscsi.service                 loaded active exited  Login to default iSCSI targets
#polkitd.service                    loaded active running Authenticate and Authorize Users to Run Privileged Tasks
#postfix.service                    loaded active running LSB: Postfix Mail Transport Agent
#rc-local.service                   loaded active exited  /etc/rc.local Compatibility
#resolvconf.service                 loaded active exited  Nameserver information manager
#rsyslog.service                    loaded active running System Logging Service
#serial-getty@ttyS0.service         loaded active running Serial Getty on ttyS0
#setvtrgb.service                   loaded active exited  Set console scheme
#snapd.service                      loaded active running Snappy daemon
#ssh.service                        loaded active running OpenBSD Secure Shell server
#systemd-journal-flush.service      loaded active exited  Flush Journal to Persistent Storage
#systemd-journald.service           loaded active running Journal Service
#systemd-logind.service             loaded active running Login Service
#systemd-modules-load.service       loaded active exited  Load Kernel Modules
#systemd-random-seed.service        loaded active exited  Load/Save Random Seed
#systemd-remount-fs.service         loaded active exited  Remount Root and Kernel File Systems
#systemd-sysctl.service             loaded active exited  Apply Kernel Variables
#systemd-timesyncd.service          loaded active running Network Time Synchronization
#systemd-tmpfiles-setup-dev.service loaded active exited  Create Static Device Nodes in /dev
#systemd-tmpfiles-setup.service     loaded active exited  Create Volatile Files and Directories
#systemd-udev-trigger.service       loaded active exited  udev Coldplug all Devices
#systemd-udevd.service              loaded active running udev Kernel Device Manager
#systemd-update-utmp.service        loaded active exited  Update UTMP about System Boot/Shutdown
#systemd-user-sessions.service      loaded active exited  Permit User Sessions
#ufw.service                        loaded active exited  Uncomplicated firewall
#unattended-upgrades.service        loaded active exited  Unattended Upgrades Shutdown
#user@1000.service                  loaded active running User Manager for UID 1000
#user@1001.service                  loaded active running User Manager for UID 1001
#uuidd.service                      loaded active running Daemon for generating UUIDs
#virtualbox.service                 loaded active exited  LSB: VirtualBox Linux kernel module
#


# root@lynx:/home/kamilm# ls /var/spool/cron/crontabs/
# jboss
# m h  dom mon dow   command
#0 * * * * find /opt/ppos/doco/load/done/ -type f -mmin +60 -delete
#2 * * * * find /opt/ppos/doco/load/err/ -type f -mmin +60 -delete
#4 * * * * find /opt/ppos/doco/catalog/done/ -type f -mmin +60 -delete
#6 * * * * find /opt/ppos/doco/catalog/err/ -type f -mmin +60 -delete


# na kazdym firewall ufw ufw status

# root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
##
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://127.0.0.1:3306",
"tcp://164.132.30.190:4747",
#"tcp://0.0.0.0:41616",
"tcp://0.0.0.0:8080",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:5010",
"tcp://0.0.0.0:5011",
"tcp://0.0.0.0:8787",
"tcp://164.132.30.190:4949",
"tcp://164.132.30.190:53",
"tcp://127.0.0.1:53",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:631",
"tcp://127.0.0.1:5432",
"tcp://127.0.0.1:953",
"tcp://0.0.0.0:8090",
"tcp://0.0.0.0:8443",
"tcp://0.0.0.0:443",
"tcp://127.0.0.1:32000",
"tcp://127.0.0.1:32001",
"tcp://127.0.0.1:32002",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:8453",
"tcp://0.0.0.0:9797",
"tcp://164.132.30.190:18181",
"tcp://127.0.0.1:9990",
"tcp://:::80",
"tcp://:::53",
"tcp://:::22",
"tcp://::1:631",
"tcp://::1:5432",
"tcp://::1:953"
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


##procesy
#root@beryl:/home/kamilm# netstat -alnp|grep LIST|head -20
#tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      2160/mysqld     
#tcp        0      0 164.132.30.190:4747     0.0.0.0:*               LISTEN      1855/java       
#tcp        0      0 164.132.30.190:4748     0.0.0.0:*               LISTEN      13502/java      
#tcp        0      0 127.0.0.1:10000         0.0.0.0:*               LISTEN      8830/java       
#tcp        0      0 0.0.0.0:41616           0.0.0.0:*               LISTEN      2715/java       
#tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      2715/java       
#tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1572/nginx -g daemo
#tcp        0      0 0.0.0.0:5010            0.0.0.0:*               LISTEN      1855/java       
#tcp        0      0 0.0.0.0:5011            0.0.0.0:*               LISTEN      1857/java       
#tcp        0      0 0.0.0.0:8787            0.0.0.0:*               LISTEN      2715/java       
#tcp        0      0 164.132.30.190:4949     0.0.0.0:*               LISTEN      1540/perl       
#tcp        0      0 164.132.30.190:53       0.0.0.0:*               LISTEN      1114/named      
#tcp        0      0 127.0.0.1:53            0.0.0.0:*               LISTEN      1114/named      
#tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1112/sshd       
#tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      28318/cupsd     
#tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      1187/postgres   
#tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN      1114/named      
#tcp        0      0 0.0.0.0:8090            0.0.0.0:*               LISTEN      8830/java       
#tcp        0      0 0.0.0.0:8443            0.0.0.0:*               LISTEN      2715/java       
#tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN      1572/nginx -g daemo
#
#/usr/sbin/apache2 -k start
#postgres
#/usr/bin/mysqld_safe
#/usr/bin/fail2ban-server
#/usr/sbin/zabbix_server
#
