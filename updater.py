#!/usr/bin/env python

import os
from time import time
import redis
from jinja2 import Template

tpl_str = open('db.myhost.tpl', 'r').read()
tpl = Template(tpl_str)

r = redis.Redis("localhost")
sub = r.pubsub()
sub.subscribe("pyndns-chan")

for item in sub.listen():
    if item["type"] == "message":
        print "new item ==>", item
        dico = r.hgetall("pyndns-dict")
        new_db = tpl.render(items=dico.items(), serial=int(time() * 100))
        db = open('/etc/bind/db.myhost', 'w')
        db.write(new_db)
        db.close()
        os.system("service bind9 restart")
