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
"cgmanager",
"confluence",
"console-setup",
"cron",
"dbus",
"fail2ban",
"fisheye",
"getty@tty1",
"grub-common",
"haproxy",
"ifup@eth0",
"irqbalance",
"jira",
"keyboard-setup",
"kmod-static-nodes",
"lvm2-lvmetad",
"lvm2-monitor",
"munin-node",
"networking",
"nfs-config",
"ondemand",
"pms",
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
"systemd-fsck@dev-sdb1",
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


