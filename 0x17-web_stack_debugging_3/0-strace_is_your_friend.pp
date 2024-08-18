# a puppet code for webstack debugging
# correcting a file extension to php

exec { 'fix-website':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin/:/bin/',
}
