# Using Puppet, create a file in /tmp.

# Define a file resource
file {'/tmp/school':
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
