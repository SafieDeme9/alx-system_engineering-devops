#Puppet manifest that kills a process named killmenow

exec { 'pkill' :
  command  => '/usr/bin/pkill -9 killmenow',
  onlyif   => 'pgrep killmenow',
  provider => 'shell',
}
