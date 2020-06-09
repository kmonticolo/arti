# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"apache2",
"autovt@",
"bind9",
"clamav-daemon",
"clamav-freshclam",
"console-setup",
"cron",
"fail2ban",
"getty@",
"irqbalance",
"keyboard-setup",
"lvm2-monitor",
"mariadb",
"mysql",
"mysqld",
"networking",
"postfix",
"postgresql",
"rsync",
"rsyslog",
"smartd",
"smartmontools",
"ssh",
"sshd",
"syslog",
"systemd-timesyncd",
"urbackupclientbackend",
"zabbix-agent",
    ):  
        service= host.service(spec)
        assert service.is_enabled


