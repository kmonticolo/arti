# ubuntu 16.04 lts

# amq	
#  vim /etc/activemq/instances-^Cabled/main/activemq.xml 

# userzy grep sh$ /etc/passwd
# adam root postgres amq activemq kamilm


#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'fd95f57476c37af464be9097c074d86b  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://127.0.0.1:5432").is_listening

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

def test_activemq_running(Process, Service, Socket, Command):
    assert Service("activemq").is_enabled
    assert Service("activemq").is_running
    amq = Process.get(comm="java",ppid='1', user="root")
    assert amq.user == "root"
    assert amq.group == "root"
    assert Socket("tcp://0.0.0.0:8161").is_listening
    assert Socket("tcp://0.0.0.0:1099").is_listening
    assert Socket("tcp://0.0.0.0:61613").is_listening
    assert Socket("tcp://0.0.0.0:61616").is_listening
    assert Socket("tcp://0.0.0.0:61617").is_listening


def test_wildfly_running(Process, Service, Socket, Command):
    assert Service("wildfly").is_enabled
    assert Service("wildfly").is_running
    amq = Process.get(comm="java", user="art")
    assert amq.user == "art"
    assert amq.group == "art"
    assert Socket("tcp://0.0.0.0:8080").is_listening
    assert Socket("tcp://0.0.0.0:8443").is_listening
    assert Socket("tcp://127.0.0.1:9990").is_listening

# systemctl list-unit-files | grep enabled
#
#root@lynx:/home/kamilm# systemctl list-unit-files | grep enabled
#
#systemctl list-units --type=service --state=active

#haproxy.service
#activemq.service

# root@lynx:/home/kamilm# ls /var/spool/cron/crontabs/
# brak

# na kazdym firewall ufw ufw status

# root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
## netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:5432",
"tcp://127.0.0.1:5433",
"tcp://0.0.0.0:8161",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:1099",
"tcp://0.0.0.0:61613",
"tcp://0.0.0.0:61616",
"tcp://0.0.0.0:61617",
"tcp://:::22",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening

