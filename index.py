#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#some config stuff
#SERVER = 'gevent'
SERVER = 'wsgiref'
URLPREFIX = 'http://home.kiney.de/ds-anmeldung'
DEBUGMODE = True
DBURL = 'sqlite:///ltb.db'

#gevent monkey patching MUST happen before other imports
if SERVER == 'gevent' and __name__ == '__main__':
    from gevent import monkey; monkey.patch_all()

from ltb import LtbDB

from bottle import get
import bottle

ltbdb = LtbDB(DBURL)

@get('/')
def index():
    return str(ltbdb.get_all_ltbs())


if __name__ == '__main__':
    #logging.basicConfig(filename='signup.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')
    bottle.debug(DEBUGMODE)
    bottle.run(host='127.0.0.1', port=8080, server=SERVER)
