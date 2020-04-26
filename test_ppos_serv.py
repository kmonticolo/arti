# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"autovt@",
"crond",
"dbus-org.fedoraproject.FirewallD1",
"fail2ban",
"firewalld",
"getty@",
"httpd",
"ntpd",
"postgresql-9.4",
"quotaon",
"rhel-autorelabel-mark",
"rhel-autorelabel",
"rhel-configure",
"rhel-dmesg",
"rhel-domainname",
"rhel-import-state",
"rhel-loadmodules",
"rhel-readonly",
"rpcbind",
"sshd",
"sysstat",
"systemd-readahead-collect",
"systemd-readahead-drop",
"systemd-readahead-replay",
"vzfifo",
"yum-cron",
"zabbix-agent",

    ):  
        service= host.service(spec)
        assert service.is_enabled


