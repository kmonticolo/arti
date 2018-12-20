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
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

# ssh draco.artifact.pl sudo md5sum /etc/ufw/user.rules
def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'f195fbcf83b132092bbec30f573375f9  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_java_running(Process, Service, Socket, Command):
    java = Process.filter(comm="java")

def test_jenkins_running(Process, Service, Socket, Command):
    assert Service("jenkins").is_enabled
    assert Service("jenkins").is_running
    assert Socket("tcp://:::9090").is_listening

def test_jenkins_website(Command):
    command = Command('curl -sSf "https://draco.artifact.pl/jenkins/" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '403'
    assert command.rc == 22

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

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.filter(ppid=nginxmaster.pid)
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening
    assert Socket("tcp://:::80").is_listening
    assert Socket("tcp://:::443").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_nginx_conf(host):
    conf = host.file("/etc/nginx/sites-enabled/draco")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.contains("server_name draco.artifact.pl")
    assert conf.contains("ssl_certificate_key /etc/nginx/ssl/artifact.key")
    assert conf.contains("ssl_certificate.*/etc/nginx/ssl/artifact.pem")
    assert conf.contains("proxy_pass http://localhost:9090/jenkins")

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
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:5432",
"tcp://0.0.0.0:25",
"tcp://0.0.0.0:443",
"tcp://0.0.0.0:10050",
"tcp://:::80",
"tcp://:::4949",
"tcp://:::22",
"tcp://::1:5432",
"tcp://:::25",
"tcp://:::9090",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


##procesy
#root@beryl:/home/kamilm# netstat -alnp|grep LIST|head -21
