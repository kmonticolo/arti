
def test_user_exists(host):
    for username in ("wildfly","docker-data","adam","kamil","mratkiewicz"):
        user = host.user("%s" % username)
        assert user.name == "%s" % username
        assert user.group == "%s" % username
        assert user.home == "/home/%s" % username

def test_user_home_exists(host):
    for username in ("wildfly","docker-data","adam","kamil","mratkiewicz"):
        user_home = host.file("/home/%s" % username)
        assert user_home.exists
        assert user_home.is_directory

def test_ufw(Command):
    command = Command('sudo ufw status | grep -w "Status: active"')
    assert command.rc == 0

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'ff4d62d28f5df5d9fd9033c69cb6e98b  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_docker_names(Command):
    command = Command('sudo docker ps --format \'{{.Names}}\'')
    assert command.stdout.rstrip() == 'ntms-nginx\nntms-wildfly'
    assert command.rc == 0

def test_docker_images(Command):
    command = Command('sudo docker ps --format \'{{.Image}}\' |awk -F: \'{print $2}\'')
    assert command.stdout.rstrip() == '2.2.1.5237\n2.2.1.5237'
    assert command.rc == 0

import pytest

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

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

## netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'
def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
    "tcp://0.0.0.0:8080",
    "tcp://127.0.0.53:53",
    "tcp://0.0.0.0:22",
    "tcp://0.0.0.0:10050",
    "tcp://0.0.0.0:8787",
    "tcp://0.0.0.0:9090",
    "tcp://0.0.0.0:9990",
    "tcp://0.0.0.0:9993",
        ):
            socket = host.socket(spec)
            assert socket.is_listening
