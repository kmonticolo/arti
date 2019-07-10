# ubuntu 16.04 lts

# userzy grep sh$ /etc/passwd
# root postgres adam jboss fecru kamilm

#ufw
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '383db7356044db123fc069d0b40a5b23  /etc/ufw/user.rules'
    assert command.rc == 0

def test_jira_website(Command):
    command = Command('curl -sSf https://jira.artifact.pl -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_confluence_website(Command):
    command = Command('curl -sSf "https://confluence.artifact.pl/login.action?os_destination=%2Findex.action&permissionViolation=true" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_demo_website(Command):
    command = Command('curl -sSf "https://demo.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_topaz_website(Command):
    command = Command('curl -sSf "http://topaz.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_vtms_website(Command):
    command = Command('curl -sSf "https://vtms.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_vtms1_website(Command):
    command = Command('curl -sSf "https://vtms1.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_vtms2_website(Command):
    command = Command('curl -sSf "https://vtms2.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_fisheye_website(Command):
    command = Command('curl -sSf "https://fisheye.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_pst_http_website(Command):
    command = Command('curl -sSf "http://pst.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_pst_https_website(Command):
    command = Command('curl -sSf "https://pst.artifact.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '302'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

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

def test_mysql_running(Process, Service, Socket, Command):
    assert Service("mysql").is_enabled
    mysql = Process.get(comm="mysqld_safe")
    assert mysql.user == "root"
    assert mysql.group == "root"
    assert Socket("tcp://127.0.0.1:3306").is_listening


def test_apache_validate(Command):
    command = Command('sudo apache2ctl -t')
    assert command.rc == 0

def test_fisheye_running(Process, Service, Socket, Command):
    assert Service("fisheye").is_enabled
    assert Service("fisheye").is_running

def test_jira_running(Process, Service, Socket, Command):
    assert Service("jira").is_enabled
    assert Service("jira").is_running
    jira = Process.get(user="jira", comm="java")
    assert jira.user == "jira"
    assert jira.group == "jira"
    assert Socket("tcp://0.0.0.0:9090").is_listening
    assert Socket("tcp://0.0.0.0:9095").is_listening

def test_confluence_running(Process, Service, Socket, Command):
    assert Service("confluence").is_enabled
    assert Service("confluence").is_running
    assert Socket("tcp://0.0.0.0:8090").is_listening

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_haproxy_running(Process, Service, Socket, Command):
    assert Service("haproxy").is_enabled
    assert Service("haproxy").is_running
    assert Socket("tcp://0.0.0.0:9084").is_listening
    assert Socket("tcp://0.0.0.0:9085").is_listening

def test_haproxy_config_test(Command):
    command = Command('sudo haproxy -c -V -f /etc/haproxy/haproxy.cfg')
    assert command.rc == 0

def test_haproxy_conf(host):
    conf = host.file("/etc/haproxy/haproxy.cfg")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.mode == 0o644
    assert conf.contains("bind \*:9085")
    assert conf.contains("bind \*:9084")


def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:5432",
"tcp://127.0.0.1:5433",
"tcp://0.0.0.0:9084",
"tcp://0.0.0.0:9085",
"tcp://0.0.0.0:10050",
"tcp://127.0.0.1:3306",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://0.0.0.0:8090",
"tcp://0.0.0.0:443",
"tcp://0.0.0.0:9090",
"tcp://0.0.0.0:9095",
"tcp://0.0.0.0:80",
    ):
        socket = host.socket(spec)
        assert socket.is_listening
