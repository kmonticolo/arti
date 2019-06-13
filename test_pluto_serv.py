# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"auditd",
"crond",
"dbus-org.fedoraproject.FirewallD1",
"dbus-org.freedesktop.NetworkManager",
"dbus-org.freedesktop.nm-dispatcher",
"fail2ban",
"firewalld",
"irqbalance",
"kafka",
"kdump",
"lvm2-monitor",
"microcode",
"NetworkManager-dispatcher",
"NetworkManager-wait-online",
"NetworkManager",
"ntpd",
"postfix",
"postgresql",
"rhel-autorelabel",
"rhel-configure",
"rhel-dmesg",
"rhel-domainname",
"rhel-import-state",
"rhel-loadmodules",
"rhel-readonly",
"rsyslog",
"sshd",
"systemd-readahead-collect",
"systemd-readahead-drop",
"systemd-readahead-replay",
"tuned",
"vtms_cm",
"wildfly",
"yum-cron",
"zabbix-agent",
"zookeeper",
    ):  
        service= host.service(spec)
        assert service.is_enabled


