# MultiThreading in Python 

## Prepare path and VE
```
cd $HOME/repositories/code/playground/multi-threading-python
conda activate simpleVE
```

## Launch scripts
* example00.py
```
$ time python example00.py 
Downloading https://images.unsplash.com/photo-1509718443690-d8e2fb3474b7 
Downloading https://images.unsplash.com/photo-1587620962725-abab7fe55159 
Downloading https://images.unsplash.com/photo-1493119508027-2b584f234d6c 
Downloading https://images.unsplash.com/photo-1482062364825-616fd23b8fc1 
Downloading https://images.unsplash.com/photo-1521185496955-15097b20c5fe 
Downloading https://images.unsplash.com/photo-1510915228340-29c85a43dcfe 
Downloading https://images.unsplash.com/photo-1509718443690-d8e2fb3474b7 
Downloading https://images.unsplash.com/photo-1587620962725-abab7fe55159 
Downloading https://images.unsplash.com/photo-1493119508027-2b584f234d6c 
Downloading https://images.unsplash.com/photo-1482062364825-616fd23b8fc1 
Downloading https://images.unsplash.com/photo-1521185496955-15097b20c5fe 
Downloading https://images.unsplash.com/photo-1510915228340-29c85a43dcfe 

real	0m8.055s
user	0m0.757s
sys	0m0.362s
``` 

* example01.py
``` 
$ time python example01.py 
img_url: https://images.unsplash.com/photo-1509718443690-d8e2fb3474b7 
img_url: https://images.unsplash.com/photo-1587620962725-abab7fe55159 
img_url: https://images.unsplash.com/photo-1493119508027-2b584f234d6c 
img_url: https://images.unsplash.com/photo-1482062364825-616fd23b8fc1 
img_url: https://images.unsplash.com/photo-1521185496955-15097b20c5fe 
img_url: https://images.unsplash.com/photo-1510915228340-29c85a43dcfe 
img_url: https://images.unsplash.com/photo-1509718443690-d8e2fb3474b7 
img_url: https://images.unsplash.com/photo-1587620962725-abab7fe55159 
img_url: https://images.unsplash.com/photo-1493119508027-2b584f234d6c 
img_url: https://images.unsplash.com/photo-1482062364825-616fd23b8fc1 
img_url: https://images.unsplash.com/photo-1521185496955-15097b20c5fe 
img_url: https://images.unsplash.com/photo-1510915228340-29c85a43dcfe 

real	0m7.432s
user	0m1.066s
sys	0m0.555s

```

* example02.py
```
$ time python example02.py 
i: 0
[12759441, 6690078, 10677728, 11299067, 3196975, 14294135, 11419689, 1041992, 6814708, 7275302]
i: 1
[16231851, 18180739, 18364122, 10671756, 14199228, 18320384, 4772414, 4730881, 17363917, 9492162]

real	0m0.014s
user	0m0.014s
sys	0m0.000s


```

* example03.py

``` 
time python example03.py

```


* Remove photos:
```
rm photo-1*
```




## References 
* https://www.youtube.com/watch?v=wOFnKB33Lls
* https://towardsdatascience.com/multithreading-multiprocessing-python-180d0975ab29


