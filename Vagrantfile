# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION="2"
PROJECT_NAME="projectdemo"
DJANGO_ENV="local"

REQUIRED_PLUGINS = [
  "vagrant-hostmanager",
  "vagrant-fsnotify",
  "vagrant-vbguest",
]

# Install automatically vagrant plugins
uninstalled_required_plugins = REQUIRED_PLUGINS.reject(&Vagrant.method(:has_plugin?))
if ! uninstalled_required_plugins.empty? && ARGV.first != "plugin"
  exec "vagrant plugin install '#{uninstalled_required_plugins.join("' '")}' && vagrant '#{ARGV.join("' '")}'"
end

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.box_check_update = false

    # Appengine dev server does not detect very well modified files from the host machine.
    # The plugin vagrant-fsnotify passes file events from host to guest machine.
    # In general the app engine dev server is a bit slow.
    # config.vm.synced_folder "project", "/home/vagrant/project"
    config.vm.synced_folder "projectdemo", "/home/vagrant/project", nfs: true, fsnotify: true, exclude: ["vendor", "node_modules", ".pyc"]
    config.vm.post_up_message = "IMPORTANT: You should run `vagrant fsnotify' on a separate terminal to enable auto-reloading features."

    # Network config
    config.hostmanager.enabled = true
    config.hostmanager.manage_host = true
    config.hostmanager.ignore_private_ip = false
    config.hostmanager.include_offline = true
    config.vm.define 'wagtailgaedemo-wagtail-v1' do |node|

        node.vm.hostname = 'wagtailgaedemo.dev'
        node.hostmanager.aliases = []
        node.vm.network :private_network, ip: '192.168.5.10'

        config.vm.network "forwarded_port", guest: 8080, host: 8080 # django
        config.vm.network "forwarded_port", guest: 3306, host: 13306 # mysql
        config.vm.network "forwarded_port", guest: 1080, host: 1088 # webmail
    end

    # Add memory
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "2048"]
    end

    # provision
    config.vm.provision :shell, :path => "vagrant/provision/ubuntu.sh"
    config.vm.provision :shell, :path => "vagrant/provision/mysql.sh", :args => [PROJECT_NAME]
    config.vm.provision :shell, :path => "vagrant/provision/python.sh", :args => [PROJECT_NAME, DJANGO_ENV]
    config.vm.provision :shell, :path => "vagrant/provision/gcloud_sdk.sh"
end