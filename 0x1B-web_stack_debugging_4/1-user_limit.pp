#Changed OS configuration with an ability to login with the holberton user

file { 'loginFile':
    ensure  => present,
    path    => '/etc/security/limits.conf',
    content => '#File erased'
}
