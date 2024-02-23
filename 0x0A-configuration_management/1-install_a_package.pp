# install flask using pip3
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
  ensure   => '1.0.1',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
