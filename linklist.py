
class Node:
    def __init__(n, r, name, m):
        n.roll = r
        n.name = name
        n.marks = m
        n.next = None


head = None

def add():
    global head
    r = int(input("Enter Roll No : "))
    name = input("Enter Name: ")
    m = int(input("Enter Marks: "))

    new = Node(r, name, m)

    if head == None:
        head = new
    else:
        t = head
        while t.next:
            t = t.next
        t.next = new

    print("Added Successfully")


def display():
    t = head
    while t:
        print(t.roll, t.name, t.marks)
        t = t.next


def search():
    r = int(input(" Enter Roll No: "))
    t = head

    while t:
        if t.roll == r:
            print("Found:", t.name, t.marks)
            return
        t = t.next

    print(" Not Found")


def delete():
    global head
    r = int(input("Enter Roll No: "))
    t = head
    p = None

    while t:
        if t.roll == r:
            if p == None:
                head = t.next
            else:
                p.next = t.next
            print("Deleted")
            return
        p = t
        t = t.next

    print("Not Found")


def update():
    r = int(input("Enter Roll No: "))
    t = head

    while t:
        if t.roll == r:
            t.name = input("Enter New Name: ")
            t.marks = int(input("Enter New Marks: "))
            print("Updated")
            return
        t = t.next

    print("Not Found")


def sort():
    t = head

    while t:
        p = t.next
        while p:
            if t.marks > p.marks:
                t.roll, p.roll = p.roll, t.roll
                t.name, p.name = p.name, t.name
                t.marks, p.marks = p.marks, t.marks
            p = p.next
        t = t.next

    print("Sorted by Marks")


while True:
    print("\n1.Add  2.Display  3.Search")
    print("4.Delete  5.Update  6.Sort  7.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        add()
    elif ch == 2:
        display()
    elif ch == 3:
        search()
    elif ch == 4:
        delete()
    elif ch == 5:
        update()
    elif ch == 6:
        sort()
        display()
    elif ch == 7:
        break
    else:
        print("Wrong Choice")
