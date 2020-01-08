# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"accounts-daemon",
"apache-htcacheclean",
"apache2",
"apparmor",
"atd",
"autovt@",
"blk-availability",
"console-setup",
"cron",
"dbus-fi.w1.wpa_supplicant1",
"dbus-org.freedesktop.resolve1",
"dbus-org.freedesktop.thermald",
"dns-clean",
"fail2ban",
"getty@",
"irqbalance",
"keyboard-setup",
"lvm2-monitor",
"networkd-dispatcher",
"networking",
"ntp",
"ondemand",
"portmap",
"postfix",
"postgresql",
"pppd-dns",
"resolvconf",
"rpcbind",
"rsync",
"rsyslog",
"setvtrgb",
"ssh",
"sshd",
"syslog",
"sysstat",
"systemd-resolved",
"systemd-timesyncd",
"thermald",
"ufw",
"unattended-upgrades",
"ureadahead",
"wpa_supplicant",
"zabbix-agent",

    ):  
        service= host.service(spec)
        assert service.is_enabled


