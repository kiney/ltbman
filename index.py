#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#some config stuff
SERVER = 'wsgiref'
URLPREFIX = 'http://localhost:8080'
DEBUGMODE = True
DBURL = 'sqlite:///ltb.db'

# neue bücher MüSSEN mit Titel gemoved werden

from ltb import LtbDB

from bottle import get, jinja2_view, Jinja2Template
import bottle

ltbdb = LtbDB(DBURL)

Jinja2Template.settings = {
    'autoescape': True,
}

@get('/')
@jinja2_view('index.j2')
def index():
    return {'pfx': URLPREFIX}

@get('/ltb/all')
@jinja2_view('all.j2')
def all():
    return {'pfx': URLPREFIX, 'ltbs': ltbdb.get_all_ltbs()}


if __name__ == '__main__':
    #logging.basicConfig(filename='signup.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')
    bottle.debug(DEBUGMODE)
    bottle.run(host='127.0.0.1', port=8080, server=SERVER)
