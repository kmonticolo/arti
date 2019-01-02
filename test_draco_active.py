# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'
# systemctl list-units --type=service --state=active
# systemctl list-units --type=service --state=active|grep \.service |sed  's/.service//g' | awk '{print "\""$1"\","}'

def test_serv_active(host):
    for spec in (
"accounts-daemon",
"acpid",
"apparmor",
"apport",
"atd",
"console-setup",
"cron",
"dbus",
"fail2ban",
"getty@tty1",
"grub-common",
"ifup@ens160",
"irqbalance",
"iscsid",
"jenkins",
"keyboard-setup",
"kmod-static-nodes",
"lvm2-lvmetad",
"lvm2-monitor",
"lxcfs",
"lxd-containers",
"mdadm",
"networking",
"nginx",
"ondemand",
"open-iscsi",
"open-vm-tools",
"polkitd",
"postfix",
"postgresql",
"postgresql@9.5-main",
"psad",
"rc-local",
"resolvconf",
"rsyslog",
"setvtrgb",
"snapd.seeded",
"snapd",
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
"vgauth",
    ):  
        service= host.service(spec)
        assert service.is_running


