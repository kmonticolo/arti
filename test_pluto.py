# centos 7



def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running

    agent = Process.filter(comm="zabbix_agentd")

    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_tuned_running(Process, Service, Socket, Command):
    assert Service("tuned").is_enabled
    assert Service("tuned").is_running


# root@lynx:/home/kamilm# ls /var/spool/cron/crontabs/
# adam  root


def test_firewalld_running(Process, Service, Socket, Command):
    assert Service("firewalld").is_enabled
    assert Service("firewalld").is_running

def test_firewalld_unchanged(Command):
    command = Command('sudo md5sum /etc/firewalld/zones/public.xml')
    assert command.stdout.rstrip() == 'c7a4a2d019e158b8240600acfbebae1e  /etc/firewalld/zones/public.xml'
    assert command.rc == 0

def test_kafka_config_unchanged(Command):
    command = Command('sudo md5sum  /opt/kafka/config/server.properties')
    assert command.stdout.rstrip() == '1e0468624d1e8e22e6ac0d35b16e57c5  /etc/ufw/user.rules'

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

def test_crond_running(Process, Service, Socket, Command):
    assert Service("crond").is_enabled
    assert Service("crond").is_running

def test_java_running(Process, Service, Socket, Command):
    java = Process.filter(comm="java")
    assert Socket("tcp://0.0.0.0:8080").is_listening

def test_httpd_running(Process, Service, Socket, Command):
    assert Service("httpd").is_enabled
    assert Service("httpd").is_running
    assert Socket("tcp://0.0.0.0:80").is_listening

def test_wildfly_running(Process, Service, Socket, Command):
    assert Service("wildfly").is_enabled
    assert Service("wildfly").is_running
    assert Socket("tcp://0.0.0.0:8080").is_listening

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://127.0.0.1:5432").is_listening
    assert Socket("tcp://::1:5432").is_listening

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:2181",
"tcp://0.0.0.0:8080",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:45848",
"tcp://0.0.0.0:5432",
"tcp://0.0.0.0:8443",
"tcp://0.0.0.0:3777",
"tcp://0.0.0.0:10050",
"tcp://:::22",
"tcp://:::5432",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


