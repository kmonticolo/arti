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
"networking",
"postgresql",
"pppd-dns",
"resolvconf",
"rsyslog",
"ssh",
"sshd",
"syslog",
"thermald",
"ufw",
"unattended-upgrades",
"ureadahead",
"zabbix-agent",
    ):  
        service= host.service(spec)
        assert service.is_enabled


