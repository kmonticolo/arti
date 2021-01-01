# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"accounts-daemon",
"atd",
"autovt@",
"binfmt-support",
"cgmanager",
"cgproxy",
"cron",
"dns-clean",
"fail2ban",
"getty@",
"lvm2-monitor",
"mysql",
"networking",
"open-vm-tools",
"pppd-dns",
"resolvconf",
"rsyslog",
"ssh",
"sshd",
"syslog",
"systemd-timesyncd",
"ufw",
"unattended-upgrades",
"ureadahead",
"vgauth",
"zabbix-agent",
    ):  
        service= host.service(spec)
        assert service.is_enabled
