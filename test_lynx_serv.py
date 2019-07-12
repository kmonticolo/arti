# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"accounts-daemon",
"atd",
"auditd",
"autovt@",
"bind9",
"cron",
"fail2ban",
"getty@",
"iscsi",
"iscsid",
"lvm2-monitor",
"lxcfs",
"lxd-containers",
"mongod",
"networking",
"nginx",
"open-iscsi",
"open-vm-tools",
"orthphoto",
"postgresql",
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
"systemd-timesyncd",
"ufw",
"unattended-upgrades",
"ureadahead",
"vgauth",
"zabbix-agent",

    ):  
        service= host.service(spec)
        assert service.is_enabled


