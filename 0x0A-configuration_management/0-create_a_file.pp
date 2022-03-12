# Creates a file
file { '/tmp/school':
  ensure  => present,
  path    => '/tmp/school',
  mode    => '0744',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
}