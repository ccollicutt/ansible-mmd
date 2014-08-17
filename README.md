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
* provisioning w openstack (see [this](https://github.com/lukaspustina/dynamic-inventory-for-ansible-with-openstack/blob/master/openstack_inventory.py))

##Issues

* set quorum to 2 with three masters? "If quorum is 2, you should have 3 masters"
