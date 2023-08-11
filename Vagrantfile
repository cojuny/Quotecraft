Vagrant.configure("2") do |config|
  config.vagrant.plugins = [{"vagrant-vbguest" => {"version" => "0.21.0"}}, "vagrant-hostmanager"]
    config.hostmanager.enabled = true 
    config.hostmanager.manage_host = true
    

  ### DB vm  ####
  config.vm.define "db01" do |db01|
    db01.vm.box = "centos/7"
    db01.vm.hostname = "db01"
    db01.vm.network "private_network", ip: "192.168.56.15"
    db01.vbguest.auto_update = true
    db01.vm.synced_folder "./provisioning/resources/sql", "/vagrant"
    db01.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
    db01.vm.provision "shell", path: "provisioning/shell/db.sh"
  end

  ### Memcache vm  #### 
  config.vm.define "mc01" do |mc01|
    mc01.vm.box = "centos/7"
    mc01.vm.hostname = "mc01"
    mc01.vm.network "private_network", ip: "192.168.56.14"
    mc01.vm.provision "shell", path: "provisioning/shell/memcache.sh"  
  end
  
  ### RabbitMQ vm  ####
    config.vm.define "rmq01" do |rmq01|
      rmq01.vm.box = "centos/7"
      rmq01.vm.hostname = "rmq01"
      rmq01.vm.network "private_network", ip: "192.168.56.16"
      rmq01.vm.synced_folder "./provisioning/resources/rmq", "/vagrant"
      rmq01.vm.provision "shell", path: "provisioning/shell/rmq.sh"  
    end
end