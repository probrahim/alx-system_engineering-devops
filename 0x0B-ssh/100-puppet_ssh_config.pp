exec { 'ssh_login':
  command => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  path    => '/usr/bin/'
}
