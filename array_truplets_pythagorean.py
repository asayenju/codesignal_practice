"""
Array Triplets with Pythagorean Property
Given an integer array of length n, return a result array of length n-2, where result[i] = 1 if:

array[i]^2 + array[i+1]^2 = array[i+2]^2,
array[i+1]^2 + array[i+2]^2 = array[i]^2, and
array[i]^2 + array[i+2]^2 = array[i+1]^2.
Otherwise, result[i] = 0.
"""

def arraytriplets(arr):
    res = [0]*(len(arr)-2)
    for i in range(len(arr)-2):
        if arr[i]**2+arr[i+1]**2 == arr[i+2]**2 and arr[i+1]**2 + arr[i+2]**2 == arr[i]**2 and arr[i]^2 + arr[i+2]^2 == arr[i+1]^2:
            res[i] +=1
    return res

