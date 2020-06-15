# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
##
#root:x:0:0:root:/root:/bin/bash
#adam:x:1000:1000:adam,,,:/home/adam:/bin/bash
#jenkins:x:112:118:Jenkins,,,:/var/lib/jenkins:/bin/bash
#postgres:x:114:122:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
#kamilm:x:1001:1001:Kamil M,,,:/home/kamilm:/bin/bash
#

#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -w "Status: active"')
    assert command.rc == 0

# ssh draco.artifact.pl sudo md5sum /etc/ufw/user.rules
def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'c63358cce2962d4062638ebe6dfd4692  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_zookeeper_running(Process, Service, Socket, Command):
    assert Service("zookeeper").is_enabled
    assert Service("zookeeper").is_running

def test_zookeeper_conf_unchanged(Command):
    command = Command('sudo md5sum /opt/zookeeper/conf/zoo.cfg')
    assert command.stdout.rstrip() == '9881e316b8148213a089953c408b91e2  /opt/zookeeper/conf/zoo.cfg'
    assert command.rc == 0

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.filter(ppid=nginxmaster.pid)
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running
