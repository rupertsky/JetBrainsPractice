import numpy as np
"""To illustrate it, we'll create two lists and two arrays containing the same elements:

list_a = [1, 2, 3, 4]
array_a = np.array(list_a)

list_b = [11, 22, 33, 44]
array_b = np.array(list_b)

First, let's find their sum. The addition of two arrays returns their sum as when we add two vectors.

print(array_a + array_b)  # [12 24 36 48]
"""
"""For this reason, we can't add up arrays of different lengths, a ValueError will appear.

array_c = np.array([111, 222])
print(array_a + array_c)        # ValueError

When we try to add a list and an array, the former is converted to an array, so the result is also a sum of vectors.

print(list_a + array_a)   # [2 4 6 8]

However, when applied to lists, addition just merges them together.

print(list_a + list_b)    # [1, 2, 3, 4, 11, 22, 33, 44]

Similarly, if we try to multiply a list by n, we'll get the list repeated n times, while with an array, 
each element will be multiplied by n:

print(list_a * 3)   # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(array_a * 3)  # [3 6 9 12]"""

"""There're a number of ways to learn more about an array without printing it.

first = np.array([1, 2, 3, 4, 5])
second = np.array([[1, 1, 1],
                   [2, 2, 2]])

To find out the dimension size, use shape. The first number of the output indicates the number of rows and the second — 
the number of columns.

print(second.shape)  # (2, 3)

If the NumPy array has only one dimension, the result will be a bit different:

print(first.shape)   # (5,)

In this case, the first number is not the number of rows but rather the number of elements in the only dimension, and 
the empty place after the comma means that there's no second dimension.

The length of the shape tuple is the number of axes, ndim.

print(first.ndim)   # 1
print(second.ndim)  # 2

The function len() returns the array's length, and size gives us the number of elements in the array.

print(len(first), first.size)    # 5 5 
print(len(second), second.size)  # 2 6

Another thing to point out is that both the length and the size of an array can also be found from its shape: 
length is actually the length of the first dimension, so it equals shape[0], and size is the total number of elements,
which equals the product of all elements in the shape tuple.

isinstance(obj, type)

"""
def analizararray(n):
    """Esta funcion analiza un arreglo de x dimensiones de la forma
        n.shape
        n = np.zeros((n.shape))
    """
    print(n.shape)
    n = np.zeros((3, 2, 6, 1))

    print(n)
    print(n.ndim)
    print(n.size)
    print(len(n))

arreglo = np.arange(0, 10)

print(arreglo)

arreglo2 = np.linspace(0, 9, 100)

print(arreglo2)

arreglo3 = np.arange(10, 101)

mask = arreglo3 % 3 == 0

print(arreglo3[mask])

arreglo4 = np.zeros((5, 10))
arreglo4[[1, 3], :] = 1
arreglo4[:, [2, 7]] = 2

print(arreglo4)


