# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"autovt@",
"chronyd",
"crond",
"dbus-org.freedesktop.NetworkManager",
"dbus-org.freedesktop.nm-dispatcher",
"fail2ban",
"getty@",
"irqbalance",
"kdump",
"lvm2-monitor",
"microcode",
"NetworkManager-dispatcher",
"NetworkManager-wait-online",
"NetworkManager",
"nginx",
"ntpd",
"postfix",
"rhel-autorelabel-mark",
"rhel-autorelabel",
"rhel-configure",
"rhel-dmesg",
"rhel-domainname",
"rhel-import-state",
"rhel-loadmodules",
"rhel-readonly",
"rsyslog",
"smartd",
"sshd",
"sysstat",
"systemd-readahead-collect",
"systemd-readahead-drop",
"systemd-readahead-replay",
"tuned",
"ufw",
"vgauthd",
"vmtoolsd",
"yum-cron",
"zabbix-agent",
    ):  
        service= host.service(spec)
        assert service.is_enabled


