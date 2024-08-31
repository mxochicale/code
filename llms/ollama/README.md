# ollama
https://github.com/ollama/ollama

## installation
curl -fsSL https://ollama.com/install.sh | sh

### Logs
```
>>> Installing ollama to /usr/local
>>> Downloading Linux amd64 bundle
######################################################################## 100.0%##O#- #                                                              ######################################################################## 100.0%
>>> Creating ollama user...
>>> Adding ollama user to render group...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
Created symlink /etc/systemd/system/default.target.wants/ollama.service → /etc/systemd/system/ollama.service.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.
```

### Usage
* Using models
```
ollama run moondream #829MB
#ollama run llama3.1:70b #40GB
```

* commands
```
ollama run moondream #829MB
>>> /?
Available Commands:
  /set            Set session variables
  /show           Show model information
  /load <model>   Load a session or model
  /save <model>   Save your current session
  /clear          Clear session context
  /bye            Exit
  /?, /help       Help for a command
  /? shortcuts    Help for keyboard shortcuts

Use """ to begin a multi-line message.
Use /path/to/file to include .jpg or .png images.

>>> /bye

```

# git_commit_ollama.sh


## References
https://github.com/ollama/ollama?tab=readme-ov-file#terminal  


