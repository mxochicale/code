

## ERRORS:

* Got error while running CUDA 
``` 
 ./image_scaling 

 Reading image width height and width [272][392]
 scaled image width height and width [136][196]
 Got error while running CUDA API Array Copy
 Got error while running CUDA API Bind Texture
 Launching grid with blocks [6][4] 
 Got error while running CUDA API kernel
 ```

* sorted:
https://github.com/PacktPublishing/Learn-CUDA-Programming/commit/0467cb58ee60b5c95ddea1fc64c83559c5d211fb

```
[-] returnValue = (cudaError_t)(returnValue | cudaMemcpyToArray( cu_array, 0, 0, data, height*width*sizeof(unsigned char), cudaMemcpyHostToDevice));
[+] returnValue = (cudaError_t)(returnValue | cudaMemcpy( cu_array, data, height * width * sizeof(unsigned char), cudaMemcpyHostToDevice));
```

