# https://alpha.novelpay.pl/ntms-rel/descriptor.xml
def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '778f6aa7c0088363f73f50daa9dc6aba  /etc/ufw/user.rules'
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_ntms_rel_website(Command):
    command = Command('curl -sSfk https://alpha.novelpay.pl/ntms-rel/descriptor.xml -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_ntms_app_website(Command):
    command = Command('curl -sSfk https://alpha.novelpay.pl -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_PPOS_website(Command):
    command = Command('curl -sSfk https://alpha.novelpay.pl/PPOS -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '302'
    assert command.rc == 0

def test_ntms_website(Command):
    command = Command('curl -sSfk https://alpha.novelpay.pl/ntms -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '301'
    assert command.rc == 0

def test_ntmss_website(Command):
    command = Command('curl -sSfk https://alpha.novelpay.pl/ntmss -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '302'
    assert command.rc == 0

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

# su - jboss; cd ~/jboss-eap-6.4$ ./bin/start_tms.sh
def test_jboss_running(Process, Service, Socket, Command):
    jbossstandalone = Process.get(user="jboss", ppid='1', comm="standalone.sh")
    assert jbossstandalone.user == "jboss"
    assert jbossstandalone.group == "jboss"

    jboss = Process.get(ppid=jbossstandalone.pid)
    assert jboss.user == "jboss"
    assert jboss.group == "jboss"
    assert jboss.comm == "java"
    assert Socket("tcp://127.0.0.1:9990").is_listening
    assert Socket("tcp://127.0.0.1:9999").is_listening
    assert Socket("tcp://0.0.0.0:8080").is_listening
    assert Socket("tcp://0.0.0.0:8787").is_listening
    assert Socket("tcp://0.0.0.0:8443").is_listening
    assert Socket("tcp://0.0.0.0:4447").is_listening

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://0.0.0.0:5432").is_listening

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

    nginxworker = Process.get(ppid=nginxmaster.pid)
    assert nginxworker.user == "www-data"
    assert nginxworker.group == "www-data"
    assert nginxworker.comm == "nginx"
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

