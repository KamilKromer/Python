n = int(input())  # Ilosc operacji

book_list = [] # Lista ksiązek, inaczej nasza półka

class Book:
    def __init__(self):
        self.id_ = None
        self.place = None

    def FetchBook(self, head, tail):

        if head != '?':
            self.id_ = int(tail)  # Zapisz id książki

        if head == 'R':
            book_list.append(self)
            self.place = len(book_list) - 1

        elif head == "L":
            ShiftBooks() # Przesuń książki przed wsadzeniem -> tej
            book_list.insert(0, self) # Wsadź tą książke na sam początek
            self.place = 0 # Zapisz nasze położenie jako początkowe



    def class_shift(self):
        '''Przesuń ksiązki na prawo, wsadzając jedną z lewej'''
        self.place += 1

def X(id_: int):
    list_len = len(book_list)
    list_len /= 2
    list_len = int(list_len)
    if id_ - 1 >= list_len: # Ksiazka w drugiej polowie, Prawa strona, odejmujemy jeden poniewaz jest argument
        return len(book_list) - id_ # ^^ To nie index w liście, ale położenie zaczynające od 1

    if id_ - 1 < list_len: # Ksiazka w pierwszej polowie, lewa strona
        return id_ - 1


def ShiftBooks():
    for book in book_list:
        book: Book
        book.class_shift()



for _ in range(n): # Glowna petla
    inp = input()
    head, tail = inp.split(sep=' ')
    #print(head)
    #print(tail)
    if head == 'R' or head == 'L':
        #print("making")
        book = Book()
        book.FetchBook(head, tail)
    else:
        #print("Cycling")
        #print(book_list)
        for b in book_list:
            #print(f"ID {b.id_}")
            if b.id_ == int(tail): # To jest książka z tym id
                #print(f"Place {b.place}")
                print(X(b.place + 1))


