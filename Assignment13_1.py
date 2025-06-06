class BookStore:
    NoofBooks = 0
    
    def __init__(self,A,B):
        self.name = A
        self.Author = B
        BookStore.NoofBooks = BookStore.NoofBooks +1
    def display(self):
        print("Name is:",self.name)
        print("Author is:",self.Author)
        print("Numbers of books:",BookStore.NoofBooks)
        

def main():
    obj1 = BookStore("Linux System Programming","Robert Love")
    obj1.display()
    
    obj2 = BookStore("C Programming","Dennis Ritchie")
    obj2.display()    

if __name__ == "__main__":
    main()