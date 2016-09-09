#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ausprobiert... erstmal cool, aber suckt überlst bei multi-statments, transactions gehen garnicht
# außer vllt. mit einerm dieser kickass pull-requests:
# https://github.com/kennethreitz/records/pull/58
# https://github.com/kennethreitz/records/pull/75
import records
#import sqlalchemy
import enum


LOC = enum.Enum('Location', 'unknown Hannover Marburg Harz')


class LTB():
    '''
    LTB class
    '''
    def __init__(self, nr, title, present=False, location=LOC.unknown)

class LtbDB():
    '''
    database interface class
    '''
    def __init__(self):
        print('TODO')

