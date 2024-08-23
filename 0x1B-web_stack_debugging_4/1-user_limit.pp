# changing the user limits

exec {'change hard user limits':
  command => 'sed -i "s/^holberton.*hard.*nofile.*/holberton hard nofile 50000/"  /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec {'change soft user limits':
  command => 'sed -i "s/^holberton.*soft.*nofile.*/holberton soft nofile 50000/"  /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
