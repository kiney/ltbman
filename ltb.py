#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import records
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

