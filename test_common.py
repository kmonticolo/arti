def test_ntp(Command):
    command = Command('ntpstat')
    assert command.rc == 0


