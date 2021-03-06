# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'
# systemctl list-units --type=service --state=active
# systemctl list-units --type=service --state=active|grep \.service |sed  's/.service//g' | awk '{print "\""$1"\","}'

def test_serv_active(host):
    for spec in (
"accounts-daemon",
"acpid",
"apache2",
"apparmor",
"apport",
"atd",
"binfmt-support",
"cgmanager",
"confluence",
"console-setup",
"cron",
"dbus",
"exim4",
"fail2ban",
"flexlm",
"getty@tty1",
"grub-common",
"ifup@eth0",
"irqbalance",
"jira",
"keyboard-setup",
"kmod-static-nodes",
"lvm2-lvmetad",
"lvm2-monitor",
"mysql",
"networking",
"nscd",
"ondemand",
"polkitd",
"prosody",
"rc-local",
"resolvconf",
"rsyslog",
"setvtrgb",
"slapd",
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
"ufw",
"unattended-upgrades",
"zabbix-agent",
    ):  
        service= host.service(spec)
        assert service.is_running


