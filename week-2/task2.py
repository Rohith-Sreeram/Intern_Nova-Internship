import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original Array:", arr)
print("Element at index 2:", arr[2])
print("Element at index 6:", arr[6])

print("Sliced Array:", arr[2:7])

two_dimensional = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("Two-dimensional Array:")
print(two_dimensional)

print("First Row:", two_dimensional[0])
print("Second Row:", two_dimensional[1])
print("First Column:", two_dimensional[:, 0])
print("Third Column:", two_dimensional[:, 2])
print("Element at Row 2, Column 3:", two_dimensional[1, 2])

reshaped_array = arr.reshape(2, 5)

print("Reshaped Array:")
print(reshaped_array)

reshaped_array_3d = arr.reshape(2, 5, 1)

print("3D Reshaped Array:")
print(reshaped_array_3d)