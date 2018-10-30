def repo = 'https://github.com/kmonticolo/arti.git'
def sshconfig='./ssh_config'

for (host in [ 'alpha', 'beta', 'soter','ntms','ppos','db' ]) {
  job("testinfra ${host}") {
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
     
        shell("sudo -u kmonti /bin/py.test test_${host}*.py --ssh-config=${sshconfig} --hosts ${host}.novelpay.pl")    
    }
    }
}
}


for (host in [ 'diament', 'topaz', 'rubin', 'szmaragd' , 'opal','beryl' , 'spinel', 'draco', 'hydra', 'luna', 'lynx', 'orion', 'pavo', 'taurus', 'gemini' ]) {
  job("testinfra ${host}") {
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
     
        shell("sudo -u kmonti /bin/py.test test_${host}*.py --ssh-config=${sshconfig} --hosts ${host}.artifact.pl")    
    }
    }
}
}
