# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"accounts-daemon",
"apparmor",
"atd",
"autovt@",
"blk-availability",
"cloud-config",
"cloud-final",
"cloud-init-local",
"cloud-init",
"console-setup",
"cron",
"dbus-org.freedesktop.resolve1",
"dbus-org.freedesktop.thermald",
"ebtables",
"fail2ban",
"friendly-recovery",
"getty@",
"irqbalance",
"iscsi",
"iscsid",
"keyboard-setup",
"lvm2-monitor",
"lxcfs",
"lxd-containers",
"networkd-dispatcher",
"nginx",
"ondemand",
"open-iscsi",
"open-vm-tools",
"pollinate",
"postgresql",
"rsync",
"rsyslog",
"setvtrgb",
"snapd.autoimport",
"snapd.core-fixup",
"snapd.seeded",
"snapd",
"snapd.system-shutdown",
"ssh",
"sshd",
"syslog",
"sysstat",
"systemd-networkd-wait-online",
"systemd-networkd",
"systemd-resolved",
"systemd-timesyncd",
"thermald",
"ufw",
"unattended-upgrades",
"ureadahead",
"vgauth",
"zabbix-agent",

    ):  
        service= host.service(spec)
        assert service.is_enabled


