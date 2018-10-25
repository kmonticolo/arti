# listener
# export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe
# -bash-4.2$ $ORACLE_HOME/bin/lsnrctl start

def test_firewalld_running(Process, Service, Socket, Command):
    assert Service("firewalld").is_enabled
    assert Service("firewalld").is_running

def test_firewalld_unchanged(Command):
    command = Command('sudo md5sum /etc/firewalld/zones/public.xml')
    assert command.stdout.rstrip() == '616d56b2cd4eb85a77423bc0ff35da4c  /etc/firewalld/zones/public.xml'
    assert command.rc == 0

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

def test_oracle_running(Process, Service, Socket, Command):
    assert Service("oracle-xe").is_enabled
    assert Service("oracle-xe").is_running
    assert Socket("tcp://46.105.232.0:1521").is_listening

def test_tnslsnr_running(Process, Service, Socket, Command):
    proc= Process.get(comm="tnslsnr")
    assert proc.user == "oracle"
    assert proc.group == "dba"
    assert Socket("tcp://46.105.232.0:1521").is_listening
    assert Socket("tcp://0.0.0.0:8080").is_listening

def test_crond_running(Process, Service, Socket, Command):
    assert Service("crond").is_enabled
    assert Service("crond").is_running

def test_chronyd_running(Process, Service, Socket, Command):
    assert Service("chronyd").is_enabled
    assert Service("chronyd").is_running

def test_java_running(Process, Service, Socket, Command):
    cron = Process.filter(comm="java")

def test_munin_running(Process, Service, Socket, Command):
    assert Service("munin-node").is_enabled
    assert Service("munin-node").is_running


def test_postfix_running(Process, Service, Socket, Command):
    assert Service("postfix").is_enabled
    assert Service("postfix").is_running

    postfix = Process.get(comm="master")

    assert Socket("tcp://127.0.0.1:25").is_listening
#

def test_testlot_website(Command):
    command = Command('curl -s https://testlot.novelpay.pl |grep "Lot POS"')
    assert command.rc == 0


def test_tuned_running(Process, Service, Socket, Command):
    assert Service("tuned").is_enabled
    assert Service("tuned").is_running


def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening


def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:4949",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:25",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:8080",
    ):  
        socket = host.socket(spec)
        assert socket.is_listening


