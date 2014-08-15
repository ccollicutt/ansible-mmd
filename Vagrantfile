# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

boxes = [
    {
        :name => :mm1,
        :pubip => '192.168.34.89',
        :privip => '10.3.0.89',
        :box => 'trusty64',
        :vbox_config => [
            { '--memory' => '1536' }
        ],
    },    {
        :name => :mm2,
        :pubip => '192.168.34.90',
        :privip => '10.3.0.90',
        :box => 'trusty64',
        :vbox_config => [
            { '--memory' => '1536' }
        ],
    },  {
        :name => :mm3,
        :pubip => '192.168.34.91',
        :privip => '10.3.0.91',
        :box => 'trusty64',
        :vbox_config => [
            { '--memory' => '1536' }
        ],
    }, {
        :name => :ms1,
        :pubip => '192.168.34.92',
        :privip => '10.3.0.92',
        :box => 'trusty64',
        :vbox_config => [
            { '--memory' => '1536' }
        ],
    }, {
        :name => :ms2,
        :pubip => '192.168.34.93',
        :privip => '10.3.0.93',
        :box => 'trusty64',
        :vbox_config => [
            { '--memory' => '1536' }
        ],
    },
    {
      :name => :ms3,
      :pubip => '192.168.34.94',
      :privip => '10.3.0.94',
      :box => 'trusty64',
      :vbox_config => [
          { '--memory' => '1536' }
      ],
  },
]

Vagrant.configure("2") do |config|

    boxes.each do |opts|
        config.vm.define opts[:name] do |config|
            # Box basics
            config.vm.hostname = opts[:name]
            config.vm.box = opts[:box]
            config.vm.box_url = opts[:box_url]
            config.vm.network :private_network, ip: opts[:pubip]
            config.vm.network :private_network, ip: opts[:privip]
            config.ssh.forward_agent = true

            # VirtualBox customizations
            unless opts[:vbox_config].nil?
                config.vm.provider :virtualbox do |vb|

                    # vboxmanage
                    opts[:vbox_config].each do |hash|
                        hash.each do |key, value|
                            vb.customize ['modifyvm', :id, key, value]
                        end
                    end
                end
            end
    end



    end
end
