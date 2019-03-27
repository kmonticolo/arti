# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"auditd",
"autovt@",

"crond",
"dbus-org.freedesktop.NetworkManager",
"dbus-org.freedesktop.nm-dispatcher",
"getty@",
"irqbalance",
"kdump",
"lvm2-monitor",
"microcode",
"NetworkManager-dispatcher",
"NetworkManager",
"nginx",
"ntpd",
"postfix",
"rsyslog",
"smartd",
"sshd",
"sysstat",
"systemd-readahead-collect",
"systemd-readahead-drop",
"systemd-readahead-replay",
"tuned",
"vgauthd",
"vmtoolsd",
"zabbix-agent",
    ):  
        service= host.service(spec)
        assert service.is_enabled


