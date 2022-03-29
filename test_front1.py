def test_ufw(Command):
    command = Command('sudo ufw status | grep -w "Status: active"')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '922eb5acf1ba758cafcb06cce4bb6e8b  /etc/ufw/user.rules'
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

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.filter(ppid=nginxmaster.pid)
    assert Socket("tcp://0.0.0.0:443").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_nginx_conf(host):
    conf = host.file("/etc/nginx/sites-enabled/ntms")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.contains("server_name ntms.novelpay.pl")
    assert conf.contains("proxy_pass http://192.99.119.26:8080/ntmss")
    assert conf.contains("ssl_certificate_key /etc/nginx/ssl/novelpay.key")
    assert conf.contains("ssl_certificate.*/etc/nginx/ssl/novelpay.pem")

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

# netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:8453",
"tcp://0.0.0.0:35621",
"tcp://0.0.0.0:35623",
"tcp://0.0.0.0:8080",
"tcp://127.0.0.53:53",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:8443",
"tcp://0.0.0.0:443",
"tcp://0.0.0.0:4832",
"tcp://0.0.0.0:10050",
"tcp://:::35621",
"tcp://:::35623",
"tcp://:::443",
"tcp://:::10050",
    ):
        socket = host.socket(spec)
        assert socket.is_listening


