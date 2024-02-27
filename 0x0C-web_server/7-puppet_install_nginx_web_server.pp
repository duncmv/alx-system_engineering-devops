# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
}

# Create Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	rewrite ^/redirect_me http://duncmeister.tech permanent;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		try_files $uri $uri/ =404;
	}
',
}
