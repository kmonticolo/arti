def test_common_ntp(Command):
    command = Command('ntpstat')
    assert command.rc == 0


