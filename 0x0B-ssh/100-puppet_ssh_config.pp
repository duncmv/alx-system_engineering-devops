# configuring ssh
$cont = "Host *
	PasswordAuthentication no
	IdentityFile ~/.ssh/school"
file { '/root/.ssh/config':
  ensure  => present,
  content => $cont,
}
