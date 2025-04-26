# docker

1. Installation

```
sudo apt update
sudo apt install docker.io
```

2. Linux post-installation steps for Docker Engine
```
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
reboot
#?chmod 777 /var/run/docker.sock
#?sudo chmod 666 /var/run/docker.sock
```

sudo systemctl start docker

