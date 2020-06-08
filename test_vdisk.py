import pytest

def test_apache2_running(Process, Service, Socket, Command):
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running
    assert Socket("tcp://:::80").is_listening

def test_apache_validate(Command):
    command = Command('sudo apache2ctl -t')
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

def test_java_running(Process, Service, Socket, Command):
    java = Process.filter(user="vcs", ppid='1', comm="java")

@pytest.mark.parametrize("name,version", [
    ("python", "2.7"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://127.0.0.1:5432").is_listening
    assert Socket("tcp://::1:5432").is_listening

def test_rsyslogd_running(Process, Service, Socket, Command):
    assert Service("rsyslog").is_enabled
    assert Service("rsyslog").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://127.0.0.1:53",
"tcp://0.0.0.0:22",
"tcp://127.0.0.1:5432",
"tcp://127.0.0.1:953",
"tcp://127.0.0.1:5433",
"tcp://127.0.0.1:25",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:35621",
"tcp://0.0.0.0:8069",
"tcp://0.0.0.0:35623",
"tcp://127.0.0.1:3306",
"tcp://:::80",
"tcp://::1:53",
"tcp://:::22",
"tcp://::1:953",
"tcp://::1:25",
"tcp://:::443",
"tcp://:::10050",
"tcp://:::35621",
"tcp://:::35623",
    ):
        socket = host.socket(spec)
        assert socket.is_listening
