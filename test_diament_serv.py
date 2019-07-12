# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"accounts-daemon",
"atd",
"autovt@",
"cgmanager",
"cgproxy",
"cron",
"dbus-org.freedesktop.thermald",
"dns-clean",
"fail2ban",
"getty@",
"haveged",
"lvm2-monitor",
"networking",
"nfs-kernel-server",
"nfs-server",
"nginx",
"pppd-dns",
"resolvconf",
"rsyslog",
"ssh",
"sshd",
"sssd",
"strongswan",
"syslog",
"systemd-timesyncd",
"thermald",
"ufw",
"unattended-upgrades",
"ureadahead",
"wildfly",
"zabbix-agent",

    ):  
        service= host.service(spec)
        assert service.is_enabled


