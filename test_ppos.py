
# cron /var/spool/cron/jboss istnieje

# dodac firewall! i fail2ban
def test_crond_running(Process, Service, Socket, Command):
    assert Service("crond").is_enabled
    assert Service("crond").is_running

def test_java_running(Process, Service, Socket, Command):
    java = Process.get(comm="java")
    assert java.user == "jboss"
    assert java.group == "jboss"
    assert Socket("tcp://0.0.0.0:8443").is_listening
    assert Socket("tcp://0.0.0.0:4447").is_listening
    assert Socket("tcp://127.0.0.1:9990").is_listening
    assert Socket("tcp://127.0.0.1:9999").is_listening
    assert Socket("tcp://0.0.0.0:8080").is_listening

def test_jboss_running(Process, Service, Socket, Command):
    #assert Service("jboss").is_enabled
    assert Service("jboss").is_running

def test_firewalld_running(Process, Service, Socket, Command):
    assert Service("firewalld").is_enabled
    assert Service("firewalld").is_running
# /usr/bin/firewall-cmd --state
# /etc/httpd/ssl/ppos.crt
def test_ppos_cert_file(host):
    file = host.file("/etc/httpd/ssl/ppos.crt")
    assert file.user == "jboss"
    assert file.group == "jboss"
    assert file.mode == 0o664

def test_ppos_key_file(host):
    file = host.file("/etc/httpd/ssl/ppos.key")
    assert file.user == "jboss"
    assert file.group == "jboss"
    assert file.mode == 0o664

def test_munin_running(Process, Service, Socket, Command):
    assert Service("munin-node").is_enabled
    assert Service("munin-node").is_running

def test_httpd_running(Process, Service, Socket, Command):
    assert Service("httpd").is_enabled
    assert Service("httpd").is_running
    assert Socket("tcp://0.0.0.0:80").is_listening
    assert Socket("tcp://0.0.0.0:443").is_listening

def test_apache2_conf(host):
    conf = host.file("/etc/httpd/sites-enabled/ppos.conf")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.contains("VirtualHost \*:80")
    assert conf.contains("ProxyPassReverse.*/napi.*http://localhost:8443/napi")
    assert conf.contains("ProxyPass.*/PPOS.*https://localhost:8443/PPOS")

def test_ppos_conf(host):
    conf = host.file("/etc/httpd/conf.d/ppos.conf")
    assert conf.user == "root"
    assert conf.group == "root"
    assert conf.contains("VirtualHost _default_:443")
    assert conf.contains("ProxyPassReverse.*/ http://localhost:8080/PPOS/")
    assert conf.contains("ProxyPass.*/ http://localhost:8080/PPOS/ retry=1")
    assert conf.contains("SSLEngine.*on")
    assert conf.contains("SSLProxyEngine.*on")
    assert conf.contains("SSLCertificateFile.*/etc/httpd/ssl/novelpay.pl.pem")
    assert conf.contains("SSLCertificateKeyFile.*/etc/httpd/ssl/novelpay.pl.key")
    assert conf.contains("ServerName ppos.novelpay.pl")
    assert conf.contains("DocumentRoot /var/www/ppos/")

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql-9.4").is_enabled
    assert Service("postgresql-9.4").is_running

    postgres = Process.filter(comm="postgres")

    assert Socket("tcp://0.0.0.0:5432").is_listening
    assert Socket("tcp://::1:5432").is_listening

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running
    assert Socket("tcp://0.0.0.0:10050").is_listening

# netstat -aln |grep ^tcp.*LIST|awk '{print "\"tcp://"$4"\","}'

def test_listening_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://0.0.0.0:4949",
"tcp://0.0.0.0:22",
"tcp://0.0.0.0:5432",
"tcp://0.0.0.0:443",
"tcp://0.0.0.0:8443",
"tcp://0.0.0.0:4447",
"tcp://0.0.0.0:10050",
"tcp://127.0.0.1:9990",
"tcp://127.0.0.1:9999",
"tcp://0.0.0.0:80",
"tcp://0.0.0.0:8080",
"tcp://:::22",
"tcp://:::5432",

    ):  
        socket = host.socket(spec)
        assert socket.is_listening


