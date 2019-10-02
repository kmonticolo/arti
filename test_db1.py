#test_agat.py::test_cron_running[paramiko://192.99.119.27] PASSED         [  0%]
#test_taj.py::test_elasticsearch_running[paramiko://192.99.119.27] PASSED [ 89%]
#test_taj.py::test_graylog_service[paramiko://192.99.119.27] PASSED       [ 89%]
#test_beta.py::test_java_running[paramiko://192.99.119.27] PASSED         [ 11%]
#test_lynx.py::test_mongod_running[paramiko://192.99.119.27] PASSED       [ 38%]
#test.py::test_packages[paramiko://192.99.119.27-python-2.7] PASSED       [ 67%]
#test_alpha.py::test_pg_isready_output[paramiko://192.99.119.27] PASSED   [  5%]
#test_agat.py::test_postgres_running[paramiko://192.99.119.27] PASSED     [  1%]
#test_beta.py::test_rsyslogd_running[paramiko://192.99.119.27] PASSED     [ 12%]
#test_agat.py::test_ufw[paramiko://192.99.119.27] PASSED                  [  0%]
#test_agat.py::test_ufw_running[paramiko://192.99.119.27] PASSED          [  1%]
#test_agat.py::test_zabbix_agent_running[paramiko://192.99.119.27] PASSED [  1%]

# trzy testy ufw maja byc zawsze
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'a50bf0c59cd4a5a8b4b325061c669eca  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_elasticsearch_running(Process, Service, Socket, Command):
    assert Service("elasticsearch").is_enabled
    assert Service("elasticsearch").is_running

def test_graylog_service(Process, Service, Socket, Command):
    assert Service("graylog-server").is_enabled
    assert Service("graylog-server").is_running
    java = Process.get(user="graylog",comm="java")

def test_java_running(Process, Service, Socket, Command):
    java = Process.filter(user="vcs", ppid='1', comm="java")

def test_mongod_running(Process, Service, Socket, Command):
    assert Service("mongod").is_enabled
    assert Service("mongod").is_running

    mongod = Process.get(comm="mongod")
    assert mongod.user == "mongodb"
    assert mongod.group == "mongodb"
    assert Socket("tcp://127.0.0.1:27017").is_listening

import pytest

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

def test_pg_isready_output(Command):
    command = Command('/usr/bin/pg_isready')
    assert command.stdout.rstrip() == '/var/run/postgresql:5432 - accepting connections'
    assert command.rc == 0

def test_rsyslogd_running(Process, Service, Socket, Command):
    assert Service("rsyslog").is_enabled
    assert Service("rsyslog").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

