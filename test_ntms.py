def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_iptables_unchanged(Command):
    command = Command('sudo md5sum /etc/iptables/rules.v4')
    assert command.stdout.rstrip() == '0a2c751e76ad007e734840aeac3a8ac1  /etc/iptables/rules.v4'
    assert command.rc == 0
    command = Command('sudo md5sum /etc/ufw/before.init')
    assert command.stdout.rstrip() == 'cd7783526a1a2b25581cecd3c2daa1a4  /etc/ufw/before.init'
    assert command.rc == 0
    command = Command('sudo md5sum /etc/ufw/before.rules')
    assert command.stdout.rstrip() == '8bbf6ebc0629a35310acc1e5e5bd63cc  /etc/ufw/before.rules'
    assert command.rc == 0
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '5274adde3e45612d12e9818ffc35d7b0  /etc/ufw/user.rules'
    assert command.rc == 0

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening
    assert Socket("tcp://:::80").is_listening
    assert Socket("tcp://:::443").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

# restart ntms, zeby zaczal sluchac na porcie 10000 i 9797
# su - jboss
# cd /opt/ntms/wildfly
# ./bin/start_server 
# tail -F standalone/log/server.log

def test_wildfly_running(Process, Service, Socket, Command):
    standalone = Process.get(user="jboss", comm="standalone.sh")
    assert standalone.user == "jboss"
    assert standalone.group == "jboss"

    wildfly = Process.get(ppid=standalone.pid)
    assert wildfly.user == "jboss"
    assert wildfly.group == "jboss"
    assert wildfly.comm == "java"
    assert Socket("tcp://127.0.0.1:10000").is_listening
    assert Socket("tcp://0.0.0.0:8090").is_listening # backend do apache
    assert Socket("tcp://127.0.0.1:61616").is_listening
    assert Socket("tcp://0.0.0.0:8453").is_listening
    #assert Socket("tcp://0.0.0.0:9797").is_listening # nie slucha - patrz wyzej

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

def test_pg_isready_output(Command):
    command = Command('/usr/bin/pg_isready')
    assert command.stdout.rstrip() == '/var/run/postgresql:5432 - accepting connections'
    assert command.rc == 0

def test_redirect_website(Command):
    command = Command('curl -sSf "http://ntms.novelpay.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '301' or command.stdout.rstrip() == '302'
    assert command.rc == 0

def test_https_website(Command):
    command = Command('curl -ksSf "https://ntms.novelpay.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:10050",
"tcp://0.0.0.0:8453",
"tcp://0.0.0.0:80",
"tcp://127.0.0.1:61616",
"tcp://127.0.0.1:10000",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://0.0.0.0:25",
"tcp://127.0.0.1:5433",
"tcp://0.0.0.0:8090",
"tcp://0.0.0.0:443",
"tcp://:::80",
"tcp://:::22",
"tcp://:::5432",
"tcp://:::25",
):
        socket = host.socket(spec)
        assert socket.is_listening


