## Ansible Mesos

Just a work-in-progress for setting up a quick vagrant and ansible based Apache Mesos and Marathon installation.

Notes:

* Hardcoded IPs based on what is in the Vagrantfile
* Assumes an apt-cacher-ng proxy

Issues:

* Aug 12 21:11:21 vagrant-ubuntu-trusty-64 marathon[23688]: [2014-08-12 21:11:21,231] INFO Proxying request to leader at mm3:8080 (mesosphere.marathon.api
* set quorum to 2 with three masters? "If quorum is 2, you should have 3 masters"
