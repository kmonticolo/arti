# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"accounts-daemon",
"anacron-resume",
"anacron",
"atd",
"autovt@",
"avahi-daemon",
"bind9",
"bluetooth",
"brltty",
"cgmanager",
"cgproxy",
"cron",
"dbus-org.bluez",
"dbus-org.freedesktop.Avahi",
"dbus-org.freedesktop.ModemManager1",
"dbus-org.freedesktop.nm-dispatcher",
"dbus-org.freedesktop.thermald",
"display-manager",
"dns-clean",
"fail2ban",
"friendly-recovery",
"getty@",
"gpu-manager",
"lightdm",
"lvm2-monitor",
"ModemManager",
"network-manager",
"networking",
"NetworkManager-dispatcher",
"NetworkManager-wait-online",
"NetworkManager",
"nginx",
"postgresql",
"pppd-dns",
"resolvconf",
"rsyslog",
"snapd.autoimport",
"snapd.core-fixup",
"snapd.seeded",
"snapd",
"snapd.system-shutdown",
"ssh",
"sshd",
"syslog",
"thermald",
"ufw",
"unattended-upgrades",
"ureadahead",
"whoopsie",
"zabbix-agent",
#"wildfly-vtms",
    ):  
        service= host.service(spec)
        assert service.is_enabled


