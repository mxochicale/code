# Pytorch
> An open source machine learning framework that accelerates the path from research prototyping to production deployment. 
See releases https://github.com/pytorch/pytorch/releases 

## Install uv and deps
```bash
uv venv --python 3.12
uv pip install -e .
uv pip list
source .venv/bin/activate
```

## Examples
Run [examples](examples)
```bash
#
uv run examples/hello-world-NN/hwnn.py
vim examples/hello-world-NN/hwnn.py
#
uv run examples/optimisation_tutorial/optimization_tutorial.py
vim examples/optimisation_tutorial
```

## Notes
* To move tensors to the respective device:
	torch.rand(10).to(device)

* To create a tensor directly on the device:
	torch.rand(10, device=device)


## References
* https://pytorch.org/get-started/locally     
* https://en.wikipedia.org/wiki/PyTorch   
* https://stackoverflow.com/questions/48152674/how-do-i-check-if-pytorch-is-using-the-gpu

