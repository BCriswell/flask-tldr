# -*- mode: ruby -*-
# vi: set ft=ruby :

$setup = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get update
SCRIPT

$dependencies = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql libpq-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev python3-dev libjpeg-dev zlib1g-dev build-essential git wget
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-virtualenv virtualenvwrapper
SCRIPT

unless Vagrant.has_plugin?("vagrant-vbguest")
 raise "Please install the vagrant-vbguest plugin by running `vagrant plugin install vagrant-vbguest`"
end

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Using Vagrant Cloud
  # https://vagrantcloud.com/ubuntu/trusty64
  config.vm.box = "ubuntu/trusty64"
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end
  config.vm.hostname = "web"
  config.ssh.private_key_path = ['~/.vagrant.d/insecure_private_key', '~/.ssh/id_rsa']

  # workaround to get vagrant 1.7+ to play nice with ansible ssh
  config.ssh.insert_key = false


  # config.ssh.forward_agent = true
  config.vm.network "private_network", ip: "192.168.88.99"
  config.vm.network :forwarded_port, guest: 80, host: 8080, id: "nginx"
  config.vm.network :forwarded_port, guest: 5000, host: 5000, id: "flask"
  # config.vm.network :forwarded_port, guest: 4567, host: 4567, id: "redmon"
  # config.vm.network :forwarded_port, guest: 8000, host: 8000, id: "django"
  # config.vm.network :forwarded_port, guest: 15672, host: 15672, id: "rabbitmq-management"
  # config.vm.network :forwarded_port, guest: 5050, host: 5050, id: "flower"
  # config.vm.network :forwarded_port, guest: 8002, host: 8002, id: "runserver"
  # config.vm.network :forwarded_port, guest: 3000, host: 3000, id: "node"

  config.vm.synced_folder ".", "/vagrant", id: "vagrant-root", disabled: true
  config.vm.synced_folder ".", "/var/www/flask/", id: "flask-root", group: "www-data", disabled: false, owner: 'vagrant', mount_options: ['dmode=775', 'fmode=775']

  config.vm.provider :virtualbox do |vb|
    vb.memory = 2048
    vb.cpus = 1
  end

  config.vm.provision "shell", inline: $setup
  config.vm.provision "shell", inline: $dependencies
end
