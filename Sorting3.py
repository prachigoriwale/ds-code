n = int(input("Enter the size of list:"))
salaries = []
print("Enter the employee salaries :")
for i in range(n):
    e = int(input(""))
    salaries.append(e)

print("Employee  salary list :",salaries)

def selection_sort(a):
    n=len(a)
    sorted_a = a.copy()
    for i in range (n):
        for j in range(i+1,n):
            if sorted_a[i]>sorted_a[j]:
                temp = sorted_a[i]
                sorted_a[i]=sorted_a[j]
                sorted_a[j]=temp
        
    return sorted_a

def bubble_sort(a):
    n =len(a)
    sorted_a = a.copy()
    for i in range(n):
        for j in range(0,n-i-1):
            if sorted_a[j]>sorted_a[j+1]:
                temp = sorted_a[j]
                sorted_a[j]=sorted_a[j+1]
                sorted_a[j+1]=temp

    return sorted_a

def display_top_5(salary_list):
    top_5 = salary_list[-5:][::-1]
    print("Top 5 highest Salaries:")
    for i,salary in enumerate(top_5,1):
        print(f"{i}.Rs{salary:.2f}")

print("original salary:")
print(salaries)

sel_sort = selection_sort(salaries)

print("salary sorted(selection sort):",sel_sort)
display_top_5(sel_sort)

bub_sort = bubble_sort(salaries)

print("salary sorted(bubble sort):",bub_sort)
display_top_5(bub_sort)




