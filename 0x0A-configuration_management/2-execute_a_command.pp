#this is a comment
exec { 'pkill':
    command => 'pkill -f killmenow',
    path    => '/usr/bin',
  }
