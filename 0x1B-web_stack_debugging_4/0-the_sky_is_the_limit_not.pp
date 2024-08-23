# reducing failures to 0

exec {'sky is the limit':
  command => 'sed -i "s/4096/15/" /etc/default/nginx && sudo nginx restart' 
  path    => '/usr/bin:/bin/',
}
