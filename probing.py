size =int(input("Enter the size of hash table:"))
hash_table = [None]*size
print(hash_table)

def insert(key,value):
    index = key%size
    for i in range(size):
        new_index = (index+i)%size

        if hash_table[new_index] is None:
            hash_table[new_index]=(key,value)
            print(f"key-{key} , value-{value} is inserted.")
            return
        elif hash_table[new_index][0]==key:
            hash_table[new_index]=(key,value)
            print("key is updated.")
            return
        else:
            print("hash table is full.")

def search(key):
    index = key%size
    for i in range(size):
        new_index = (index+i)%size

        if hash_table[new_index] is None:
            print("key is not found.")
            return
        if hash_table[new_index][0]==key:
            print("value is:",hash_table[new_index][1])
            return
    print("key is not found")

def delete(key):
    index = key%size

    for i in range(size):
        new_index =(index+i)%size

        if hash_table[new_index] is None:
            print("key not found.")
            return
        if hash_table[new_index][0]==key:
            hash_table[new_index]="DELETED"
            print("key deleted successfully.")
            return
    print("key not found.")

def display():
    for i in range(size):
        print(i,":",hash_table[i])

def menu():
    while True:
        print("\n ---menu---")
        print("1.insert key")
        print("2.search key")
        print("3.delete key")
        print("4.display hash table")
        print("5.exit")

        choice = int(input("enter the choice :"))

        if choice==1:
            key = int(input("Enter the key:"))
            value = input("Enter the value:")
            insert(key,value)
        elif choice==2:
            key = int(input("Enter the key:"))
            search(key)
        elif choice==3:
            key = int(input("Enter the key :"))
            delete(key)
        elif choice==4:
            display()
        elif choice==5:
            print("exiting...")
            break
        else:
            print("invalid choice")

menu()