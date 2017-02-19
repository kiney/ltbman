#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import yaml
#DEBUG = os.environ.get('DEBUG') or False

#some config stuff
config = yaml.load(open('config.yaml', 'r'))
SERVER = config['server']
PORT = config['port']
URLPREFIX = config['urlprefix']
DEBUGMODE = config['debugmode']
DBURL = config['dburl']
HOST = config['host']

# neue bücher MüSSEN mit Titel gemoved werden

# Feature request von Dirk:
# Bücher in der Liste anchecken um sie moven zu können

from ltb import LtbDB

from bottle import get, post, jinja2_view, Jinja2Template, request, redirect, static_file
import bottle

app = bottle.Bottle()

ltbdb = LtbDB(DBURL)
locs = sorted(ltbdb.lid.keys())

Jinja2Template.settings = {
    'autoescape': True,
}

@app.get('/static/<filename>')
def staticfiles(filename):
    return static_file(filename, root='static')

@app.get('/')
@jinja2_view('index.j2')
def index():
    return {'pfx': URLPREFIX, 'locs': locs}

@app.get('/ltbs/all')
@jinja2_view('all.j2')
def all():
    return {'pfx': URLPREFIX, 'locs': locs, 'ltbs': ltbdb.get_all_ltbs()}

@app.get('/ltbs/lost')
@jinja2_view('lost.j2')
def all():
    return {'pfx': URLPREFIX, 'locs': locs, 'ltbs': ltbdb.get_lost_ltbs()}

@app.get('/ltbs/<loc>')
@jinja2_view('by_location.j2')
def by_location(loc):
    return {'pfx': URLPREFIX, 'locs': locs, 'ltbs': ltbdb.get_ltbs_by_location(loc), 'loc': loc}

@app.get('/moveltb/form')
@jinja2_view('moveltb_form.j2')
def moveltb_form():
    return {'pfx': URLPREFIX, 'locs': locs}

@app.post('/moveltb/move')
@jinja2_view('moveltb_result.j2')
def moveltb_form():
    ltbs = request.forms.get('ltbs')
    loc  = request.forms.get('location')
    r = ltbdb.move_ltbs(ltbs, loc)
    return {'pfx': URLPREFIX, 'locs': locs, 'r': r}

@app.get('/addltb/form')
@jinja2_view('addltb_form.j2')
def moveltb_form():
    return {'pfx': URLPREFIX, 'locs': locs}

@app.post('/addltb/add')
@jinja2_view('addltb_result.j2')
def moveltb_form():
    ltb = request.forms.get('ltb')
    loc  = request.forms.get('location')
    r = ltbdb.add_ltb(ltb, loc)
    return {'pfx': URLPREFIX, 'locs': locs}

bottle.debug(DEBUGMODE)
if __name__ == '__main__':
    #logging.basicConfig(filename='signup.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')
    app.run(host=HOST, port=PORT, server=SERVER)
