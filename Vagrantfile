Vagrant.configure("2") do |config|
    config.hostmanager.enabled = true 
    config.hostmanager.manage_host = true

  ### DB vm  ####
    config.vm.define "db01" do |db01|
      db01.vm.box = "centos/7"
      db01.vm.hostname = "db01"
      db01.vm.network "private_network", ip: "192.168.56.15"
      db01.vbguest.installer_hooks[:before_install] = ["yum install -y epel-release", "sleep 1"]
      db01.vbguest.installer_options = { allow_kernel_upgrade: false , enablerepo: true }
      db01.vm.synced_folder "./src/resources/sql", "/home/vagrant"
      db01.vm.provider "virtualbox" do |vb|
        vb.memory = "600"
    end
  end