size = int(input("Enter the size of hash table:"))
hash_table = [[] for _ in range(size)]
print("hash table:",hash_table)

def insert(key,value):
    index = key%size
    for i in range(len(hash_table[index])):
        if hash_table[index][i][0]==key:
            hash_table[index][i]= (key,value)
            print("key is updated.")
            return

    hash_table[index].append((key,value))
    print(f"key-{key},value-{value} is inserted.")

def search(key):
    index = key%size
    for k,v in enumerate(hash_table[index]):
        if k==key:
            print("value is ",v)

    print("value is not found.")

def delete(key):
    index = key%size
    for i in range(hash_table[index]):
        if hash_table[index][i][0]==key:
            hash_table[index].pop(i) 
            print("key is deleted.")
            return
    print("key is not found") 

def display():
    for i in range(size):
        print(i , "" , hash_table[i])

def menu():
    while True:
            print("\n---menu---")
            print("1.insert value")
            print("2.search value")
            print("3.delete value")
            print("4.Display hash table")
            print("5.exit")
    
            choice = int(input("Enter the choice:"))
    
            if choice==1:
                key = int(input("Enter the key:"))
                value = input("Enter the values:")
                insert(key,value)

            elif choice==2:
                key = int(input(" Enter the key :"))
                search(key)
            elif choice==3:
                key = int(input("Enter the key:"))
                delete(key)
            elif choice==4:
                display()
            elif choice==5:
                print("Exiting...")
                break
            else:
                print("invalid choice")
menu()
