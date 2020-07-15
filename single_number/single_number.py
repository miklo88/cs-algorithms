'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
'''
UPER UPER TIME
so this function takes in a list of ints. aka a list[1,2,3,4,5,6]
 of nums where every int shows up twice except one so like list[1,1,2,2,3,4,4,5,5,6,6]
so i need to return the int that is only listed once in a list.
"so what needs to be done"
as an arr list being passed into single_number(arr): fn 
i need to look over each value in that list.
while doing so i need to be able to check each value and see if there are more than one of the same value.
if there is only one of a certain value. then return it.
"how am i going to do it?"
i'm thinking that i need to loop over the data,
so either a for or while loop -
then check each value if it meets certain conditions.
if elif else. most likely if and else will be needed.

sorting can be applied here. iteration sort or binary search tree would work aqui.
bubble sort as well.


'''
def single_number(arr):
    # Your code here
    n = len(arr)
    for i in range(0, n):
        print(n[1])
    # pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")