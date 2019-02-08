# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'
# systemctl list-units --type=service --state=active
# systemctl list-units --type=service --state=active|grep \.service |sed  's/.service//g' | awk '{print "\""$1"\","}'

def test_serv_active(host):
    for spec in (
"accounts-daemon",
"acpid",
"apparmor",
"nginx",
"apport",
"atd",
"cgmanager",
"console-setup",
"cron",
"dbus",
"fail2ban",
"getty@tty1",
"grub-common",
"ifup@eth0",
"irqbalance",
"keyboard-setup",
"kmod-static-nodes",
"networking",
"ondemand",
"polkitd",
"postgresql",
"postgresql@9.3-main",
"postgresql@9.5-main",
"rc-local",
"resolvconf",
"rsyslog",
"setvtrgb",
"ssh",
"sysstat",
"systemd-journal-flush",
"systemd-journald",
"systemd-logind",
"systemd-modules-load",
"systemd-random-seed",
"systemd-remount-fs",
"systemd-sysctl",
"systemd-tmpfiles-setup-dev",
"systemd-tmpfiles-setup",
"systemd-udev-trigger",
"systemd-udevd",
"systemd-update-utmp",
"systemd-user-sessions",
"thermald",
"ufw",
"unattended-upgrades",
"user@1003",
"zabbix-agent",
    ):  
        service= host.service(spec)
        assert service.is_running


