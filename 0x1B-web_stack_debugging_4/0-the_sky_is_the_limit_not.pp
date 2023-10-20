# Puppet manifest to fix amount of traffic nginx can handle

# Changes ulimit from 15 to 4096
exec { 'change-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

# restart nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d'
}
