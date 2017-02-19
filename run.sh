#!/bin/sh
# copy ltb.db.example wenn es noch nicht /var/... existiert
# config?
if [ ! -e /var/lib/ltbman/ltb.db ]
then
    cp /opt/ltbman/ltb.db.example /var/lib/ltbman/ltb.db
fi

chown ltbman:ltbman /var/lib/ltbman/ltb.db
#chmod 0600 /var/lib/ltbman/ltb.db

# for n cores use 2n+1 workers
cd /opt/ltbman
cp config.yaml.example config.yaml
su ltbman -c "gunicorn -w $(expr $(nproc) \* 2 + 1) -b :8080 index:app"
