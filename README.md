cisco-test
==========

This thing I gotta do.  If you don't know, don't worry about it.

That previous line is there for the rest of GitHub.  If you continue
reading, it is assumed you are one of the people at Cisco evaluating
this.

thing.py
--------

I decided to write this in Python 3 because I figured it was about
time I start getting used to typing print() with parentheses.

Get your API key from https://macaddress.io/ .  Registration is free
if you don't have one already.  This gives you 1000 lookups a day for
free.  In order to avoid someone getting charged for using too many
lookups in a day, every user will need their own API key.

Store your API key in your home directory.

```
cat <<EOF>~/.macaddress.io.key
0123456789abcdef0123456789abcdef
EOF
```

Now you can query a MAC address and, using the API, you get the vendor
that manufactured the NIC.  You can send just the first three octets,
according to the API documentation.  Also, the API accepts any
delimiter between octets, or none at all.

Dockerfile
----------

This is the first time I've written a Dockerfile.  I hope you like it.

Just run `docker build .` in the project directory.  Then you'll get a
new Docker image when you run `docker images`.  It won't have a name,
but it will have a hash.  Then you can run `docker run <hash>`.  When
I did this it spewed messages about not opening TTYs.  Speaking of
TTYs, you won't get the use of your back, so fire up another terminal
(or screen/tmux window) and run `docker ps` and identify your
instance, then run `docker exec -it <container-id> /bin/sh`.  You
should get a shell in the container and you can configure your API key
(in root's home directory) and run thing.py.
