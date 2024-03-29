# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
##
#root:x:0:0:root:/root:/bin/bash
#adam:x:1000:1000:adam,,,:/home/adam:/bin/bash
#jenkins:x:112:118:Jenkins,,,:/var/lib/jenkins:/bin/bash
#postgres:x:114:122:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
#kamilm:x:1001:1001:Kamil M,,,:/home/kamilm:/bin/bash
#

#def test_is_onet_reachable(Command):
    #command = Command('timeout 5 wget onet.pl -o /dev/null')
    #assert command.rc != 0

#ufw
import pytest
username="jboss"
def test_ufw(Command):
    command = Command('sudo ufw status | grep -w "Status: active"')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'a4833e2dce1a42a7a5ce15ae8cf585c7  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_java_running(Process, Service, Socket, Command):
    java = Process.filter(comm="java")
    assert Socket("tcp://0.0.0.0:8080").is_listening
    assert Socket("tcp://0.0.0.0:8443").is_listening

#@pytest.mark.parametrize("package", [
#    ("ppos-application-0.9.1-SNAPSHOT.war")
#])

#def test_is_package_deployed(host, package):
#    pkg = host.run("sudo -u %s /opt/ppos/wildfly-10.1.0.Final/bin/jboss-cli.sh -c --controller=127.0.0.1  \"deployment-info --name=%s\" | grep %s | awk '{print $NF}'" % (username, package, package))
#    assert pkg.stdout.rstrip() == 'OK'
#    assert pkg.rc == 0

#def test_count_java_process(host):
#    javas = host.process.filter(user="%s" % username, comm="java", fname="java")
#    assert len(javas) == 1

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

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.filter(user="root", ppid='1', comm="nginx")
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

# netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:8080",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://0.0.0.0:8443",
"tcp://0.0.0.0:443",
"tcp://0.0.0.0:10050",
    ):
        socket = host.socket(spec)
        assert socket.is_listening


##procesy
#root@beryl:/home/kamilm# netstat -alnp|grep LIST|head -20
