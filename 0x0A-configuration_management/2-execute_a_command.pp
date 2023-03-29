#Puppet manifest that kills a process named killmenow

exec { 'killmenow'
  command  => '/usr/bin/pkill killmenow',
  onlyif   => 'pgrep killmenow',
  provider => 'shell',
}
