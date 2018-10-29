def repo = 'https://github.com/kmonticolo/arti.git'

job('testinfra alpha') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=alpha; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.novelpay.pl')    
    }
    }
}

job('testinfra beta') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=beta; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.novelpay.pl')    
    }
    }
}

job('testinfra beryl') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=beryl; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra db') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=db; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.novelpay.pl')    
    }
    }
}

job('testinfra diament') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=diament; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra draco') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=draco; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra gemini') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=gemini; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra hydra') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=hydra; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra luna') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=luna; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra lynx') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=lynx; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra ntms') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=ntms; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.novelpay.pl')    
    }
    }
}

job('testinfra opal') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=opal; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra orion') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=orion; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra pavo') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=pavo; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra ppos') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=ppos; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.novelpay.pl')    
    }
    }
}

job('testinfra rubin') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=rubin; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra soter') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=soter; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.novelpay.pl')    
    }
    }
}

job('testinfra spinel') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=spinel; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra szmaragd') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=szmaragd; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra taurus') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=taurus; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}

job('testinfra topaz') {
  scm {
      git {
          remote { url(repo) }
          branches('master')
          extensions { }
        }
      
    triggers {
        scm('H * * * *')
    }
    steps {
     
        shell('HOST=topaz; SSHCONFIG=./ssh_config ; sudo -u kmonti /bin/py.test test_${HOST}*.py --ssh-config=${SSHCONFIG} --hosts ${HOST}.artifact.pl')    
    }
    }
}
