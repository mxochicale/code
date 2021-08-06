# Anaconda [:link:](https://www.anaconda.com/)

## Installation in Ubuntu 18.04, 20.04
In the terminal, enter: bash [download-installation.sh](download-installation.sh):
```
bash download-installation.bash
```

## Deactivate/actiavet conda base

Comment and uncomment the following lines in `.bashrc`:

```

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/mx19/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/mx19/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/mx19/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/mx19/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<



```




