class Node:
    def __init__(self,roll,name,marks):
        self.roll= roll
        self.name= name
        self.marks = marks
        self.next = None

class Student:

    def __init__(self):
        self.head = None

    def add(self,roll,name,marks):
        new = Node(roll,name,marks)


        if self.head is None:
            self.head = new

        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

        print("Student is successfully added.")

    def display(self):
        temp = self.head

        if temp is None:
            print("no record found.")
            return

        print("\nroll \tname \tmarks")
        while temp:
            print(temp.roll,"\t",temp.name,"\t",temp.marks)
            temp = temp.next

    def search(self,roll):
        temp = self.head
      
        while temp:
            if temp.roll==roll:
                print("Student found.")
                print("Student rollno:",temp.roll)
                print("Student name:",temp.name)
                print("Student marks:",temp.marks)
                return
            temp=temp.next

        print("student not found.")

    def delete(self,roll):
        temp = self.head
        prev= None

        while temp:
            if temp.roll==roll:
                if prev is None:
                    self.head=temp.next
                else:
                    prev.next = temp.next
                    print("student is deleted successfully.")
                    return
            prev=temp
            temp = temp.next

        print("Student is not found.")

    def update(self,roll):
        temp = self.head

        while temp:
            if temp.roll==roll:
                temp.name = input("Enter new name:")
                temp.marks = float(input("enter new marks:"))
                print("student updated successfully.")
                return
            temp = temp.next
        print("student not found.")

    def sort(self, choice ,order):
        a = []
        temp = self.head

        while temp:
            a.append(temp)
            temp=temp.next

            if choice==1:
                a.sort(lambda x: x.marks , reverse=(order==2))
            else:
                a.sort(lambda x: x.roll , reverse=(order==2))

            self.head=None

            for x in a:
                x.next = None
                if self.head is None:
                    self.head=x
                else:
                    temp= self.head
                    while temp.next:
                        temp = temp.next
                    temp.next = x

            print("record sorted successfully.")

            self.display()

s = Student()
while True:
    print("\n1.Add Student")
    print("2.Delete Student")
    print("3.Update Student")
    print("4.Search Student")
    print("5.Sort Records")
    print("6.Display Records")
    print("7.Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        r = int(input("Enter Roll Number : "))
        n = input("Enter Name: ")
        m = float(input("Enter Marks: "))
        s.add(r, n, m)

    elif ch == 2:
        r = int(input("Enter Roll Number : "))
        s.delete(r)

    elif ch == 3:
        r = int(input("Enter Roll Number: "))
        s.update(r)

    elif ch == 4:
        r = int(input("Enter Roll Number: "))
        s.search(r)

    elif ch == 5:
        print("1.Sort by Marks")
        print("2.Sort by Roll Number")
        choice = int(input("Enter choice: "))

        print("1.Ascending")
        print("2.Descending")
        order = int(input("Enter order: "))

        s.sort(choice, order)

    elif ch == 6:
        s.display()

    elif ch == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")





                        





