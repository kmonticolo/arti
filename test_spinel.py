# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
#
#root:x:0:0:root:/root:/bin/bash
#adam:x:1000:1000:Adam Bartoszuk,,,:/home/adam:/bin/bash
#jboss:x:1001:1001:,,,:/home/jboss:/bin/bash
#postgres:x:106:114:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
#pjakubowski:x:1003:1003:Piotr Jakubowski,,,:/home/pjakubowski:/bin/bash
#tgalko:x:1004:1004:Tomasz Galko,,,:/home/tgalko:/bin/bash
#art:x:1005:1005::/home/art:/bin/bash
#mk:x:1006:1006:MK,,,:/home/mk:/bin/bash
#kamilm:x:1002:1002:Kamil M,,,:/home/kamilm:/bin/bash
#

#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_apache2_running(Process, Service, Socket, Command):
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running
    assert Socket("tcp://:::80").is_listening

#000-default.conf  002-mirror-ssl.conf
def test_apache2_conf000default(host):
    conf = host.file("/etc/apache2/sites-enabled/000-default.conf")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.contains("ProxyPass       http://localhost:8080/lustro")

def test_apache2_conf002mirror_ssl(host):
    conf = host.file("/etc/apache2/sites-enabled/002-mirror-ssl.conf")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.contains("SSLEngine on")
    assert conf.contains("VirtualHost mirror.artifact.pl:443")
    assert conf.contains("ServerName mirror.artifact.pl")
    assert conf.contains("ServerAlias.*mirror.artifact.pl")
    assert conf.contains("DocumentRoot /var/www/mirror")
    assert conf.contains("SSLCertificateFile.*/etc/apache2/ssl/artifact.pem")
    assert conf.contains("SSLCertificateKeyFile.*/etc/apache2/ssl/artifact.key")

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

    cron = Process.get(comm="cron")
    assert cron.user == "root"
    assert cron.group == "root"

def test_java_running(Process, Service, Socket, Command):
    cron = Process.filter(comm="java")

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

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginx = Process.filter(comm="nginx")

    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://:::80").is_listening

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

# sms_gsmsservice
    #wrapper = Process.get(comm="/opt/sms/bin/./wrapper")
def test_gsm_wrapper(Process, Service, Socket, Command):
    wrapper = Process.get(comm="wrapper")
    assert wrapper.user == "jboss"
    assert wrapper.group == "jboss"
def test_gsm_wrapper_pid(host):
    conf = host.file("/opt/sms/bin/./sms_gsmsservice.pid")
    assert conf.user == "jboss"
    assert conf.group == "jboss"
    assert conf.mode == 0o664




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


#root@spinel:/home/kamilm#  ls /var/spool/cron/crontabs/
#adam  jboss  root


# na kazdym firewall ufw ufw status

# root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
# netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'

##
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://127.0.0.1:3306",
"tcp://164.132.30.191:61613",
"tcp://0.0.0.0:61614",
"tcp://0.0.0.0:8080",
"tcp://0.0.0.0:61616",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:81",
"tcp://0.0.0.0:8787",
"tcp://0.0.0.0:5012", # java sms
"tcp://164.132.30.191:4949",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://0.0.0.0:42297",
"tcp://127.0.0.1:5433",
"tcp://0.0.0.0:8443",
"tcp://0.0.0.0:1883",
"tcp://127.0.0.1:32000", # java sms
"tcp://0.0.0.0:8161",
"tcp://0.0.0.0:10050",
"tcp://127.0.0.1:9990",
"tcp://0.0.0.0:5672",
"tcp://:::80",
"tcp://:::22",
"tcp://:::5432",
"tcp://::1:5433",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


##procesy
#root@beryl:/home/kamilm# netstat -alnp|grep LIST|head -20
