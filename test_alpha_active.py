# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'
# systemctl list-units --type=service --state=active
# systemctl list-units --type=service --state=active|grep \.service |sed  's/.service//g' | awk '{print "\""$1"\","}'

def test_serv_active(host):
    for spec in (
"accounts-daemon",
"apparmor",
"apport",
"atd",
"blk-availability",
"cloud-config",
"cloud-final",
"cloud-init-local",
"console-setup",
"cron",
"dbus",
"ebtables",
"fail2ban",
"grub-common",
"keyboard-setup",
"kmod-static-nodes",
"lvm2-lvmetad",
"lvm2-monitor",
"lxcfs",
"lxd-containers",
"networkd-dispatcher",
"nginx",
"open-vm-tools",
"polkit",
"postgresql",
"postgresql@10-main",
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
"systemd-networkd-wait-online",
"systemd-networkd",
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
"thermald",
"ufw",
"unattended-upgrades",
"vgauth",
"zabbix-agent",


    ):  
        service= host.service(spec)
        assert service.is_running


