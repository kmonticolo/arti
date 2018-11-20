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
