# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"auditd",
"autovt@",
"avahi-daemon",

"crond",
"dbus-org.fedoraproject.FirewallD1",
"dbus-org.freedesktop.Avahi",
"dbus-org.freedesktop.NetworkManager",
"dbus-org.freedesktop.nm-dispatcher",
"firewalld",
"getty@",
"irqbalance",
"kdump",
"lvm2-monitor",
"mdmonitor",
"microcode",
"munin-node",
"NetworkManager-dispatcher",
"NetworkManager",
"postfix",
"rsyslog",
"sshd",
"sysstat",
"systemd-readahead-collect",
"systemd-readahead-drop",
"systemd-readahead-replay",
"tuned",
"zabbix-agent",

    ):  
        service= host.service(spec)
        assert service.is_enabled


