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

# Create Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx_config/nginx_default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Custom template for Nginx default site
file { '/etc/nginx/sites-available/default.erb':
  ensure  => present,
  content => '
server {
    listen 80;
    server_name localhost;

    location / {
        return 200 "Hello World!\n";
    }

    location /redirect_me {
        return 301 /new_location;
    }

    location /new_location {
        return 200 "This is the new location!\n";
    }
}
',
}

# Enable the default site by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

