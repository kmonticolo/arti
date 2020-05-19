# centos 7

# userzy grep sh$ /etc/passwd
# root adam dpiekarek oracle hklekowicz kamilm


#def test_ora11g_running(Process, Service, Socket, Command):
    #proc= Process.filter(comm="oracle")
    #assert Socket("tcp://:::32098").is_listening

# startowanie
# [oracle@gemini ~]$ sqlplus '/ as sysdba'
# SQL> startup
# lsnrctl start
# lsnrctl status
def test_lsnrctl_status(Process, Service, Socket, Command):
    command = Command('sudo su - oracle -c "lsnrctl status"')
    assert command.rc == 0

def test_firewalld_unchanged(Command):
    command = Command('sudo md5sum /etc/firewalld/zones/public.xml')
    assert command.stdout.rstrip() == '079967c1db51253a6a39768ad8ace8a8  /etc/firewalld/zones/public.xml'
    assert command.rc == 0

def test_oracle_running(Process, Service, Socket, Command):

    proc= Process.get(comm="tnslsnr")
    assert proc.ppid == 1
    assert proc.user == "oracle"
    assert proc.group == "oinstall"

    assert Socket("tcp://0.0.0.0:1521").is_listening

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.filter(ppid=nginxmaster.pid)
    assert Socket("tcp://0.0.0.0:80").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running

    agent = Process.filter(comm="zabbix_agentd")

    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_tuned_running(Process, Service, Socket, Command):
    assert Service("tuned").is_enabled
    assert Service("tuned").is_running

def test_postfix_running(Process, Service, Socket, Command):
    assert Service("postfix").is_enabled
    assert Service("postfix").is_running

    postfix = Process.get(comm="master")

    assert Socket("tcp://127.0.0.1:25").is_listening

# root@lynx:/home/kamilm# ls /var/spool/cron/crontabs/
# adam  root


#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:25",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:1521",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


