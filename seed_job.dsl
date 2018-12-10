def repo = 'https://github.com/kmonticolo/arti.git'
def sshconfig='./ssh_config'
def user='kmonti'

for (host in [ 
  'alpha',
  'beta',
  'soter',
  'ntms',
  'ppos',
  'db' ]) {
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
      // needed for junit tests, run as jenkins
      shell("mkdir -p target/test-reports/")
      // spawn testinfra via sudo and store reports in junit.xml
      shell("sudo -u ${user} /bin/py.test test_${host}*.py test_common.py --ssh-config=${sshconfig} --hosts ${host}.novelpay.pl --junit-xml /tmp/junit_${host}.xml")    
      // copy junit files from /tmp as jenkins
      shell("cp /tmp/junit_${host}.xml target/test-reports/")
    }
     publishers {
        archiveJunit('target/test-reports/*xml')
    }
    }
}
}


for (host in [ 
  'diament', 
  'topaz', 
  'rubin', 
  'szmaragd', 
  'opal',
  'beryl', 
  'spinel', 
  'draco', 
  'hydra', 
  'luna', 
  'lynx', 
  'orion', 
  'pavo', 
  'taurus', 
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
      // needed for junit tests, run as jenkins
      shell("mkdir -p target/test-reports/")
      // spawn testinfra via sudo and store reports in junit.xml
      shell("sudo -u ${user} /bin/py.test test_${host}*.py test_common.py --ssh-config=${sshconfig} --hosts ${host}.artifact.pl --junit-xml /tmp/junit_${host}.xml")    
      // copy junit files from /tmp as jenkins
      shell("cp /tmp/junit_${host}.xml target/test-reports/")
    }
      publishers {
        archiveJunit('target/test-reports/*xml')
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
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/reboot_needed.yml -i /home/kmonti/ansible/inventory")
     }
              
 }

	
 job("ansible debian_upgrade") {
    logRotator {
        numToKeep(100)
    }
  triggers {
        cron('H 21 * * *')
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/debian_upgrade.yml -i /home/kmonti/ansible/inventory")
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



job("ansible aide update") {
    logRotator {
        numToKeep(100)
    }
  triggers {
        cron('H 4 * * *')
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/aide.yml -i /home/kmonti/ansible/inventory")
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
