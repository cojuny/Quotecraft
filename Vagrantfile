Vagrant.configure("2") do |config|
  config.vagrant.plugins = [{"vagrant-vbguest" => {"version" => "0.21.0"}}, "vagrant-hostmanager", "vagrant-scp"]
    config.hostmanager.enabled = true 
    config.hostmanager.manage_host = true
    

  ### DB vm  ###
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

  ### Memcache vm  ###
  config.vm.define "mc01" do |mc01|
    mc01.vm.box = "centos/7"
    mc01.vm.hostname = "mc01"
    mc01.vbguest.auto_update = true
    mc01.vm.network "private_network", ip: "192.168.56.14"
    mc01.vm.provision "shell", path: "provisioning/shell/memcache.sh"  
  end
  
  ### Django vm 1 ###
  config.vm.define "dj01" do |dj01|
    dj01.vm.box = "hashicorp/bionic64"
    dj01.vm.hostname = "dj01"
    dj01.vm.network "private_network", ip: "192.168.56.16"
    dj01.vbguest.auto_update = true
    dj01.vm.synced_folder "./src", "/src"
    dj01.vm.synced_folder "provisioning/resources/django", "/vagrant"
    dj01.vm.provision "shell", path: "provisioning/shell/django.sh" 
    dj01.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
    dj01.vm.provision "shell", run: "always", inline: "sudo systemctl start quotecraft.service"
  end

  ### Django vm 2 ###
  config.vm.define "dj02" do |dj02|
    dj02.vm.box = "hashicorp/bionic64"
    dj02.vm.hostname = "dj02"
    dj02.vm.network "private_network", ip: "192.168.56.17"
    dj02.vbguest.auto_update = true
    dj02.vm.synced_folder "./src", "/src"
    dj02.vm.synced_folder "provisioning/resources/django", "/vagrant"
    dj02.vm.provision "shell", path: "provisioning/shell/django.sh" 
    dj02.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
    dj02.vm.provision "shell", run: "always", inline: "sudo systemctl start quotecraft.service"

  end

  ### Nginx VM ###
  config.vm.define "ngx01" do |ngx01|
    ngx01.vm.box = "ubuntu/xenial64"
    ngx01.vm.hostname = "ngx01"
    ngx01.vm.network "private_network", ip: "192.168.56.10"
    ngx01.vm.network "forwarded_port", guest: 80, host: 8080
    ngx01.vm.provision "shell", path: "provisioning/shell/nginx.sh"  
  end

end