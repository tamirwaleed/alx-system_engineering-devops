# changing the user limits

exec {'change user limits':
  command => 'echo -e "holberton soft nofile 4096\nholberton hard nofile 8192"' >> /etc/security/limits.conf,
  path    => '/usr/bin/:/bin/',
}
