# llm
https://github.com/simonw/llm


## Installation in Ubuntu 20.04
```
conda create -n "eVE" python=3.12 pip -c conda-forge
conda activate eVE
pip install llm
llm install llm-gpt4all

llm -m orca-mini-3b-gguf2-q4_0 'What is the capital of France?'
llm chat -m gpt-4o-mini

#OSError: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.32' not found (required by ~/envs/eVE/lib/python3.12/site-packages/gpt4all/llmodel_DO_NOT_MODIFY/build/libllmodel.so)
```



