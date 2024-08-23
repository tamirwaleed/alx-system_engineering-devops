# reducing failures to 0

exec {'sky is the limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/bin:/bin/',
}
