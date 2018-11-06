def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == '632a7526b0cb7e7a397b65676f4d92b1  /etc/ufw/user.rules'

    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

    cron = Process.get(comm="cron")
    assert cron.user == "root"
    assert cron.group == "root"

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_wildfly_running(Process, Service, Socket, Command):
    assert Service("wildfly").is_enabled
    assert Service("wildfly").is_running
    assert Socket("tcp://0.0.0.0:8443").is_listening
    assert Socket("tcp://127.0.0.1:9990").is_listening
    assert Socket("tcp://0.0.0.0:8080").is_listening

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

    command = Command('sudo nginx -t')
    assert command.rc == 0


# munin?
