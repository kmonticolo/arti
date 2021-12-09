# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
# adam root postgres kamilm jboss

def test_is_onet_reachable(Command):
    command = Command('timeout 5 wget onet.pl -o /dev/null')
    assert command.rc != 0

#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -w "Status: active"')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '651c57df2b3b7622359ff2bc5e8c30bd  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://0.0.0.0:5432").is_listening

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

#fail2ban.service                           enabled
def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

# nexus
def test_nexus_running(Process, Service, Socket, Command):
    assert Service("nexus").is_enabled
    assert Service("nexus").is_running
    #assert Socket("tcp://127.0.0.1:32000").is_listening
    assert Socket("tcp://0.0.0.0:8081").is_listening

# sonar
# service sonar restart
def test_sonar_running(Process, Service, Socket, Command):
    assert Service("sonar").is_enabled
    assert Service("sonar").is_running
    assert Socket("tcp://127.0.0.1:32001").is_listening
    #assert Socket("tcp://0.0.0.0:9000").is_listening

def test_apache2_running(Process, Service, Socket, Command):
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening

def test_apache_validate(Command):
    command = Command('sudo apache2ctl -t')
    assert command.rc == 0

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

def test_nexus_website(Command):
    command = Command('curl -sSfk https://repo.artifact.pl/nexus -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '302'
    assert command.rc == 0

def test_sonar_website(Command):
    command = Command('curl -sSfk https://repo.artifact.pl/sonar -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '302'
    assert command.rc == 0

# na kazdym firewall ufw ufw status

# root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
##
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://127.0.0.1:5433",
"tcp://127.0.0.1:32001",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:8081",
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
