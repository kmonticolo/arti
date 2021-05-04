def repo = 'https://github.com/kmonticolo/arti.git'
def sshconfig='./ssh_config'
def user='kmonti'

for (host in [
  'vdisk',
  'ppos2']) {
  job("testinfra ${host}") {
     logRotator {
        numToKeep(100)
    }
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
    triggers {
        cron('H * * * *')
    }
    steps {
      shell("mkdir -p target/test-reports/")
      shell("sudo -u  ${user} /bin/py.test test_${host}.py test_${host}_active.py test_${host}_serv.py test_common.py test_ntp.py --ssh-config=${sshconfig} --hosts ${host}.novelpay.pl --junit-xml /tmp/junit_${host}.xml")
    }
    }
}
}

for (host in [
  //'diament',
  //'rubin',
  //'topaz',
  //'szmaragd',
  //'opal',
  //'beryl',
  'draco',
  'hydra',
  'luna',
  'lynx',
  'orion',
  'pavo',
  'taurus',
  //'spinel',
  //'fantazja',
  'jerom',
  'taj',
  'piskra',
  'miki',
  'gemini' ]) {
  job("testinfra ${host}") {
    logRotator {
        numToKeep(100)
    }
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
    triggers {
        cron('H * * * *')
    }
     steps {
      shell("mkdir -p target/test-reports/")
      shell("sudo -u  ${user} /bin/py.test test_${host}.py test_${host}_active.py test_${host}_serv.py test_common.py --ssh-config=${sshconfig} --hosts ${host}.artifact.pl --junit-xml /tmp/junit_${host}.xml")
    }
    }
}
}

 job("ansible is reboot needed") {
    logRotator {
        numToKeep(100)
    }
  triggers {
        cron('H 22 * * *')
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/reboot_needed.yml -i /home/kmonti/ansible/inventory -l artifactubuntu,novelpayubuntu")
     }
 }

 job("ansible NPNTMS is reboot needed") {
    logRotator {
        numToKeep(100)
    }
  triggers {
        cron('H 12 * * *')
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/reboot_needed.yml -i /home/kmonti/ansible/inventory -l npntms")
     }
 }

 job("ansible Centos is reboot needed") {
    logRotator {
        numToKeep(100)
    }
  triggers {
        cron('H 12 * * *')
    }
     steps {
        shell("sudo -u kmonti ansible -m shell -a \"needs-restarting -r|grep 'not necessary'\" centos:!ppos.novelpay.pl")
     }
 }

 job("ansible reboot Centos") {
    logRotator {
        numToKeep(300)
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/centos_reboot.yml")
     }
}

 job("ansible reboot Ubuntu") {
    logRotator {
        numToKeep(300)
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/reboot.yml -i /home/kmonti/inventory -l artifactubuntu,novelpayubuntu")
     }
}

 job("ansible debian_upgrade") {
    logRotator {
        numToKeep(300)
    }
  triggers {
        cron('H 21 * * *')
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/debian_upgrade.yml -i /home/kmonti/ansible/inventory -l artifactubuntu,novelpayubuntu")
     }
 }

 job("ansible NPNTMS debian_upgrade") {
    logRotator {
        numToKeep(100)
    }
  triggers {
        cron('H 21 * * *')
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/debian_upgrade.yml -i /home/kmonti/ansible/inventory -l npntms")
     }
 }

job("ansible centos_upgrade") {
    logRotator {
        numToKeep(100)
    }
  triggers {
        cron('H 20 * * *')
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/centos_upgrade.yml -i /home/kmonti/ansible/inventory")
     }
 }

job("ansible ntp") {
    logRotator {
        numToKeep(100)
    }
  triggers {
        cron('H * * * *')
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/ntp.yml -i /home/kmonti/ansible/inventory")
     }
 }

  job("testinfra ntms db1") {
     logRotator {
        numToKeep(100)
    }
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
    triggers {
        cron('H * * * *')
    }
    steps {
      shell("mkdir -p target/test-reports/")
      shell("sudo -u  ${user} /bin/py.test test_db1*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 192.99.119.27 --junit-xml /tmp/junit_db1.xml")
    }
    }
}

  job("testinfra ntms db2") {
     logRotator {
        numToKeep(100)
    }
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
    triggers {
        cron('H * * * *')
    }
    steps {
      shell("mkdir -p target/test-reports/")
      shell("sudo -u  ${user} /bin/py.test test_db2*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 51.77.198.199 --junit-xml /tmp/junit_db2.xml")
    }
    }
}

  job("testinfra ntms amq1") {
     logRotator {
        numToKeep(100)
    }
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
    triggers {
        cron('H * * * *')
    }
    steps {
      shell("mkdir -p target/test-reports/")
      shell("sudo -u  ${user} /bin/py.test test_amq1*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 192.99.119.25 --junit-xml /tmp/junit_amq1.xml")
    }
    }
}

  job("testinfra ntms amq2") {
     logRotator {
        numToKeep(100)
    }
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
    triggers {
        cron('H * * * *')
    }
    steps {
      shell("mkdir -p target/test-reports/")
      shell("sudo -u  ${user} /bin/py.test test_amq2*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 51.77.198.197 --junit-xml /tmp/junit_amq2.xml")
    }
    }
}

  job("testinfra ntms wf1") {
     logRotator {
        numToKeep(100)
    }
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }

    triggers {
        cron('H * * * *')
    }
    steps {
      shell("mkdir -p target/test-reports/")
      shell("sudo -u  ${user} /bin/py.test test_wf1*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 192.99.119.26 --junit-xml /tmp/junit_wf1.xml")
    }
    }
}

  job("testinfra ntms wf2") {
     logRotator {
        numToKeep(100)
    }
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
    triggers {
        cron('H * * * *')
    }
    steps {
      shell("mkdir -p target/test-reports/")
      shell("sudo -u  ${user} /bin/py.test test_wf2*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 51.77.198.198 --junit-xml /tmp/junit_wf2.xml")
    }
    }
}

  job("testinfra ntms front1") {
     logRotator {
        numToKeep(100)
    }
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
    triggers {
        cron('H * * * *')
    }
    steps {
      shell("mkdir -p target/test-reports/")
      shell("sudo -u  ${user} /bin/py.test test_front1*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 192.99.119.24 --junit-xml /tmp/junit_front1.xml")
    }
    }
}

  job("testinfra ntms front2") {
     logRotator {
        numToKeep(100)
    }
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
    triggers {
        cron('H * * * *')
    }
    steps {
      shell("mkdir -p target/test-reports/")
      shell("sudo -u  ${user} /bin/py.test test_front2*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 51.77.198.196 --junit-xml /tmp/junit_front2.xml")
    }
    }
}
