#test_agat.py::test_cron_running[paramiko://192.99.119.26] PASSED         [  0%]
#test_beta.py::test_java_running[paramiko://192.99.119.26] PASSED         [ 11%]
#test.py::test_packages[paramiko://192.99.119.26-python-2.7] PASSED       [ 67%]
#test_beta.py::test_rsyslogd_running[paramiko://192.99.119.26] PASSED     [ 12%]
#test_agat.py::test_ufw[paramiko://192.99.119.26] PASSED                  [  0%]
#test_agat.py::test_ufw_running[paramiko://192.99.119.26] PASSED          [  1%]
#test_agat.py::test_zabbix_agent_running[paramiko://192.99.119.26] PASSED [  1%]

username = "wildfly"

def test_user_exists(host):
    user = host.user("%s" % username)
    assert user.name == "%s" % username
    assert user.group == "%s" % username
    assert user.home == "/home/%s" % username

def test_user_home_exists(host):
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
    assert command.stdout.rstrip() == '744bfcc5e679940f220f92cb7e386401  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_java_running(Process, Service, Socket, Command):
    java = Process.filter(user="vcs", ppid='1', comm="java")

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

@pytest.mark.parametrize("package", [
    ("ntms-application-2.1.3.war")
])

def test_is_package_deployed(host, package):
    pkg = host.run("sudo -u %s /opt/wildfly-15.0.0.Final/bin/jboss-cli.sh -c --controller=127.0.0.1 \"deployment-info --name=%s\"" % (username, package))
    assert pkg.rc == 0

def test_count_java_process(host):
    javas = host.process.filter(user="%s" % username, comm="java", fname="java")
    assert len(javas) == 1

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
    "tcp://0.0.0.0:8443",
    "tcp://0.0.0.0:10050",
    "tcp://127.0.0.1:9990",
        ):
            socket = host.socket(spec)
            assert socket.is_listening
