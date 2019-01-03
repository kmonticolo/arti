# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'
# systemctl list-units --type=service --state=active
# systemctl list-units --type=service --state=active|grep \.service |sed  's/.service//g' | awk '{print "\""$1"\","}'

def test_serv_active(host):
    for spec in (
"accounts-daemon",
"apache-htcacheclean",
"apache2",
"apparmor",
"apport",
"atd",
"blk-availability",
"console-setup",
"cron",
"dbus",
"fail2ban",
"getty@tty1",
"grub-common",
"ifup@eth0",
"keyboard-setup",
"kmod-static-nodes",
"lvm2-lvmetad",
"lvm2-monitor",
"lvm2-pvscan@8:5",
"networkd-dispatcher",
"networking",
"nexus",
"ntp",
"polkit",
"postfix",
"postfix@-",
"postgresql",
"postgresql@10-main",
"postgresql@9.3-main",
"postgresql@9.5-main",
"resolvconf",
"rpcbind",
"rsyslog",
"setvtrgb",
"sonar",
"ssh",
"sysstat",
"systemd-journal-flush",
"systemd-journald",
"systemd-logind",
"systemd-modules-load",
"systemd-random-seed",
"systemd-remount-fs",
"systemd-resolved",
"systemd-sysctl",
"systemd-tmpfiles-setup-dev",
"systemd-tmpfiles-setup",
"systemd-udev-trigger",
"systemd-udevd",
"systemd-update-utmp",
"systemd-user-sessions",
"ufw",
"unattended-upgrades",
"user@1000",
"user@1001",
"user@1002",
"wildfly",
"wpa_supplicant",
"zabbix-agent",
    ):  
        service= host.service(spec)
        assert service.is_running
