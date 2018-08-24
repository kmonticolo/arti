# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'
# systemctl list-units --type=service --state=active
# systemctl list-units --type=service --state=active|grep \.service |sed  's/.service//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"console-getty",
"crond",
"dbus",
"getty@tty2",
"httpd",
"jboss",
"munin-node",
"network",
"postgresql-9.4",
"quotaon",
"rhel-readonly",
"sshd",
"sysstat",
"systemd-journald",
"systemd-logind",
"systemd-random-seed",
"systemd-tmpfiles-setup",
"systemd-udev-trigger",
"systemd-udevd",
"systemd-update-utmp",
"systemd-user-sessions",
"vzquota",
"zabbix-agent",

    ):  
        service= host.service(spec)
        assert service.is_running


