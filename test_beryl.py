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

def test_is_onet_works(Command):
    command = Command('timeout 5 wget onet.pl -o /dev/null')
    assert command.rc != 0

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
    command = Command('sudo ufw status | grep -w "Status: active"')
    assert command.rc == 0

# ssh beryl.artifact.pl sudo md5sum /etc/ufw/user.rules
def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '7033440160ad197b4c5989339adbd61c  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_wildfly_ntms_running(Process, Service, Socket, Command):
    assert Service("wildfly").is_enabled
    assert Service("wildfly").is_running
    assert Socket("tcp://164.132.30.190:4747").is_listening
    #assert Socket("tcp://0.0.0.0:5011").is_listening
    #assert Socket("tcp://164.132.30.190:18181").is_listening
    assert Socket("tcp://0.0.0.0:8080").is_listening
    assert Socket("tcp://0.0.0.0:8080").is_listening
    #assert Socket("tcp://0.0.0.0:5011").is_listening
    assert Socket("tcp://0.0.0.0:8443").is_listening

def test_ntms_cm_ssl_running(Process, Service, Socket, Command):
    assert Service("ntms_cm_ssl").is_enabled

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

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_vibbek_website(Command):
    command = Command('curl -sSfk http://beryl.artifact.pl/#/quick -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_mysql_running(Process, Service, Socket, Command):
    assert Service("mysql").is_enabled

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
"tcp://0.0.0.0:8080",
"tcp://0.0.0.0:80",
#"tcp://0.0.0.0:5011",
"tcp://164.132.30.190:53",
"tcp://127.0.0.1:53",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:5432",
"tcp://127.0.0.1:953",
"tcp://0.0.0.0:8443",
"tcp://0.0.0.0:443",
"tcp://127.0.0.1:32000",
"tcp://0.0.0.0:10050",
#"tcp://164.132.30.190:18181",
"tcp://:::80",
"tcp://:::53",
"tcp://:::22",
"tcp://::1:5432",
    ):
        socket = host.socket(spec)
        assert socket.is_listening
