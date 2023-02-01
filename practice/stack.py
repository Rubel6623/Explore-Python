books=[]
books.append("Physics")
books.append("Chemistry")
books.append("Biology")
print(books)
books.pop()
print(books)
print("Now the top book is",books[-1])
books.pop()
print("Now the top book is",books[-1])
books.pop()
print(books)
if not books:
    print("there is no book")
