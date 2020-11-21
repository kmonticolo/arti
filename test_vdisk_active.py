def test_serv_active(host):
    for spec in (
"acpid",
"apache2",
"bind9",
"clamav-daemon",
"clamav-freshclam",
"console-setup",
"cron",
"dbus",
"fail2ban",
"getty@tty1",
"hddtemp",
"irqbalance",
"keyboard-setup",
"lvm2-lvmetad",
"lvm2-monitor",
"mariadb",
"mdmonitor",
"ntp",
"postfix",
"postfix@-",
"postgresql",
"postgresql@9.4-main",
"postgresql@9.6-main",
"rc-local",
"rsyslog",
"smartd",
"ssh",
"sysstat",
"systemd-fsck-root",
"systemd-fsck@dev-md3",
"systemd-journal-flush",
"systemd-journald",
"systemd-logind",
"systemd-random-seed",
"systemd-remount-fs",
"systemd-sysctl",
"systemd-tmpfiles-setup-dev",
"systemd-tmpfiles-setup",
"systemd-udev-trigger",
"systemd-udevd",
"systemd-update-utmp",
"systemd-user-sessions",
"urbackupclientbackend",
"user@1002",
"zabbix-agent",
    ):
        service= host.service(spec)
        assert service.is_running
