#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# records is missing native transaction support, there are pulll-requests:
# https://github.com/kennethreitz/records/pull/58
# https://github.com/kennethreitz/records/pull/75
# atm there ltbman uses a local fork based on pr75
# i guess all of this is not really thread safe!
import records
#import sqlalchemy
import time


class LtbDB():
    '''
    database abstraction class
    '''
    def __init__(self, dburl):
        self._dburl = dburl
        self.db = records.Database(self._dburl) # db handle, only for reading because of thread saferty
        self.init_location_ids()
    
    def init_location_ids(self):
        '''
        create location mappings for fast lookup
        (forward and backward)
        '''
        lid = {} # name -> id
        rlid = {} # id -> name
        r = self.db.query('SELECT id, name FROM locations;')
        for i in r:
            rlid[i[0]] = i[1]
            lid[i[1]] = i[0]
        self.lid = lid
        self.rlid = rlid
    
    def get_stats(self):
        '''
        return some general stats for the index page
        '''
        #TODO
        return {}
    
    def get_ltb_by_id(self, ltbid):
        q ='''SELECT ltbs.ltbid, ltbs.title, locations.name AS location, ltbs.dupes, ltbs.present
FROM ltbs
INNER JOIN locations ON ltbs.location = locations.id
WHERE ltbs.ltbid = :ltbid;
'''
        ltb = self.db.query(q, ltbid = ltbid)[0].as_dict()
        return ltb
    
    def get_all_ltbs(self):
        q = '''SELECT ltbs.ltbid, ltbs.title, locations.name AS location, ltbs.present
FROM ltbs
INNER JOIN locations ON ltbs.location = locations.id'''
        a = self.db.query(q)
        ltbs = list(map(dict, list(a)))
        return ltbs
    
    def get_lost_ltbs(self):
        q = '''SELECT ltbs.ltbid, ltbs.title, locations.name AS location, ltbs.present
FROM ltbs
INNER JOIN locations ON ltbs.location = locations.id
WHERE locations.id = 0 AND ltbs.present = 1'''
        a = self.db.query(q)
        ltbs = list(map(dict, list(a)))
        return ltbs
    
    def get_ltbs_by_location(self, loc):
        q = '''SELECT ltbs.ltbid, ltbs.title, locations.name AS location, ltbs.present
FROM ltbs
INNER JOIN locations ON ltbs.location = locations.id
WHERE locations.id = :loc;'''
        if isinstance(loc, str):
            loc = self.lid[loc]
        a = self.db.query(q, loc=loc)
        ltbs = list(map(dict, list(a)))
        return ltbs

    def move_ltbs(self, ltbs, loc):
        '''
        move one or more LTB to dest
        
        ltbs can be either an array of numbers or a space seperated string
        return: list of whats been done
        '''
        if isinstance(loc, str):
            loc = self.lid[loc]
        if isinstance(ltbs, str):
            ltbs = map(int, ltbs.split())
        result = {'moved': [], 'failed': []} # collect books that are not updated
        db = records.Database(self._dburl) #local db handle for thread-safety
        #db = self.db
        q = '''UPDATE ltbs
SET location = :loc
WHERE ltbid = :ltbid'''
        #TODO correct moves table in db.sql
        q2 = 'INSERT INTO moves (ltbid, OldLocation, NewLocation) VALUES (:ltbid, :old, :new);'
        q3 = 'SELECT location FROM ltbs where ltbid=:ltbid;'
        with db.transaction():
            for ltb in ltbs:
                oldloc = db.query(q3, ltbid = ltb)[0][0]
                r = db.query(q, ltbid = ltb, loc = loc)
                #TODO check if prestent
                #check if ltb is int
                if db.rowcount == 0:
                    result['failed'].append(ltb)
                elif db.rowcount == 1:
                    result['moved'].append(ltb)
                    db.query(q2, ltbid = ltb, old = oldloc, new = loc)
                else:
                    raise RuntimeError('Mehr als ein LTB angefasst. BUG!')
        return result
        

if __name__ == '__main__':
    '''
    ignore this section
    just testing stuff...
    '''
    DBURL = 'sqlite:///ltb.db'
    l = LtbDB(DBURL)
    #print(l.lid)
    #print(l.rlid)
    print(l.get_ltb_by_id(132))
    #print(l.move_ltbs('132 134 145 870', 1))
    #print(l.get_ltb_by_id(132))
    #print(l.get_ltbs_by_location('Hannover'))
    #print(l.get_all_ltbs())
