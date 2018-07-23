descript:
A python script to start up a linux-servic(memcached).
This script replace origin shell script with memcached and can also be a template to other linux service's rc script.
rc_memcached1.py : origin version, error ouccurs when using 'start' parameter two consecutive times.
rc_memcached2.py : modify rc_memcached1.py's error
rc_memcached.py : final version, daemon

usage:
python [rc_memcached1.py|rc_memcached2.py|rc_memcached.py] [start|status|stop|restart]

need:
python 2.7
yum install -y memcached