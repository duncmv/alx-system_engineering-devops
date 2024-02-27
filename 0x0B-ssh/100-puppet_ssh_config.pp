# configuring ssh
$cont = "Host *
	PasswordAuthentication no
	IdentityFile ~/.ssh/school"
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => $cont,
}
