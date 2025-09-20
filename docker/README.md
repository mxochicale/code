# docker
> Docker is a platform designed to help developers build, share, and run container applications. We handle the tedious setup, so you can focus on the code.
https://en.wikipedia.org/wiki/Docker_(software)

0. Clean your system to uninstall all conflicting packages:
```
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

1. Installation
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Install the Docker packages.
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

2. Linux post-installation steps for Docker Engine
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

3. Verify Docker
```bash

sudo service docker status
sudo docker run hello-world
sudo docker pull hello-world

```

4. Useful commands

* Clean up the container images:
```bash
docker system prune -f --volumes
docker images --format '{{.Repository}}:{{.Tag}}' | grep '^vsc-holohub' | xargs -r docker rmi
```

```
docker images
docker ps
docker attach <ID>
docker stop <ID>
docker rename keen_einstein mycontainer
docker rmi --force <ID>

docker stop $(docker ps -a -q)
docker system prune -f --volumes #clean unused systems
```

* Restart
```bash
sudo systemctl start docker
```

## Notes
* The unofficial packages to uninstall are:
```
docker.io
docker-compose
docker-compose-v2
docker-doc
podman-docker
```
https://docs.docker.com/engine/install/ubuntu/



* Drafts
```
reboot
#?chmod 777 /var/run/docker.sock
#?sudo chmod 666 /var/run/docker.sock
```
