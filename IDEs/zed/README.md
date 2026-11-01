# [zed](https://zed.dev/)

> Zed is a minimal code editor crafted for speed and collaboration with humans and AI.

## Download
```bash
curl -f https://zed.dev/install.sh | sh
```


## Commit changes
```
# Extract info
VERSION=$(zed --version | awk '{printf "%s ", $2}')
os=$(hostnamectl | grep "Operating System" | sed 's/.*Operating System: //')
kernel=$(hostnamectl | grep "Kernel" | sed 's/.*Kernel: //')
arch=$(hostnamectl | grep "Architecture" | sed 's/.*Architecture: //')
echo $VERSION $os $kernel $arch


# Append to logs.log
sed -i "/\<LOGS\>/ s/$/ \n\n## $(date)\nzed-version: ${VERSION}\nos: ${os}\nkernel: ${kernel}\narch: ${arch}/" logs.log
cd $HOME/repositories/mxochicale/code
git add .
git commit -m "zed--version: ${VERSION} under ${os} ${kernel} ${arch} #00"
git push origin main
```


