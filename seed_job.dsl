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
     
      shell("sudo -u ${user} /bin/py.test test_${host}*.py test_common.py --ssh-config=${sshconfig} --hosts ${host}.novelpay.pl")    
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
     
      shell("sudo -u ${user} /bin/py.test test_${host}*.py test_common.py --ssh-config=${sshconfig} --hosts ${host}.artifact.pl")    
    }
    }
}
}
