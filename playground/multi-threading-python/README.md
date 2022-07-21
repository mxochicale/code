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

* example04.py

``` 
$ time python example04.py
Start thread function
End thread function
thread.name: Thread-1 (threadFunc)
Start thread function
End thread function
thread.name: Learning Threads
None
Start thread function
139708453263104
End thread function

real	0m3.017s
user	0m0.014s
sys	0m0.000s

```

* example05.py
``` 
$ time python example05.py
Thread arguments=> 100 and 200
End thread function

real	0m1.014s
user	0m0.009s
sys	0m0.005s

```

* example06.py
``` 
$ time python example06.py
Thread... Argument PASSING_ARG1
A thread is existing

real	0m1.015s
user	0m0.011s
sys	0m0.003s

```


* multi.py
```
$ time python multi.py 
singleprocessing
counter1 done!
counter2 done!
time taken =  9.262816667556763
multiprocessing
counter2 done!
counter1 done!
time taken =  5.792382478713989

real	0m15.076s
user	0m18.002s
sys	0m0.004s


```

* prime.py 
```  
 time python prime.py
singleprocessing
[False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True]
time taken =  7.529933452606201
multiprocessing
[(0, False), (1, False), (2, True), (3, True), (4, False), (5, True), (6, False), (7, True), (8, False), (9, False), (10, False), (11, True), (12, False), (13, True), (14, False), (15, False), (16, False), (17, True), (18, False), (19, True), (20, False), (21, False), (22, False), (23, True), (24, False), (25, False), (26, False), (27, False), (28, False), (29, True)]
time taken =  1.4778649806976318

real	0m9.102s
user	0m20.392s
sys	0m0.148s

```

* downloader.py

mkdir images 

```  
$ time python downloader.py 
singleprocessing
time taken =  3.482032299041748 

multiprocessing
time taken =  0.5417776107788086 

real	0m4.105s
user	0m0.409s
sys	0m0.076s
```

rm images/* 


* event00.py
```
$ time python event00.py
value is False
value is False
value is True, quitting

real	0m2.015s
user	0m0.014s
sys	0m0.000s

```

* event01.py
``` 
$ time python event01.py
A: val=20
B: val=30
A: val=20
B: val=30
A: val=20
B: val=30
A: val=20
B: val=30
A: val=20


```


## References 
* https://www.youtube.com/watch?v=wOFnKB33Lls
* https://towardsdatascience.com/multithreading-multiprocessing-python-180d0975ab29


