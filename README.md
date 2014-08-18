# Ansible MMDD - Mesos, Marathon, Deimos and Docker

A work-in-progress for setting up a quick vagrant and ansible based apache mesos and marathon installation.

The masters run:

* zookeeper
* mesos-master
* marathon

The slaves run:

* mesos-slave

##Notes

* Hardcoded IPs based on what is in the Vagrantfile
* Assumes an apt-cacher-ng proxycd

##Todo

* DONE: mesos (zookeeper) + marathon
* DONE: enable cgroups in mesos
* Marathon authentication? (And marathon authenticate to mesos?) - "--http_credentials user:pass"
* deimos
* docker
* http server to grab zip files from to launch applications?
* create system in openstack environment

##OpenStack

If you are creating instances using OpenStack instead of Vagrant, then there is a nova.py inventory script to use.

This will require a nova.ini file that is filled out with your OpenStack credentials. You can use the nova.ini.example file to fill it out, then copy that file to nova.ini. The nova.py script will use it.

###Ssh proxy

Ensure netcat-tradititional is installed on the openstack-gw (assuming it's Ubuntu 14.04).

```bash
host openstack-gw
   Hostname some.public.ip
   User ubuntu
# Where 10.2.*.* is your tenant/project private ip space
host 10.2.*.*
   ProxyCommand ssh -q rac-gw netcat %h 22
```

##Issues

* set quorum to 2 with three masters? "If quorum is 2, you should have 3 masters"
