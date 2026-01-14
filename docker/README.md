# docker [#51](https://github.com/mxochicale/code/issues/51)  
> Docker is a platform designed to help developers build, share, and run container applications. We handle the tedious setup, so you can focus on the code.
https://en.wikipedia.org/wiki/Docker_(software)

0. Clean your system to uninstall all conflicting packages:
```
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

1. Installation
```bash
bash install-docker.bash
```

2. Linux post-installation steps for Docker Engine
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

2.1. `ERROR: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock` 
```bash
#Head "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied
sudo chown $USER:$USER /var/run/docker.sock #Solution 3: Change socket permissions (Less secure)
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


## Commit changes
```
export V=$(docker --version | awk '{print $3 $4 $5}')
echo $V
sed -i "/\<logs\>/ s/$/ \n \n## $(date) \ndocker-version: $V/" logs.md #insert date and version
git commit -am "docker $V #51"
git push origin main
```


