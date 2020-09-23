# systemctl list-unit-files | grep service.*enabled |sed 's/.service.*enabled//g' | awk '{print "\""$1"\","}'

def test_serv(host):
    for spec in (
"accounts-daemon",
"atd",
"autovt@",
"containerd",
"cron",
"docker-ntms",
"docker",
"fail2ban",
"getty@",
"iscsi",
"iscsid",
"lvm2-monitor",
"lxcfs",
"lxd-containers",
"networking",
"nginx",
"open-iscsi",
"open-vm-tools",
"postgresql",
"resolvconf",
"rsyslog",
"snapd.apparmor",
"snapd.autoimport",
"snapd.core-fixup",
"snapd.recovery-chooser-trigger",
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


