#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#some config stuff
SERVER = 'wsgiref'
URLPREFIX = 'http://localhost:8080'
DEBUGMODE = True
DBURL = 'sqlite:///ltb.db'

# neue bücher MüSSEN mit Titel gemoved werden

# Feature request von Dirk:
# Bücher in der Liste anchecken um sie moven zu können

# css class definitionen

from ltb import LtbDB

from bottle import get, post, jinja2_view, Jinja2Template, request, redirect, static_file
import bottle

ltbdb = LtbDB(DBURL)
locs = sorted(ltbdb.lid.keys())

Jinja2Template.settings = {
    'autoescape': True,
}

@get('/static/<filename>')
def staticfiles(filename):
    return static_file(filename, root='static')

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
    return {'pfx': URLPREFIX, 'locs': locs}

@post('/moveltb/move')
@jinja2_view('moveltb_result.j2')
def moveltb_form():
    ltbs = request.forms.get('ltbs')
    loc  = request.forms.get('location')
    r = ltbdb.move_ltbs(ltbs, loc) #TODO location
    return {'pfx': URLPREFIX, 'locs': locs, 'r': r}


if __name__ == '__main__':
    #logging.basicConfig(filename='signup.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')
    bottle.debug(DEBUGMODE)
    bottle.run(host='127.0.0.1', port=8080, server=SERVER)
