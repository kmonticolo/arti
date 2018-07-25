# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'
# systemctl list-units --type=service --state=active
# systemctl list-units --type=service --state=active|grep \.service |sed  's/.service//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"auditd",
"chronyd",
"crond",
"dbus",
"firewalld",
"getty@tty1",
"gssproxy",
"irqbalance",
"kdump",
"kmod-static-nodes",
"lvm2-lvmetad",
"lvm2-monitor",
"lvm2-pvscan@8:2",
"munin-node",
"network",
"NetworkManager-wait-online",
"NetworkManager",
"nginx",
"polkit",
"postfix",
"rhel-dmesg",
"rhel-import-state",
"rhel-readonly",
"rsyslog",
"smartd",
"sshd",
"sysstat",
"systemd-binfmt",
"systemd-journal-flush",
"systemd-journald",
"systemd-logind",
"systemd-random-seed",
"systemd-remount-fs",
"systemd-sysctl",
"systemd-tmpfiles-setup-dev",
"systemd-tmpfiles-setup",
"systemd-udev-trigger",
"systemd-udevd",
"systemd-update-utmp",
"systemd-user-sessions",
"systemd-vconsole-setup",
"tuned",
"vgauthd",
"vmtoolsd",
"zabbix-agent",
    ):  
        service= host.service(spec)
        assert service.is_running


