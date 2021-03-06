def test_common_etckeeper_clean(Command):
    command = Command('sudo etckeeper vcs status | grep clean$')
    assert command.rc == 0

def test_common_ufw_default_reject_outgoing(Command, SystemInfo):
    command = Command('which ufw && sudo ufw status verbose|grep "reject (outgoing)"')
    if SystemInfo.type == "debian":
      assert command.rc == 0


