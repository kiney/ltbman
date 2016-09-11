#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#some config stuff
SERVER = 'wsgiref'
URLPREFIX = 'http://localhost:8080'
DEBUGMODE = True
DBURL = 'sqlite:///ltb.db'

# neue bücher MüSSEN mit Titel gemoved werden

from ltb import LtbDB

from bottle import get, post, jinja2_view, Jinja2Template
import bottle

ltbdb = LtbDB(DBURL)
locs = ltbdb.lid.keys()

Jinja2Template.settings = {
    'autoescape': True,
}

@get('/')
@jinja2_view('index.j2')
def index():
    return {'pfx': URLPREFIX, 'locs': locs}

@get('/ltbs/all')
@jinja2_view('all.j2')
def all():
    return {'pfx': URLPREFIX, 'locs': locs, 'ltbs': ltbdb.get_all_ltbs()}

@get('/ltbs/<loc>')
@jinja2_view('by_location.j2')
def by_location(loc):
    return {'pfx': URLPREFIX, 'locs': locs, 'ltbs': ltbdb.get_ltbs_by_location(loc), 'loc': loc}

@get('/moveltb/form')
@jinja2_view('moveltb_form.j2')
def moveltb_form():
    #TODO
    return {'pfx': URLPREFIX, 'locs': locs}

@post('/moveltb/move')
def moveltb_form():
    pass
    #TODO. redirekt stuff

@get('/moveltb/result')
@jinja2_view('moveltb_result.j2')
def moveltb_form():
    #TODO
    return {'pfx': URLPREFIX, 'locs': locs}

if __name__ == '__main__':
    #logging.basicConfig(filename='signup.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')
    bottle.debug(DEBUGMODE)
    bottle.run(host='127.0.0.1', port=8080, server=SERVER)
