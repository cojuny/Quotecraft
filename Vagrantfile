Vagrant.configure("2") do |config|
    config.hostmanager.enabled = true 
    config.hostmanager.manage_host = true

  ### DB vm  ####
    config.vm.define "db01" do |db01|
      db01.vm.box = "geerlingguy/centos7"
      db01.vm.hostname = "db01"
      db01.vm.network "private_network", ip: "192.168.56.15"
      db01.vm.synced_folder "./src/resources/sql", "/home/vagrant"
    end
  end