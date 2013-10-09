#!/usr/bin/env python

from bottle import Bottle, run, request
from bottle.ext.redis import RedisPlugin
 
app = Bottle()
plugin = RedisPlugin(host='localhost')
app.install(plugin)

@app.route('/helloiam/:key')
def hello(key, rdb):
    row = rdb.hget('pyndns-dict', key)
    if row is None or row != request.remote_addr:
        rdb.hset('pyndns-dict', key, request.remote_addr)
        rdb.publish('pyndns-chan', 'go')  # trigger update
    return "<pre>Key : {0} ; New val : {1}</pre>".format(key, request.remote_addr)

run(app, host='0.0.0.0', port=5353)
