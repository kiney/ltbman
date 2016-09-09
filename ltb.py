#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# records is missing native transaction support, there are pulll-requests:
# https://github.com/kennethreitz/records/pull/58
# https://github.com/kennethreitz/records/pull/75
# work-around:
# tx = db.db.begin() / tx.commit()
# i guess all of this is not really thread safe!
import records
#import sqlalchemy
import enum


#LOC = enum.Enum('Location', 'unknown Hannover Marburg Harz')
DBURL = 'sqlite:///ltb.db'


#class LTB(): # FIXME useful?
    #'''
    #LTB class
    #'''
    #def __init__(self, nr, title, present=False, location=0):
        #pass

class LtbDB():
    '''
    database interface class
    '''
    def __init__(self, dburl=DBURL):
        self._dburl = dburl
        self.db = records.Database(dburl) # db handle, only for reading because of thread saferty
        self.init_location_ids()
    
    def init_location_ids(self):
        '''
        create location mappings for fast lookup
        (forward and backward)
        '''
        lid = {}
        rlid = {}
        r = self.db.query('SELECT id, name FROM locations;')
        for i in r:
            lid[i[0]] = i[1]
            rlid[i[1]] = i[0]
        self.lid = lid
        self.rlid = rlid
    
    def get_ltb_by_id(self, ltbid):
        q ='''SELECT ltbs.ltbid, ltbs.title, locations.name AS location, ltbs.dupes, ltbs.present
FROM ltbs
INNER JOIN locations ON ltbs.location = locations.id
WHERE ltbs.ltbid = :ltbid;
'''
        ltb = self.db.query(q, ltbid = ltbid)[0].as_dict()
        return ltb
    
    def get_all_ltbs(self):
        q = '''SELECT ltbs.ltbid, ltbs.title, locations.name AS location
FROM ltbs
INNER JOIN locations ON ltbs.location = locations.id'''
        a = self.db.query(q)
        ltbs = list(map(dict, list(a)))
        return ltbs
        

if __name__ == '__main__':
    l = LtbDB(DBURL)
    print(l.lid)
    print(l.rlid)
    print(l.get_ltb_by_id(256))
    #print(l.get_all_ltbs())
