zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。

我们可以使用 list() 转换来输出列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。


```python
a = [1,2,3]
b = [5,6,7]
zipped = zip(a,b)
zipped
```




    <zip at 0x24ab65b3b48>




```python
liste = list(zipped)
liste
```




    [(1, 5), (2, 6), (3, 7)]




```python
c = [7,8,9,10]
zipped2 = zip(a,c)

```

此处c比a多一项，被省去


```python
liste2 = list(zipped2)
liste2
```




    [(1, 7), (2, 8), (3, 9)]



解压方法


```python
a1, a2 = zip(*liste)

```


```python
a1 
```




    (1, 2, 3)




```python
a2
```




    (5, 6, 7)




```python
a1,a3 = zip(*liste2)
```


```python
a1
```




    (1, 2, 3)




```python
a2
```




    (5, 6, 7)



注意：此处a3与原来相比少了一项


```python
a3
```




    (7, 8, 9)




```python

```
