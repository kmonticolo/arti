import pytest
username="jboss"

#def test_ufw(Command):
#    command = Command('sudo ufw status | grep -w "Status: active"')
#    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'ef61846d27fac046be14b8c97353b91b  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running
    postgres = Process.filter(comm="postgres")
    assert Socket("tcp://0.0.0.0:5432").is_listening

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_pg_isready_output(Command):
    command = Command('/usr/bin/pg_isready')
    assert command.stdout.rstrip() == '/var/run/postgresql:5432 - accepting connections'
    assert command.rc == 0

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    nginxmaster = Process.get(user="root", ppid='1', comm="nginx")
    assert nginxmaster.user == "root"
    assert nginxmaster.group == "root"

    nginxworker = Process.filter(ppid=nginxmaster.pid)
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:444").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_ntmsqa_website(Command):
    command = Command('curl -sSfk https://qantms.novelpay.pl:444 -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_java_running(Process, Service, Socket, Command):
    java = Process.filter(user="vcs", ppid='1', comm="java")

@pytest.mark.parametrize("name,version", [
    ("python", "2.7"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)

def test_rsyslogd_running(Process, Service, Socket, Command):
    assert Service("rsyslog").is_enabled
    assert Service("rsyslog").is_running

def test_postfix_running(Process, Service, Socket, Command):
    assert Service("postfix").is_enabled
    assert Service("postfix").is_running
    postfix = Process.get(comm="master")
    assert Socket("tcp://0.0.0.0:25").is_listening

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:25",
"tcp://0.0.0.0:444",
"tcp://0.0.0.0:8161",
"tcp://0.0.0.0:9090",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:35621",
"tcp://0.0.0.0:9990",
"tcp://0.0.0.0:35623",
"tcp://0.0.0.0:9993",
"tcp://0.0.0.0:4747",
"tcp://0.0.0.0:61613",
"tcp://0.0.0.0:61616",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:8081",
"tcp://0.0.0.0:8787",
"tcp://127.0.0.53:53",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
    ):
        socket = host.socket(spec)
        assert socket.is_listening
