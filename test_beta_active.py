# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'
# systemctl list-units --type=service --state=active
# systemctl list-units --type=service --state=active|grep \.service |sed  's/.service//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"auditd",
"crond",
"dbus",
"firewalld",
"getty@tty1",
"hostSimulator",
"irqbalance",
"jexec",
"kdump",
"kmod-static-nodes",
"logServer",
"lvm2-lvmetad",
"lvm2-monitor",
"lvm2-pvscan@8:2",
"munin-node",
"network",
"NetworkManager",
"ntpd",
"oracle-xe",
"polkit",
"postfix",
"rhel-dmesg",
"rhel-import-state",
"rhel-readonly",
"rsyslog",
"si-config-server",
"sshd",
"sysstat",
"systemd-fsck@dev-sdb1",
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
"vcs",
"zabbix-agent",

    ):  
        service= host.service(spec)
        assert service.is_running

