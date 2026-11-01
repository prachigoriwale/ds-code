Library = {}

n= int(input("Enter the no of members:"))
for i in range(n):
    member_id = input("Enter the member IDs:")
    book_borrowed = int(input("Enter the no of books borrowed:"))

    book = []
    for j in range(book_borrowed):
        book_name = input("Enter the book name:")
        book.append(book_name)

    Library[member_id] =book

total_members = len(Library)
total_book_borrowed = sum(len(book) for book in Library.values())

average = total_book_borrowed//total_members

print("Average book borrowed:",average)

all_book = []

for book in Library.values():
    all_book.extend(book)

book_count = {}

for book_name in all_book:
    book_count[book_name]= book_count.get(book_name,0)+1

if book_count:
    most_borrowed = max(book_count,key=book_count.get)
    least_borrowed = min(book_count,key=book_count.get)

    print("most borrowed book :",most_borrowed)
    print("least borrowed book:",least_borrowed)
    print("frequently borrowed book (mode):",most_borrowed)

else:
    print("no book have borrowed.")

zero_borrowed = sum( 1 for book in Library.values() if len(book)==0)
print("Member with zero borrowing:",zero_borrowed)