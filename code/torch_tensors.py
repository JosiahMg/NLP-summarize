import torch

# 构造一个未初始化的矩阵
x = torch.empty(5, 3)
print(x)

# 构造一个随机初始化的矩阵
x = torch.rand(5, 3)
print(x)

# 构造一个初始化为0的矩阵,类型为long
x = torch.zeros(5, 3, dtype=torch.long)
print(x)
print(x.dtype)

# 使用long()转换为long类型
x = torch.zeros(5, 3).long()
print(x.dtype)

# 直接从数据构造tensor,重用原先数据的类型
x = torch.tensor([5.5, 3])
print(x)
x = x.new_ones(5, 3, dtype=torch.float32)
print(x)

x = torch.randn_like(x, dtype=torch.float)
print(x)

# 获取tensor的形状
print(x.shape)
print(x.size())


# tensors的运算
y = torch.rand(5, 3)
print(y)
result = torch.empty(5, 3)
torch.add(x, y, out=result)
# result = x + y   #等价于torch.add()


# in-place加法
y.add_(x) # y = y+x

# 切片
print(x[:, 1:])

# reshape操作
x = torch.randn(4, 4)
print(x)
y = x.view(16)  # y为 16*1
print(y)
y = x.view(-1, 8) # y为2*8的tensors
print(y)

# 将0轴和1轴进行变换，相当于转置操作
print(x.transpose(0, 1))

# 取出tensor的值 只有当x的成员有一个时
x = torch.randn(1)
print(x.item())

# 更多tensor操作如：transposing indexing slicing math linear random
# https://pytorch.org/docs/torch

# tensor与numpy转换
# 下面a和b是共享一块内存
a = torch.ones(5)
print(a)
b = a.numpy()
print(b)

import numpy as np

a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)

# CUDA Tensors
if torch.cuda.is_available():
    device = torch.device("cuda")
    # y数据在gpu上运行
    y = torch.ones_like(x, device=device)
    # 将x数据搬到gpu上
    x = x.to(device)
    z = x + y
    print(z)
    # 将x数据搬到cpu上
    print(z.to("cpu", torch.double))

# cpu上的数据才可以转换成numpy
print("---------------")
print(y)
print(y.to("cpu").numpy()) # 等级与y.cpu().numpy()

