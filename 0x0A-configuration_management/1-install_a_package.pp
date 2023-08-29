# A manifest file to install package

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
