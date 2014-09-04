##Mesos

* https://mesosphere.io/docs/deep-dive/mesos-slave/

work_dir is /tmp/mesos by default, eg.

```bash
vagrant@ms2:/tmp/mesos/slaves/20140813-233541-1493173002-5050-1380-1/frameworks/20140812-191817-1526727434-5050-12744-0000/executors/py-http2.82f917c0-2400-11e4-9b9c-0800272ca238/runs/latest$
```

##Marathon

* Docs: https://mesosphere.github.io/marathon/docs/

* Lots of options show here: https://github.com/mdsol/marathon_cookbook
* Examples: https://github.com/mesosphere/marathon/tree/master/examples
* With Play: http://typesafe.com/blog/play-framework-grid-deployment-with-mesos

###Commands

Check what host is master?

```bash
curtis$ ansible -m shell -a "mesos-resolve zk://localhost:2181/mesos" -i shooz.py mesos_masters
```

###Example application

```bash
{
  "id": "http",
  "cmd": "python -m SimpleHTTPServer $PORT",
  "mem": 50,
  "cpus": 0.1,
  "instances": 1,
  "constraints": [
    ["hostname", "UNIQUE"]
  ]
}
```

curl -i -H 'Content-Type: application/json' -d @example.json localhost:8080/v2/apps

From the master, run something like:

```bash
root@mm2:~# curl -i -H 'Content-Type: application/json' -d @example.json localhost:8080/v2/apps
HTTP/1.1 201 Created
Location: http://localhost:8080/v2/apps/http
Content-Type: application/json
Transfer-Encoding: chunked
Server: Jetty(8.y.z-SNAPSHOT)

nullroot@mm2:~#
```

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

##Mesos-slaves

```bash
Aug 20 21:49:45 mm2 mesos-master[8937]: W0820 21:49:45.139228  8957 master.cpp:2745] Shutting down slave 20140820-205713-2130706954-5050-8937-59 at slave(1)@10.2.0.160:5051 (10.2.0.160) with message 'health check timed out'
```

##Zookeeper

* http://zookeeper.apache.org/doc/trunk/zookeeperAdmin.html#sc_administering

###Commands

```bash
ubuntu@mm2:~$ echo stat | nc localhost 2181
Zookeeper version: 3.4.5--1, built on 06/10/2013 17:26 GMT
Clients:
 /10.2.1.32:58425[1](queued=0,recved=81,sent=81)
 /127.0.0.1:39108[0](queued=0,recved=1,sent=0)
 /10.2.1.32:58424[1](queued=0,recved=80,sent=80)

Latency min/avg/max: 0/0/16
Received: 167
Sent: 166
Connections: 3
Outstanding: 0
Zxid: 0x87
Mode: standalone
Node count: 11
```

###zkCli.sh

```bash
root@mm2:/home/ubuntu# /usr/share/zookeeper/bin/zkCli.sh
Connecting to localhost:2181
Welcome to ZooKeeper!
JLine support is enabled

WATCHER::

WatchedEvent state:SyncConnected type:None path:null
[zk: localhost:2181(CONNECTED) 0] help
ZooKeeper -server host:port cmd args
	connect host:port
	get path [watch]
	ls path [watch]
	set path data [version]
	rmr path
	delquota [-n|-b] path
	quit
	printwatches on|off
	create [-s] [-e] path data acl
	stat path [watch]
	close
	ls2 path [watch]
	history
	listquota path
	setAcl path acl
	getAcl path
	sync path
	redo cmdno
	addauth scheme auth
	delete path [version]
	setquota -n|-b val path
```

##Service Discovery

* http://nerds.airbnb.com/smartstack-service-discovery-cloud/
