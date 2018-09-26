# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
##
#root:x:0:0:root:/root:/bin/bash
#adam:x:1000:1000:adam,,,:/home/adam:/bin/bash
#postgres:x:112:119:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
#works:x:1001:1001:,,,:/home/works:/bin/bash
#mmursztyn:x:1002:1002:,,,:/home/mmursztyn:/bin/bash
#kamilm:x:1003:1003:Kamil M,,,:/home/kamilm:/bin/bash
#
#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '058342183529fff3e8ee13840c14e59e  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

    cron = Process.get(comm="cron")
    assert cron.user == "root"
    assert cron.group == "root"

def test_mongod_running(Process, Service, Socket, Command):
    assert Service("mongodb").is_enabled
    assert Service("mongodb").is_running

    mongod = Process.get(comm="mongod")
    assert mongod.user == "mongodb"
    assert mongod.group == "nogroup"
    assert Socket("tcp://127.0.0.1:27017").is_listening

def test_java_running(Process, Service, Socket, Command):
    java = Process.filter(comm="java")
    assert Socket("tcp://:::8080").is_listening
    assert Socket("tcp://:::8180").is_listening

def test_haproxy_running(Process, Service, Socket, Command):
    assert Service("haproxy").is_enabled
    assert Service("haproxy").is_running

def test_haproxy_config_test(Command):
    command = Command('sudo haproxy -c -V -f /etc/haproxy/haproxy.cfg')
    assert command.rc == 0

def test_haproxy_conf(host):
    conf = host.file("/etc/haproxy/haproxy.cfg")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.mode == 0o644
    assert conf.contains("stats socket /run/haproxy/admin.sock mode 660 level admin")
    assert conf.contains("ssl-default-bind-ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS")
    assert conf.contains("server s1 127.0.0.1:81 maxconn 32 check inter 1000 fall 5")
    assert conf.contains("server s2 127.0.0.1:82 maxconn 32 check backup")

def test_tomcat7_running(Process, Service, Socket, Command):
    assert Service("tomcat7").is_enabled
    assert Service("tomcat7").is_running
    assert Socket("tcp://:::8180").is_listening

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

# systemctl list-unit-files | grep enabled
#
#root@lynx:/home/kamilm# systemctl list-unit-files | grep enabled



#root@spinel:/home/kamilm#  ls /var/spool/cron/crontabs/


# na kazdym firewall ufw ufw status

# root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
# netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'

##
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://127.0.0.1:27017",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://0.0.0.0:10050",
"tcp://:::8080",
"tcp://:::8180",
"tcp://:::4949",
"tcp://:::22",
"tcp://:::5432",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


##procesy
#root@beryl:/home/kamilm# netstat -alnp|grep LIST|head -20
