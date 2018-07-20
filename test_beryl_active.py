# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'
# systemctl list-units --type=service --state=active
# systemctl list-units --type=service --state=active|grep \.service |sed  's/.service//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"apport",
"atd",
"console-setup",
"cron",
"dbus",
"fail2ban",
"getty@tty1",
"grub-common",
"irqbalance",
"keyboard-setup",
"kmod-static-nodes",
"lvm2-lvmetad",
"lvm2-monitor",
"networking",
"ondemand",
"polkitd",
"rc-local",
"resolvconf",
"rsyslog",
"setvtrgb",
"snapd",
"ssh",
"systemd-journal-flush",
"systemd-journald",
"systemd-logind",
"systemd-modules-load",
"systemd-random-seed",
"systemd-remount-fs",
"systemd-sysctl",
"systemd-timesyncd",
"systemd-tmpfiles-setup-dev",
"systemd-tmpfiles-setup",
"systemd-udev-trigger",
"systemd-udevd",
"systemd-update-utmp",
"systemd-user-sessions",
"ufw",
"unattended-upgrades",
"user@1001",
"wildfly-ntms",
"wildfly-vtms",
    ):  
        service= host.service(spec)
        assert service.is_running


