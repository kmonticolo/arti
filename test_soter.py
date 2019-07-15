def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '7074f53e4300206a5759336abc757b91  /etc/ufw/user.rules'
    assert command.rc == 0

def test_fwstart_unchanged(Command):
    command = Command('sudo md5sum /root/fwstart.sh')
    assert command.stdout.rstrip() == 'cd6f7d0e2419601180f40c1cd8b2efe1  /root/fwstart.sh'
    assert command.rc == 0

def test_apache2_running(Process, Service, Socket, Command):
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening

def test_apache_validate(Command):
    command = Command('sudo apache2ctl -t')
    assert command.rc == 0

#def test_certbot_dry_run(Command):
#    command = Command('sudo certbot --dry-run renew')
#    assert command.rc == 0

def test_soter_website(Command):
    command = Command('curl -sSf "https://soter.novelpay.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '301' or command.stdout.rstrip() == '302'
    assert command.rc == 0

def test_confluence_website(Command):
    command = Command('curl -sSf "https://soter.novelpay.pl:8070/login.action" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_jira_website(Command):
    command = Command('curl -sSf "https://jira.novelpay.pl/secure/Dashboard.jspa" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

#  su - fisheye -s /bin/bash
# cd fecru/bin/
# ./stop.sh; ./start.sh
def test_crucible_website(Command):
    command = Command('curl -sSf "https://cr.novelpay.pl/browse" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_timesheet_website(Command):
    command = Command('curl -sSf "https://timesheet.novelpay.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200' or command.stdout.rstrip() == '301'
    assert command.rc == 0

def test_redmine_website(Command):
    command = Command('curl -sSf "https://redmine.novelpay.pl/login" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_mysql_running(Process, Service, Socket, Command):
    assert Service("mysql").is_enabled
    assert Service("mysql").is_running

    mysql = Process.get(comm="mysqld")
    assert mysql.user == "mysql"
    assert mysql.group == "mysql"

    assert Socket("tcp://127.0.0.1:3306").is_listening

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running


def test_prosody_running(Process, Service, Socket, Command):
    assert Service("prosody").is_enabled
    assert Service("prosody").is_running
    lua = Process.get(comm="lua5.1")
    assert lua.user == "prosody"
    assert lua.group == "prosody"
    assert Socket("tcp://0.0.0.0:5322").is_listening
    assert Socket("tcp://0.0.0.0:5223").is_listening
    assert Socket("tcp://0.0.0.0:5224").is_listening 
    assert Socket("tcp://0.0.0.0:5000").is_listening

def test_lmgrd_running(Process, Service, Socket, Command):
    lmgrd = Process.get(comm="lmgrd")
    assert lmgrd.user == "flexlm"
    assert lmgrd.group == "flexlm"
    assert Socket("tcp://0.0.0.0:8224").is_listening

def test_armlmd_running(Process, Service, Socket, Command):
    armlmd = Process.get(comm="lmgrd")
    assert armlmd.user == "flexlm"
    assert armlmd.group == "flexlm"
    assert Socket("tcp://0.0.0.0:27010").is_listening

#def test_pinpadlogserver_running(Process, Service, Socket, Command):
    #assert Socket("tcp://:::61234").is_listening

def test_slapd_running(Process, Service, Socket, Command):
    slapd= Process.get(comm="slapd")
    assert slapd.user == "openldap"
    assert slapd.group == "openldap"
    assert Socket("tcp://0.0.0.0:389").is_listening


def test_jira_running(Process, Service, Socket, Command):
    assert Service("jira").is_enabled
    assert Service("jira").is_running
    jira = Process.get(user="jira1", comm="java")
    assert jira.user == "jira1"
    assert jira.group == "jira1"
    assert Socket("tcp://0.0.0.0:8080").is_listening

def test_catalina_policy_unchanged(Command):
    command = Command('sudo md5sum /opt/atlassian/jira/conf/catalina.policy')
    assert command.stdout.rstrip() == '0cfebc3134731e42cc02b75047c366a0  /opt/atlassian/jira/conf/catalina.policy'
    assert command.rc == 0

def test_jira_catalina_properties_unchanged(Command):
    command = Command('sudo md5sum /opt/atlassian/jira/conf/catalina.properties')
    assert command.stdout.rstrip() == '938494616bf21094f21ec663d242045f  /opt/atlassian/jira/conf/catalina.properties'
    assert command.rc == 0

def test_jira_context_xml_unchanged(Command):
    command = Command('sudo md5sum /opt/atlassian/jira/conf/context.xml')
    assert command.stdout.rstrip() == '61b5ffcad3f105f035aca33ca811b516  /opt/atlassian/jira/conf/context.xml'
    assert command.rc == 0

def test_jira_jaspic_providers_unchanged(Command):
    command = Command('sudo md5sum /opt/atlassian/jira/conf/jaspic-providers.xml')
    assert command.stdout.rstrip() == '4f5cc55cca2c4e5dc19cf9ea7ba8e76d  /opt/atlassian/jira/conf/jaspic-providers.xml'
    assert command.rc == 0

def test_jira_server_xml_unchanged(Command):
    command = Command('sudo md5sum /opt/atlassian/jira/conf/server.xml')
    assert command.stdout.rstrip() == '52a7cdcaad8217dfbffeaa11d1366ff9  /opt/atlassian/jira/conf/server.xml'
    assert command.rc == 0

def test_jira_tomcat_users_xml_unchanged(Command):
    command = Command('sudo md5sum /opt/atlassian/jira/conf/tomcat-users.xml')
    assert command.stdout.rstrip() == 'd995b7238e99826cbfa1476ed9e18265  /opt/atlassian/jira/conf/tomcat-users.xml'
    assert command.rc == 0

def test_jira_web_xml_unchanged(Command):
    command = Command('sudo md5sum /opt/atlassian/jira/conf/web.xml')
    assert command.stdout.rstrip() == '24ba95d91330d1f547c8c602bf91873d  /opt/atlassian/jira/conf/web.xml'
    assert command.rc == 0

def test_confluence_running(Process, Service, Socket, Command):
    assert Service("confluence").is_enabled
    assert Service("confluence").is_running
    #conflu = Process.get(user="confluence", comm="java")
    #assert conflu.user == "confluence"
    #assert conflu.group == "confluence"
    #assert Socket("tcp://:::8087").is_listening
    #assert Socket("tcp://127.0.0.1:8000").is_listening

def test_exim_running(Process, Service, Socket, Command):
    assert Service("exim4").is_enabled
    assert Service("exim4").is_running
    assert Socket("tcp://127.0.0.1:25").is_listening

def test_apache2_running(Process, Service, Socket, Command):
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening
    assert Socket("tcp://0.0.0.0:8061").is_listening
    assert Socket("tcp://0.0.0.0:8005").is_listening
    assert Socket("tcp://0.0.0.0:8070").is_listening
    assert Socket("tcp://0.0.0.0:9000").is_listening

def test_ejabberd_running(Process, Service, Socket, Command):
    #assert Service("jabberd").is_enabled
    #assert Service("jabberd").is_running
    assert Socket("tcp://0.0.0.0:4369").is_listening



def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://127.0.0.1:3306",
"tcp://0.0.0.0:5322",
"tcp://0.0.0.0:4369",
"tcp://0.0.0.0:5269",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:7000",
"tcp://127.0.0.1:25",
"tcp://0.0.0.0:5280",
"tcp://0.0.0.0:8224",
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:27010",
"tcp://0.0.0.0:389",
"tcp://0.0.0.0:5222",
"tcp://0.0.0.0:5223",
"tcp://0.0.0.0:5224",
"tcp://0.0.0.0:5000",
"tcp://0.0.0.0:5322",
"tcp://0.0.0.0:8080",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:4369",
#"tcp://:::61234",
"tcp://0.0.0.0:8060",
"tcp://0.0.0.0:8061",
"tcp://0.0.0.0:389",
"tcp://0.0.0.0:8005",
"tcp://0.0.0.0:8070",
"tcp://0.0.0.0:8007",
"tcp://0.0.0.0:5223",
"tcp://0.0.0.0:5224",
"tcp://0.0.0.0:9000",
"tcp://0.0.0.0:5000",

    ):  
        socket = host.socket(spec)
        assert socket.is_listening
