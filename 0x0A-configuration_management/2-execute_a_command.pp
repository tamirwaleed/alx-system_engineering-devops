#a manifest that kills kilmenow

exec { 'pkill -f killmenow':
  path   => '/usr/bin/:/usr/local/bin:/bin/'
}
