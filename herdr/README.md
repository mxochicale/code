# herdr [#87](https://github.com/mxochicale/code/issues/87)
> Run them anywhere. Leave them running.

## Installaton
```bash
curl -fsSL https://herdr.dev/install.sh | sh
```

## Keyboard control
```
Ctrl+b ? #help
Ctrl+b v #Split right
Ctrl+b - #Split down
Ctrl+b c #New tab
Ctrl+b n #Next tab
Ctrl+b p #Previous tab
Ctrl+b q #Detach herdr client
```


* Workspaces and session:
```
Ctrl+b w #Workspace navigation
Ctrl+b shift+n #New Workspace
Ctrl+b shift+w #Rename Workspace
Ctrl+b shift+d #Close Workspace
```


## Log changes

```bash
VER=$(herdr --version | head -n1)
os=$(hostnamectl | grep "Operating System" | sed 's/.*Operating System: //')
kernel=$(hostnamectl | grep "Kernel" | sed 's/.*Kernel: //')
arch=$(hostnamectl | grep "Architecture" | sed 's/.*Architecture: //')
echo $VER $os $kernel $arch

# Append to logs.md
sed -i "/\<LOGS\>/a # $(date)\nherdr-version: ${VER}\nos: ${os}\nkernel: ${kernel}\narch: ${arch}" logs.md
cd $HOME/repositories/mxochicale/code
git commit -am "updates herdr-version $VER under $os $kernel $arch #87"
git push origin main

```

## Reference
https://herdr.dev/


