import numpy as np
a = np.arange(15).reshape(3, 5)
# 1.   [簡答題] 請問下列兩種將 Array 轉換成 List 的方式有何不同？
print(a)
print('list(a): ', list(a), "\n", type(list(a)[0]))
print('tolist(): ', a.tolist(), "\n", type(a.tolist()[0]))
print('list僅轉換第一層資料，tolist則完全轉換')

# 2.   請試著在程式中印出以下三個 NdArray 的屬性？（屬性：ndim、shape、size、dtype、itemsize、length、type）
a = np.random.randint(10, size=6)
b = np.random.randint(10, size=(3, 4))
c = np.random.randint(10, size=(2, 3, 2))
print(a.ndim) # 陣列有多少維度
print(a.shape) # 每維度的大小
print(a.size) # 陣列有多少元素
print(a.dtype) # 資料型態
print(a.itemsize) # 每元素佔用的空間
print(len(a))
print(type(a))

print(b.ndim) # 陣列有多少維度
print(b.shape) # 每維度的大小
print(b.size) # 陣列有多少元素
print(b.dtype) # 資料型態
print(b.itemsize) # 每元素佔用的空間
print(len(b))
print(type(b))

print(c.ndim) # 陣列有多少維度
print(c.shape) # 每維度的大小
print(c.size) # 陣列有多少元素
print(c.dtype) # 資料型態
print(c.itemsize) # 每元素佔用的空間
print(len(c))
print(type(c))

# 3.   如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
print(a.tolist())
print(list(a))
print(b.tolist())
print(list(b))
print(c.tolist())
print(list(c))

def list(iterable):
    newlist = []
    [newlist.append(x) for x in iter(iterable)]
    return newlist
def list(iterable):
    return iterable.tolist()
print(list(a))
print(list(b))
print(list(c))
