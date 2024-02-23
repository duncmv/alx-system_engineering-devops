# install flask using pip3

class { 'python':
  version => '3.8.10',
}

package { 'python3-pip':
  ensure => installed,
}

package { 'setuptools':
  ensure   => installed,
  provider => 'pip3',
}

package { 'wheel':
  ensure   => installed,
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
