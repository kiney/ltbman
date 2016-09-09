#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import records

FN = 'LtbListe.txt'
BN = 395 #data format changed slightly after this number
LN = 484 #last number, stop parser
#LOC = enum.Enum('Location', 'unknown Hannover Marburg Harz')
GLOC = {'XO': 0, 'NO': 0, 'BO': 1, 'MO': 2, 'HO': 3}

DB = 'ltb.db'

def get_from_file(fn):
    ltbs = []
    f = open(fn, 'r')
    for l in f:
        ll = l.split()
        try:
            nr = int(ll[1])
        except (ValueError, IndexError):
            print('invalid line!')
            break
        if nr <= 395:
            title = ' '.join(ll[2:-4])
        else:
            title = ' '.join(ll[2:])
        loc = ll[0]
        if len(loc) > 2:
            dupe = 1
        else:
            dupe = 0
        present = 1
        if loc.startswith('NO'):
            present = 0
        nloc = GLOC[loc[:2]]
        #print(nloc)
        #print(nr)
        #print(title)
        ltbs.append({'ltbid': nr, 'title': title, 'location': nloc, 'present': present, 'dupes': dupe})
    return ltbs

def push_books_to_db(db, ltbs):
    '''
    db: records db handle
    '''
    tx = db.db.begin()
    for ltb in ltbs:
        print(ltb['ltbid'])
        db.query('INSERT INTO `ltbs`(`ltbid`,`title`,`present`,`location`, `dupes`) VALUES (:i,:t,:p,:l,:d);',
            i =  ltb['ltbid'], t = ltb['title'], p = ltb['present'],
            l = ltb['location'], d = ltb['dupes'])
    tx.commit()


if __name__=='__main__':
    ltbs = get_from_file(FN)
    db = records.Database('sqlite:///%s'%(DB))
    push_books_to_db(db, ltbs)
    #print(ltbs)
    print('done!')
