# Run time analysis

## Task0
The run time is constant **O(1)** because to access a location in the array takes constant time.
```
O(1)
```

## Task1
The run time is **O(n)**, this is because it needs to iterate through the texts list this takes O(n). Lastly, it also 
iterates the entire list of calls which takes O(n).

```
 O(n) + O(n) = O(2n) = O(n)
```

## Task2
The time complexity for this task is **O(n)**, the code iterates over the list and filters out calls that were made on 
09-2016, then it stores the phone as the key and their duration on a dictionary. All of these operations takes O(n). 
Lastly, it goes through the dictionary to determine the longest call duration and this takes O(n).

```
 O(n) + O(n) = O(2n) = O(n)
```


## Task3

### Task3.1

This takes **O(n log n)**, the algorithm goes through the list of calls and filter the calling numbers with the prefix 
'(080)'. Then the algorithm looks if the receiving call of the area codes and mobile prefixes and append these number to
a set. All the prior operations takes **O(n)**, lastly the algorithm sorts the unique numbers which takes 
**O(n log n)**.

```
 O(n) + O(n log n) = O(n log n)
```

### Task3.2
The run time is **O(n)**, the algorithm first iterates over the list of calls and filters the numbers with the prefix 
'(080)'. Then the algorithm looks if the receiving call has the prefix '(080)' to count and being able to determine the 
percentage.

```
 O(n)
```

## Task4
The run time is **O(n log n)**, the code iterates 2 times over the call list, the first time to store in the unique 
phone number from the callers. The second time to remove from the set the receipt number. Lastly it iterates through the 
text list to remove all these numbers from the set also. Finally, the remaining items on the set are sorted this 
operation takes **O(n log n)**.

```
 O(n) + O(n) +O(n) + O(n log n) = O(n log n)
```