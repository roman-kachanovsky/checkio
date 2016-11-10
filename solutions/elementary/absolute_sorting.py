""" --- Absolute sorting --- Simple

The array (a tuple) has various numbers. You should sort it, but sort it 
by absolute value in ascending order. 
For example, the sequence (-20, -5, 10, 15) 
will be sorted like so: (-5, 10, 15, -20). 
Your function should return the sorted list or tuple.

Input:              An array of numbers , a tuple..
Output:             The list or tuple (but not a generator) sorted 
                    by absolute values in ascending order.
Addition:           The results of your function will be shown as 
                    a list in the tests explanation panel.
How it is used:     Sorting is a part of many tasks, so 
                    it will be useful to know how to use it.
Precondition:       The numbers in the array are unique 
                        by their absolute values.
                    len(set(abs(x) for x in array)) == len(array)
                    0 < len(array) < 100
                    all(isinstance(x, int) for x in array)
                    all(-100 < x < 100 for x in array)
"""


def my_solution(numbers_array):
    return sorted(numbers_array, key=abs)


veky_solution = lambda n: sorted(n, key=abs)
