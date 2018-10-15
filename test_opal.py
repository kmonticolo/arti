def test_ufw(Command):
    command = Command('sudo ufw status | grep -qw active')
    assert command.rc == 0

def test_ufw_unchanged(Command):
    command = Command('sudo md5sum /etc/ufw/user.rules')
    assert command.stdout.rstrip() == 'a3fbaef910466dcc137f9037106c78f7  /etc/ufw/user.rules'

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


