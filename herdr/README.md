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

## agents

### cursor
1. Install Cursor and sign in

```bash
curl https://cursor.com/install -fsS | bash
```

2. Ask Cursor to explain your codebase
> Explain this codebase. Point me to the main entry points, key modules, and anything I should read before making changes.

```bash
cursor-agent
```


3. Make one small change
> Suggest three small, safe improvements in this codebase. Explain the tradeoffs and wait for me to choose one.


4. Review the diff and verify the result


https://cursor.com/docs/get-started/quickstart


### hermes

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
#sudo is needed ONLY to install build tools (build-essential, python3-dev, libffi-dev) via apt.
```

https://hermes-agent.nousresearch.com/docs/

### pi

```bash
curl -fsSL https://pi.dev/install.sh | sh
```

* https://pi.dev/docs/latest
* https://pi.dev/docs/latest/providers


## Reference
https://herdr.dev/


