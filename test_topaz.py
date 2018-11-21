# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
# root postgres adam jboss munin fecru kamilm

#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'bb2f7d8e69fe6fa9bdaff3d3ba04c658  /etc/ufw/user.rules'
    assert command.rc == 0

def test_jira_website(Command):
    command = Command('curl -sSf https://jira.artifact.pl -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_confluence_website(Command):
    command = Command('curl -sSf "https://confluence.artifact.pl/login.action?os_destination=%2Findex.action&permissionViolation=true" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_demo_website(Command):
    command = Command('curl -sSf "https://demo.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_topaz_website(Command):
    command = Command('curl -sSf "http://topaz.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_vtms_website(Command):
    command = Command('curl -sSf "https://vtms.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_vtms1_website(Command):
    command = Command('curl -sSf "https://vtms1.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_vtms2_website(Command):
    command = Command('curl -sSf "https://vtms2.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_fisheye_website(Command):
    command = Command('curl -sSf "https://fisheye.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_pst_http_website(Command):
    command = Command('curl -sSf "http://pst.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_pst_https_website(Command):
    command = Command('curl -sSf "https://pst.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '302'
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

def test_pg_isready_output(Command):
    command = Command('/usr/bin/pg_isready')
    assert command.stdout.rstrip() == '/var/run/postgresql:5432 - accepting connections'
    assert command.rc == 0

def test_mysql_running(Process, Service, Socket, Command):
    assert Service("mysql").is_enabled
    #assert Service("mysql").is_running
    mysql = Process.get(comm="mysqld_safe")
    assert mysql.user == "root"
    assert mysql.group == "root"
    assert Socket("tcp://127.0.0.1:3306").is_listening

def test_apache2_running(Process, Service, Socket, Command):
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running
    assert Socket("tcp://:::80").is_listening

def test_apache_validate(Command):
    command = Command('sudo apache2ctl -t')
    assert command.rc == 0

#def test_apache2_conf000default(host):
#    conf = host.file("/etc/apache2/sites-enabled/000-default.conf")
#    assert conf.user == "root"
#    assert conf.group == "root"
#    assert conf.contains("ProxyPass       http://localhost:8080/lustro")
#
##000-default.conf           002-demo-ssl.conf          004-vtms-cluster-ssl.conf  006-vtms-node2-ssl.conf    008-confluence-ssl.conf    default-ssl.conf           
##001-jira-ssl.conf          003-topaz-ssl.conf         005-vtms-node1-ssl.conf    007-fisheye-ssl.conf       009-pst-ssl.conf           
#
#def test_apache2_conf002mirror_ssl(host):
#    conf = host.file("/etc/apache2/sites-enabled/002-mirror-ssl.conf")
#    assert conf.user == "root"
#    assert conf.group == "root"
#    assert conf.contains("SSLEngine on")
#    assert conf.contains("VirtualHost mirror.artifact.pl:443")
#    assert conf.contains("ServerName mirror.artifact.pl")
#    assert conf.contains("ServerAlias.*mirror.artifact.pl")
#    assert conf.contains("DocumentRoot /var/www/mirror")
#    assert conf.contains("SSLCertificateFile.*/etc/apache2/ssl/artifact.pem")
#    assert conf.contains("SSLCertificateKeyFile.*/etc/apache2/ssl/artifact.key")
#
def test_fisheye_running(Process, Service, Socket, Command):
    assert Service("fisheye").is_enabled
    assert Service("fisheye").is_running

def test_jira_running(Process, Service, Socket, Command):
    assert Service("jira").is_enabled
    assert Service("jira").is_running
    jira = Process.get(user="jira", comm="java")
    assert jira.user == "jira"
    assert jira.group == "jira"
    assert Socket("tcp://:::9090").is_listening
    assert Socket("tcp://:::9095").is_listening
    assert Socket("tcp://127.0.0.1:9095").is_listening

def test_confluence_running(Process, Service, Socket, Command):
    assert Service("confluence").is_enabled
    assert Service("confluence").is_running
    #conflu = Process.get(user="confluence", comm="java")
    #assert conflu.user == "confluence"
    #assert conflu.group == "confluence"
    assert Socket("tcp://:::8090").is_listening
    #assert Socket("tcp://127.0.0.1:8000").is_listening

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_haproxy_running(Process, Service, Socket, Command):
    assert Service("haproxy").is_enabled
    assert Service("haproxy").is_running
    assert Socket("tcp://0.0.0.0:9084").is_listening
    assert Socket("tcp://0.0.0.0:9085").is_listening
    #assert Socket("udp://0.0.0.0:37743").is_listening

def test_haproxy_config_test(Command):
    command = Command('sudo haproxy -c -V -f /etc/haproxy/haproxy.cfg')
    assert command.rc == 0

def test_haproxy_conf(host):
    conf = host.file("/etc/haproxy/haproxy.cfg")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.mode == 0o644
    assert conf.contains("bind \*:9085")
    assert conf.contains("bind \*:9084")


#fail2ban.service                           enabled 
def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

#
### systemctl list-unit-files | grep enabled
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
#haproxy.service                            enabled 
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
#
#systemctl list-units --type=service --state=active


# root@lynx:/home/kamilm# ls /var/spool/cron/crontabs/
# brak

# na kazdym firewall ufw ufw status

## root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
## netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'

#
##
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:5432",
"tcp://127.0.0.1:5433",
"tcp://0.0.0.0:9084",
"tcp://0.0.0.0:9085",
"tcp://0.0.0.0:10050",
"tcp://127.0.0.1:3306",
#"tcp://0.0.0.0:33297",
"tcp://0.0.0.0:22",
"tcp://:::5432",
"tcp://::1:5433",
"tcp://:::8090",
"tcp://:::443",
#"tcp://127.0.0.1:8000",
"tcp://:::9090",
#"tcp://:::36770",
"tcp://:::9095",
#"tcp://127.0.0.1:9005",
"tcp://:::80",
"tcp://:::4949",
"tcp://:::22"
    ):
        socket = host.socket(spec)
        assert socket.is_listening


#procesy
# apache jiraI# 
