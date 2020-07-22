def repo = 'https://github.com/kmonticolo/arti.git'
def sshconfig='./ssh_config'
def user='kmonti'

for (host in [ 
  'alpha',
  'beta',
  'soter',
  'qantms',
  'vdisk',
  'ppos2',
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
      shell("sudo -u ${user} timeout 300 /bin/py.test test_${host}.py test_${host}_active.py test_${host}_serv.py test_common.py test_ntp.py --ssh-config=${sshconfig} --hosts ${host}.novelpay.pl --junit-xml /tmp/junit_${host}.xml")          // copy junit files from /tmp as jenkins
      //shell("cp /tmp/junit_${host}.xml target/test-reports/")
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
  'draco', 
  'hydra', 
  //'luna', 
  'lynx', 
  'orion', 
  'pavo', 
  'taurus',
  'spinel',
  'fantazja',
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
      // needed for junit tests, run as jenkins
      shell("mkdir -p target/test-reports/")
      // spawn testinfra via sudo and store reports in junit.xml
      shell("sudo -u ${user} timeout 300 /bin/py.test test_${host}.py test_${host}_active.py test_${host}_serv.py test_common.py --ssh-config=${sshconfig} --hosts ${host}.artifact.pl --junit-xml /tmp/junit_${host}.xml")    
      // copy junit files from /tmp as jenkins
      //shell("cp /tmp/junit_${host}.xml target/test-reports/")
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


//job("ansible aide update") {
//    logRotator {
//        numToKeep(100)
//    }
//  triggers {
//        cron('H 4 * * *')
//    }
//     steps {
//        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/aide.yml -i /home/kmonti/ansible/inventory")
//     }              
// }

//job("ansible aide check") {
//    logRotator {
//        numToKeep(100)
//    }
//  triggers {
//        cron('H 0 * * *')
//    }
//     steps {
//        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/aide_check.yml -i /home/kmonti/ansible/inventory")
//     }              
// }

job("ansible NPNTMS aide update") {
    logRotator {
        numToKeep(100)
    }
  triggers {
        cron('H 13 * * *')
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/aide.yml -i /home/kmonti/ansible/inventory -l npntms")
     }              
 }

job("ansible NPNTMS aide check") {
    logRotator {
        numToKeep(100)
    }
  triggers {
        cron('H 12 * * *')
    }
     steps {
        shell("sudo -u kmonti ansible-playbook /home/kmonti/ansible/aide_check.yml -i /home/kmonti/ansible/inventory -l npntms")
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

job("copy_junit_reports") {
    logRotator {
        numToKeep(100)
    }
     steps {
        shell("for i in \$(ls /tmp/junit*xml |sed -e 's/^.*_//' -e 's/.xml\$//g'); do cp /tmp/junit_\${i}.xml //var/lib/jenkins/workspace/testinfra \${i}/target/test-reports/junit_\${i}.xml || exit 0 ;done")
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
      // needed for junit tests, run as jenkins
      shell("mkdir -p target/test-reports/")
      // spawn testinfra via sudo and store reports in junit.xml
      shell("sudo -u ${user} timeout 300 /bin/py.test test_db1*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 192.99.119.27 --junit-xml /tmp/junit_db1.xml")    
      // copy junit files from /tmp as jenkins
      //shell("cp /tmp/junit_db1.xml target/test-reports/")
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
      // needed for junit tests, run as jenkins
      shell("mkdir -p target/test-reports/")
      // spawn testinfra via sudo and store reports in junit.xml
      shell("sudo -u ${user} timeout 300 /bin/py.test test_db2*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 51.77.198.199 --junit-xml /tmp/junit_db2.xml")    
      // copy junit files from /tmp as jenkins
      //shell("cp /tmp/junit_db2.xml target/test-reports/")
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
      // needed for junit tests, run as jenkins
      shell("mkdir -p target/test-reports/")
      // spawn testinfra via sudo and store reports in junit.xml
      shell("sudo -u ${user} timeout 300 /bin/py.test test_amq1*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 192.99.119.25 --junit-xml /tmp/junit_amq1.xml")    
      // copy junit files from /tmp as jenkins
      //shell("cp /tmp/junit_amq1.xml target/test-reports/")
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
      // needed for junit tests, run as jenkins
      shell("mkdir -p target/test-reports/")
      // spawn testinfra via sudo and store reports in junit.xml
      shell("sudo -u ${user} timeout 300 /bin/py.test test_amq2*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 51.77.198.197 --junit-xml /tmp/junit_amq2.xml")    
      // copy junit files from /tmp as jenkins
      //shell("cp /tmp/junit_amq1.xml target/test-reports/")
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
      // needed for junit tests, run as jenkins
      shell("mkdir -p target/test-reports/")
      // spawn testinfra via sudo and store reports in junit.xml
      shell("sudo -u ${user} timeout 300 /bin/py.test test_wf1*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 192.99.119.26 --junit-xml /tmp/junit_wf1.xml")    
      // copy junit files from /tmp as jenkins
      //shell("cp /tmp/junit_wf1.xml target/test-reports/")
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
      // needed for junit tests, run as jenkins
      shell("mkdir -p target/test-reports/")
      // spawn testinfra via sudo and store reports in junit.xml
      shell("sudo -u ${user} timeout 300 /bin/py.test test_wf2*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 51.77.198.198 --junit-xml /tmp/junit_wf2.xml")
      // copy junit files from /tmp as jenkins
      //shell("cp /tmp/junit_wf2.xml target/test-reports/")
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
      // needed for junit tests, run as jenkins
      shell("mkdir -p target/test-reports/")
      // spawn testinfra via sudo and store reports in junit.xml
      shell("sudo -u ${user} timeout 300 /bin/py.test test_front1*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 192.99.119.24 --junit-xml /tmp/junit_front1.xml")
      // copy junit files from /tmp as jenkins
      //shell("cp /tmp/junit_front1.xml target/test-reports/")
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
      // needed for junit tests, run as jenkins
      shell("mkdir -p target/test-reports/")
      // spawn testinfra via sudo and store reports in junit.xml
      shell("sudo -u ${user} timeout 300 /bin/py.test test_front2*.py test_common.py --ssh-config=./ssh_ntms_config --hosts 51.77.198.196 --junit-xml /tmp/junit_front2.xml")
      // copy junit files from /tmp as jenkins
      //shell("cp /tmp/junit_front2.xml target/test-reports/")
    }
    }
}

  job("testinfra ppos") {
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
      shell("sudo -u ${user} timeout 300 /bin/py.test test_ppos_active.py  test_ppos.py  test_ppos_serv.py test_common.py --ssh-config=${sshconfig} --hosts ppos.novelpay.pl --junit-xml /tmp/junit_ppos.xml")          
      // copy junit files from /tmp as jenkins
      //shell("cp /tmp/junit_front2.xml target/test-reports/")
    }
    }
}
