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
    assert command.stdout.rstrip() == '632a06aa019c430c0f394ee4cd4f54fd  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_mongod_running(Process, Service, Socket, Command):
    assert Service("mongod").is_enabled
    assert Service("mongod").is_running

    mongod = Process.get(comm="mongod")
    assert mongod.user == "mongodb"
    assert mongod.group == "mongodb"
    assert Socket("tcp://127.0.0.1:27017").is_listening

def test_graylog_service(Process, Service, Socket, Command):
    assert Service("graylog-server").is_enabled
    assert Service("graylog-server").is_running
    java = Process.get(user="graylog",comm="java")

def test_elasticsearch_running(Process, Service, Socket, Command):
    assert Service("elasticsearch").is_enabled
    assert Service("elasticsearch").is_running

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
