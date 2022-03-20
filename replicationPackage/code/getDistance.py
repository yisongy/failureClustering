```python
@jit
def kendall(x, y):
    ken_distance = 0
    len = shape(x)[0]
    x1 = 1 / x
    y1 = 1 / y
    for i in range(len):
        for j in range(i+1, len):
            if (x[i] - x[j]) * (y[i] - y[j]) < 0:
                k = x1[i] + x1[j] + y1[i] + y1[j]
                ken_distance += k
    return ken_distance
```

