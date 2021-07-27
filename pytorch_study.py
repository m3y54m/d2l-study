#!/user/bin/env python3


# 2.1. Data Manipulation
# 2.1.1. Getting Started

import torch

# create a row vector x containing the first 12 integers starting with 0
x = torch.arange(12)
print(x)

print(x.shape)

print(x.numel())

# change the shape of a tensor
X = x.reshape(3, 4)
print(X)

# create a tensor representing a tensor with all elements set to 0 and a shape of (2, 3, 4)
print(torch.zeros((2, 3, 4)))

# create tensors with each element set to 1
print(torch.ones((2, 3, 4)))

# create a tensor with shape (3, 4)
# each of its elements is randomly sampled from a standard Gaussian (normal) distribution
# with a mean of 0 and a standard deviation of 1.
print(torch.randn(3, 4))
