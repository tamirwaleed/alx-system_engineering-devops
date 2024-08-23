# changing the user limits

exec {'change hard user limits':
  command => 'sed -i "/holberton hard/s/4/50000/"  /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec {'change soft user limits':
  command => 'sed -i "/holberton soft/s/5/50000/"  /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
