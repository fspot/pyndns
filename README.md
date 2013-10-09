pyndns
======

My personal, minimalist, quick and dirty dyndns-like.

Most of things are hard coded so you can't use this without any change !

Installation
------------

Needs some python libs :

    $ pip install bottle redis bottle-redis jinja2

In my case, needs also bind9 and redis-server running and well-configured, a /etc/bind/db.myhost zone file, etc.

As root (or other privileged user), launch :

    $ python updater.py  # needs some privileges to write in /etc/bind/db.myhost and to restart bind9

And as non-root, launch :

    $ python app.py      # will launch a webapp on port 5353

Usage
-----

Suppose you make this request from a computer which public address is 1.2.3.4 :

    $ curl http://myhost.com:5353/helloiam/luc

So, now :

    $ dig luc.myhost.com
    
...should return 1.2.3.4 !

Issues
------

What if someone spams http://myhost.com:5353/helloiam/XXX ? Redis gets full, bind9 restarts again and again... definitely bad.
