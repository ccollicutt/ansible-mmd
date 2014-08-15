##Mesos

* https://mesosphere.io/docs/deep-dive/mesos-slave/

work_dir is /tmp/mesos by default, eg.

```bash
vagrant@ms2:/tmp/mesos/slaves/20140813-233541-1493173002-5050-1380-1/frameworks/20140812-191817-1526727434-5050-12744-0000/executors/py-http2.82f917c0-2400-11e4-9b9c-0800272ca238/runs/latest$
```

##Marathon

* Lots of options show here: https://github.com/mdsol/marathon_cookbook
* Examples: https://github.com/mesosphere/marathon/tree/master/examples
* With Play: http://typesafe.com/blog/play-framework-grid-deployment-with-mesos

###Launching tasks

Apparently can use mesos-execute?

```bash
mesos-execute --master="127.0.1.1:5050" --name="foobar" --command="sleep 5"
```

Launch a simple python http server, use this as the command.

```bash
python -m SimpleHTTPServer $PORT
```

###cgroup notes

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

 And...

 ```bash
 vagrant@ms1:~$ cat /proc/4204/cgroup
6:freezer:/mesos/3942c250-3d15-4984-9210-a93a280a35bb
5:memory:/mesos/3942c250-3d15-4984-9210-a93a280a35bb
4:cpuacct:/mesos/3942c250-3d15-4984-9210-a93a280a35bb
3:cpu:/mesos/3942c250-3d15-4984-9210-a93a280a35bb
2:name=systemd:/
```

##Zookeeper

* http://zookeeper.apache.org/doc/trunk/zookeeperAdmin.html#sc_administering

##Service Discovery

* http://nerds.airbnb.com/smartstack-service-discovery-cloud/
