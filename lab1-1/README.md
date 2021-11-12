# algo_labs
my algo labs on IoT program


Your task is to implement a sorting algorithm. The input data is a one-dimensional array of numbers, which is written through a comma and can be run as follows:
python merge_sort.py asc 1,2,56,45, -9,78,11
java MergeSort.java desc 1,2,56,45, -9,78,11
asc - ascending
desc - descending
That is, your code must be able to sort ascending. and descending
The result should display:
the name of the algorithm
work time
the number of comparison operations that were performed during the operation of the algorithm
the number of exchange operations that were performed during the operation of the algorithm
Sorting results
MergeSort:
execution time: 23ms
Comparisons: 2000
Swaps: 3000
-9,1,2,11,45,56,78
Every student must have their own code!
The code should be filled in Github before the demonstration to the teacher and add a comment link to the assessment document
The project must have correctly configured .gitignore (compilation files, IDE configuration files must be absent in the repository)
Your code should be covered by tests that verify:
sort the input array
sort in ascending order of sorted array in ascending order
sort in descending order of sorted array in ascending order
sort in descending order of sorted array in ascending order
sort descending sorted array descending
Note that in a sorted sort situation, you should not have exchange operations, or they should be as many as possible (if the sort is descending and the array is sorted in ascending order).
Your option is determined by a simple principle:
your number in the group list% 3
remainder 1 - QuickSort
remainder 2 - MergeSoft
remainder 0 - HeapSort
Also, everyone should be able to describe and write the code of one of the three basic algorithms:
bubble
exchange
insert
