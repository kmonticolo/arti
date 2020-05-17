# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
#root postgres adam mlickiewicz art kamilm


#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '494062b59dc7e2845b65c472df9f9cb1  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_squid_running(Process, Service, Socket, Command):
    assert Service("squid").is_enabled
    assert Service("squid").is_running

    squidmaster = Process.get(user="root", ppid='1', comm="squid")
    assert squidmaster.user == "root"
    assert squidmaster.group == "proxy"

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.get(ppid=nginxmaster.pid)
    assert nginxworker.user == "www-data"
    assert nginxworker.group == "www-data"
    assert nginxworker.comm == "nginx"
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0


def test_website(Command):
    command = Command('curl -sSfk http://diament.artifact.pl -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
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

## root@lynx:/home/kamilm# netstat -alnp|grep LIST|head -20
## netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:443",
"tcp://0.0.0.0:2049",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:111",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:22",
"tcp://:::2049",
"tcp://:::111",
"tcp://:::80",
"tcp://:::22"
    ):
        socket = host.socket(spec)
        assert socket.is_listening
