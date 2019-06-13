# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'
# systemctl list-units --type=service --state=active
# systemctl list-units --type=service --state=active|grep \.service |sed  's/.service//g' | awk '{print "\""$1"\","}'

def test_serv_active(host):
    for spec in (
"auditd",
"crond",
"dbus",
"fail2ban",
"firewalld",
"getty@tty1",
"jexec",
"kafka",
"kdump",
"kmod-static-nodes",
"lvm2-lvmetad",
"lvm2-monitor",
"lvm2-pvscan@8:3",
"network",
"NetworkManager-wait-online",
"NetworkManager",
"ntpd",
"polkit",
"postgresql",
"rhel-dmesg",
"rhel-domainname",
"rhel-import-state",
"rhel-readonly",
"rsyslog",
"sshd",
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
"wildfly",
"yum-cron",
"zabbix-agent",
"zookeeper",
    ):  
        service= host.service(spec)
        assert service.is_running


