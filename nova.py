#!/usr/bin/env python

import sys
import re
import os
import ConfigParser
from novaclient import client as nova_client

try:
    import json
except:
    import simplejson as json

def nova_load_config_file():
    p = ConfigParser.SafeConfigParser()
    path1 = os.getcwd() + "/nova.ini"
    path2 = os.path.expanduser(os.environ.get('ANSIBLE_CONFIG', "~/nova.ini"))
    path3 = "/etc/ansible/nova.ini"

    if os.path.exists(path1):
        p.read(path1)
    elif os.path.exists(path2):
        p.read(path2)
    elif os.path.exists(path3):
        p.read(path3)
    else:
        return None
    return p


def add_meta(vm_name, inventory, group, ip):

    if not vm_name in inventory[group]:
      inventory[group]['hosts'].append(vm_name)

    if not vm_name in inventory['_meta']:
        inventory['_meta']['hostvars'][vm_name] = {}
        inventory['_meta']['hostvars'][vm_name]['ansible_ssh_host'] = ip

################################################################################
#
# MAIN
#
################################################################################

config = nova_load_config_file()

client = nova_client.Client(
    version     = config.get('openstack', 'version'),
    username    = config.get('openstack', 'username'),
    api_key     = config.get('openstack', 'api_key'),
    auth_url    = config.get('openstack', 'auth_url'),
    region_name = config.get('openstack', 'region_name'),
    project_id  = config.get('openstack', 'project_id'),
    auth_system = config.get('openstack', 'auth_system')
)

groups = [ 'undefined']
inventory = {}
inventory['_meta'] = {}
inventory['_meta']['hostvars'] = {}

for group in groups:
    if not group in inventory:
        inventory[group] = {
          'hosts' : [],
        }

if len(sys.argv) == 2 and (sys.argv[1] == '--list'):
    groups = {}

    # Cycle on servers
    for f in client.servers.list():

      private = [ x['addr'] for x in getattr(f, 'addresses').itervalues().next()
       if x['OS-EXT-IPS:type'] == 'fixed' ]

      public  = [ x['addr'] for x in getattr(f, 'addresses').itervalues().next()
        if x['OS-EXT-IPS:type'] == 'floating']

      # Define group (or set to empty string)
      group = f.metadata['group'] if f.metadata.has_key('group') else 'undefined'

      # Create group if not exist
      if group not in groups:
          groups[group] = []

      if public:
          # just take the first ip
          ip = public[0]
          if len(ip) < 16:
            add_meta(f.name, inventory, group, ip)
            continue

      if private:
          ip = private[0]
          if len(ip) < 16:
            add_meta(f.name, inventory, group, ip)
            continue

    # Return server list
    print json.dumps(inventory)
    sys.exit(0)

else:
    print "usage: --list"
    sys.exit(1)
