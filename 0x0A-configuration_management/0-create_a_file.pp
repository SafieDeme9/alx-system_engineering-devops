#Create a file with puppet

file { '/tmp/school':
  ensure => present,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0744',
}

