'''
Input: a List of integers
Returns: a List of integers
'''
'''
UPER NOTES
so you're given an array.
for every index in that array you must use a certain 
multiplication pattern to return that indexs value 
so you have to do some super tricky math here. 
example array of [1,7,3,4] 
you would multiply each value in this array like so
[7*3*4,1*3*4,1*7*4,1*7*3] so the pattern is obv when you see it
"how am i going to get this done."
a lot of googling

'''
def product_of_all_other_numbers(arr):
    # Your code here

    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
