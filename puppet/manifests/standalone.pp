#
# Standalone manifest - for dev Vagrant box.
#

import 'lib/*.pp'

include stdlib
include fabric
include git
include gunicorn
include nginx
include postgresql::server
include python
include sass
include uglifyjs
include vagrant

nginx::site { 'gunicorn':
  config => 'gunicorn',
}
# this is required to build Psycopg2
#package { [ 'postgresql-server-dev-all' ]:
#  ensure => 'installed',
#  }
# creates a blank db for our app to use
postgresql::db{ 'app_db':
  user          => 'flask_user',
  password      => 'flask_pass',
  grant         => 'all',
}
