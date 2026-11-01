n = int(input("Enter the size of list:"))
a = []
print("Enter the customer IDs:")
for i in range(n):
    e = int(input(""))
    a.append(e)

print("List is : ",a)

def linear_search(a,target_id):
    for j in range(n):
        if target_id == a[j]:
            return j
    return -1

def binary_search(a,target_id):
    low = 0
    high = n-1
    while low<=high :
        mid = (low+high)//2
        if target_id == a[mid]:
            return mid
        elif target_id <= a[mid]:
            high = mid - 1
        else:
            low = mid + 1   
             
    return -1

target_id = int(input("Enter the customer ID to search:"))

# linear search result
found_linear = linear_search(a,target_id)
if found_linear != -1:
    print("linear Search : ID found at index ",found_linear)
else:
    print("Linear Search : ID not found")

# Binary search result
a.sort()
print("Sorted list:",a)
found_binary = binary_search(a,target_id)
if found_binary != -1:
    print("Binary Search : ID found at index ",found_binary)
else:
    print("Binary Search : ID not found")

