import pytest

def test_apache2_running(Process, Service, Socket, Command):
    assert Service("apache2").is_enabled
    assert Service("apache2").is_running

def test_apache_validate(Command):
    command = Command('sudo apache2ctl -t')
    assert command.rc == 0

def test_cron_running(Process, Service, Socket, Command):
    assert Service("cron").is_enabled
    assert Service("cron").is_running

def test_fail2ban_running(Process, Service, Socket, Command):
    assert Service("fail2ban").is_enabled
    assert Service("fail2ban").is_running

@pytest.mark.parametrize("name", [
    ("python"),
    ("apache2"),
    ("apache2-bin"),
    ("apache2-data"),
    ("apache2-utils"),
    ("bind9"),
    ("bind9-host"),
    ("bind9utils"),
    ("clamav"),
    ("clamav-base"),
    ("clamav-daemon"),
    ("clamav-freshclam"),
    ("dattobd-dkms"),
    ("dattobd-utils"),
    ("etckeeper"),
    ("fail2ban"),
    ("galera-3"),
    ("owncloud"),
    ("owncloud-deps-php5"),
    ("owncloud-files"),
    ("php7.0-cli"),
    ("php7.0-common"),
    ("php7.0-curl"),
    ("php7.0-gd"),
    ("php7.0-intl"),
    ("php7.0-json"),
    ("php7.0-mbstring"),
    ("php7.0-mysql"),
    ("php7.0-opcache"),
    ("php7.0-readline"),
    ("php7.0-xml"),
    ("php7.0-zip"),
    ("postgresql"),
    ("postgresql-9.4"),
    ("postgresql-9.6"),
    ("postgresql-client"),
    ("postgresql-client-9.4"),
    ("postgresql-client-9.6"),
    ("postgresql-client-common"),
    ("postgresql-common"),
    ("postgresql-contrib-9.6"),
    ("python-antlr"),
    ("python-apt"),
    ("python-apt-common"),
    ("python-babel"),
    ("python-babel-localedata"),
    ("python-bs4"),
    ("python-cffi-backend"),
    ("python-chardet"),
    ("python-cryptography"),
    ("python-dateutil"),
    ("python-decorator"),
    ("python-docutils"),
    ("python-egenix-mxdatetime"),
    ("python-egenix-mxtools"),
    ("python-enum34"),
    ("python-feedparser"),
    ("python-funcsigs"),
    ("python-gevent"),
    ("python-greenlet"),
    ("python-html5lib"),
    ("python-idna"),
    ("python-imaging"),
    ("python-ipaddress"),
    ("python-jinja2"),
    ("python-ldap"),
    ("python-libxml2"),
    ("python-libxslt1"),
    ("python-lxml"),
    ("python-mako"),
    ("python-markupsafe"),
    ("python-minimal"),
    ("python-mock"),
    ("python-openid"),
    ("python-openssl"),
    ("python-passlib"),
    ("python-pbr"),
    ("python-pil:amd64"),
    ("python-pkg-resources"),
    ("python-psutil"),
    ("python-psycopg2"),
    ("python-pyasn1"),
    ("python-pychart"),
    ("python-pydot"),
    ("python-pygments"),
    ("python-pyinotify"),
    ("python-pyparsing"),
    ("python-pypdf"),
    ("python-renderpm:amd64"),
    ("python-reportlab"),
    ("python-reportlab-accel:amd64"),
    ("python-requests"),
    ("python-roman"),
    ("python-setuptools"),
    ("python-six"),
    ("python-stdnum"),
    ("python-suds"),
    ("python-support"),
    ("python-talloc"),
    ("python-tz"),
    ("python-urllib3"),
    ("python-utidylib"),
    ("python-vatnumber"),
    ("python-vobject"),
    ("python-webencodings"),
    ("python-werkzeug"),
    ("python-xlwt"),
    ("python-yaml"),
    ("python2.7"),
    ("python2.7-minimal"),
    ("python3"),
    ("python3-minimal"),
    ("python3-pyinotify"),
    ("python3-systemd"),
    ("python3.5"),
    ("python3.5-minimal"),
    ("rake"),
    ("zabbix-agent"),
    ("zabbix-get"),
    ("zabbix-sender"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("name,version", [
    ("python", "2.7"),

])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)

def test_postgres_running(Process, Service, Socket, Command):
    assert Service("postgresql").is_enabled
    assert Service("postgresql").is_running

    postgres = Process.filter(comm="postgres")

def test_rsyslogd_running(Process, Service, Socket, Command):
    assert Service("rsyslog").is_enabled
    assert Service("rsyslog").is_running

def test_zabbix_agent_running(Process, Service, Socket, Command):
    assert Service("zabbix-agent").is_enabled
    assert Service("zabbix-agent").is_running

def test_MD_array(Command):
    command = Command('awk \'/^md/ {printf "%s: ", $1}; /blocks/ {print $NF}\'  /proc/mdstat | awk \'/\[U+\]/ {print $0 }; /\[.*_.*\]/ {print $0 }\'')
    assert command.stdout.rstrip() == 'md2: [UU]\nmd3: [UU]'
    assert command.rc == 0

def test_owncloud_version(Command):
    command = Command(' cd /var/www/owncloud/ && sudo -u www-data php occ -V')
    assert command.stdout.rstrip() == 'ownCloud 10.3.2'
    assert command.rc == 0

  

# cd /var/www/owncloud/
# sudo -u www-data php occ upgrade
# fail2ban-client status owncloud
# urbackupclientctl status
# urbackupclientctl list-backupdirs
