def test_goss(Command):
    command = Command('goss v')
    assert command.rc == 0

def test_ufw_running(Process, Service, Socket, Command):
    assert Service("ufw").is_enabled
    assert Service("ufw").is_running

def test_nginx_running(Process, Service, Socket, Command):
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running

    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening

def test_nginx_validate(Command):
    command = Command('sudo nginx -t')
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_redirect_website(Command):
    command = Command('curl -sSf "http://tbpost.novelpay.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '301' or command.stdout.rstrip() == '302'
    assert command.rc == 0

def test_https_website(Command):
    command = Command('curl -ksSf "https://tbpost.novelpay.pl" -o /dev/null -w %{http_code}')
    assert command.stdout.rstrip() == '200'
    assert command.rc == 0
