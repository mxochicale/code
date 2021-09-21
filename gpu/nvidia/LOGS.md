

## Tue Sep 21 19:29:19 2021       
```
$ nvidia-smi
Tue Sep 21 19:29:19 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.63.01    Driver Version: 470.63.01    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:01:00.0  On |                  N/A |
| N/A   55C    P8    21W /  N/A |    393MiB / 16116MiB |      3%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      3279      G   /usr/lib/xorg/Xorg                 35MiB |
|    0   N/A  N/A      8090      G   /usr/lib/xorg/Xorg                155MiB |
|    0   N/A  N/A      8219      G   /usr/bin/gnome-shell               41MiB |
|    0   N/A  N/A     10010      G   /usr/lib/firefox/firefox          140MiB |
|    0   N/A  N/A     12963      G   /usr/lib/firefox/firefox            3MiB |
|    0   N/A  N/A     13426      G   /usr/lib/firefox/firefox            3MiB |
+-----------------------------------------------------------------------------+
```


```
nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Sun_Jul_28_19:07:16_PDT_2019
Cuda compilation tools, release 10.1, V10.1.243
```



## Mon Feb  8 22:42:28 2021       
* Check versions
```
mx19@sie085-lap:~$ nvidia-smi
Mon Feb  8 22:42:28 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.100      Driver Version: 440.100      CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 207...  Off  | 00000000:01:00.0  On |                  N/A |
| N/A   48C    P8     6W /  N/A |    246MiB /  7973MiB |      6%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1357      G   /usr/lib/xorg/Xorg                            18MiB |
|    0      1417      G   /usr/bin/gnome-shell                          49MiB |
|    0      1811      G   /usr/lib/xorg/Xorg                            96MiB |
|    0      1968      G   /usr/bin/gnome-shell                          77MiB |
+-----------------------------------------------------------------------------+

mx19@sie085-lap:~$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89
```




## Thu Apr  8 00:23:34 2021       
```
mx19@sie085-lap:~$ nvidia-smi
Thu Apr  8 00:23:34 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.39       Driver Version: 460.39       CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 2070    Off  | 00000000:01:00.0  On |                  N/A |
| N/A   46C    P8     7W /  N/A |    259MiB /  7973MiB |      1%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1065      G   /usr/lib/xorg/Xorg                 18MiB |
|    0   N/A  N/A      1120      G   /usr/bin/gnome-shell               69MiB |
|    0   N/A  N/A      1523      G   /usr/lib/xorg/Xorg                124MiB |
|    0   N/A  N/A      1684      G   /usr/bin/gnome-shell               40MiB |
|    0   N/A  N/A      4205      G   /usr/lib/firefox/firefox            1MiB |
+-----------------------------------------------------------------------------+
mx19@sie085-lap:~$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89

```





