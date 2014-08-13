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
* Assumes an apt-cacher-ng proxy

###Zookeeper

* http://zookeeper.apache.org/doc/trunk/zookeeperAdmin.html#sc_administering

###Service Discovery

* http://nerds.airbnb.com/smartstack-service-discovery-cloud/

##Todo

* DONE: mesos (zookeper) + marathon
* enable cgroups in mesos
* deimos
* docker

##Issues

* set quorum to 2 with three masters? "If quorum is 2, you should have 3 masters"

##cgroup notes

After starting mesos-slave with isolation cgroups, and running a sleep process:

```bash
vagrant@ms1:~$ ps xawf -eo pid,user,cgroup,args | tail
 4121 vagrant  2:name=systemd:/user/1000.u          \_ -bash
 4178 vagrant  2:name=systemd:/user/1000.u              \_ ps xawf -eo pid,user,cgroup,args
 4179 vagrant  2:name=systemd:/user/1000.u              \_ tail
 3604 root     -                           /usr/local/sbin/mesos-slave --master=zk://10.3.0.89:2181,10.3.0.90:2181,10.3.0.91:2181/mesos --ip=10.3.0.92 --log_dir=/var/log/mesos --hostname=10.3.0.92 --isolation=cgroups
 3616 root     -                            \_ logger -p user.info -t mesos-slave[3604]
 3617 root     -                            \_ logger -p user.err -t mesos-slave[3604]
 4045 root     6:freezer:/mesos/466501fd-b  \_ sh -c /usr/local/libexec/mesos/mesos-executor
 4054 root     6:freezer:/mesos/466501fd-b      \_ /usr/local/libexec/mesos/mesos-executor
 4064 root     6:freezer:/mesos/466501fd-b          \_ sh -c sleep 600
 4065 root     6:freezer:/mesos/466501fd-b              \_ sleep 600
 ```
