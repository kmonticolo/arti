def test_ntp(Command):
    command = Command('ntpstat')
    assert command.rc == 0

def test_etckeeper_clean(Command):
    command = Command('sudo etckeeper vcs status | grep clean$')
    assert command.rc == 0
