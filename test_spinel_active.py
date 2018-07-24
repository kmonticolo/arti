# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'
# systemctl list-units --type=service --state=active
# systemctl list-units --type=service --state=active|grep \.service |sed  's/.service//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"accounts-daemon",
"atd",
"cgmanager",
"cron",
"fail2ban",
"lvm2-monitor",
"munin-node",
"networking",
"nginx",
"postgresql",
"resolvconf",
"rsyslog",
"ssh",
"syslog",
"systemd-timesyncd",
"ufw",
"unattended-upgrades",
"zabbix-agent",
    ):  
        service= host.service(spec)
        assert service.is_running


