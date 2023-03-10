MAX_KIDS_BOOK_PAGES = 10

class Book():
    def __init__(self, author, title, subject, num_pages):
        '''(Book, str, str, str, int) -> NoneType

        Initialize this book with an author's name (author), the book's
        title (title), the topic of the book (subject) and the total number
        of pages in the book (num_pages)
        REQ: num_pages > 0
        '''
        self._author = author
        self._title = title
        self._subject = subject
        self._pages = num_pages

    def __str__(self):
        '''(Book) -> str

        Return a string representation of this book
        '''
        return self._title + " by " + self._author

    def get_title(self):
        '''(Book) -> str

        Return the title of this book
        '''
        return self._title

    def get_topic(self):
        '''(Book) -> str

        Return the topic that this book covers
        '''
        return self._subject

class AutoBiography(Book):
    # def __init__(self, author, title, num_pages):
        # self._author = author
        # self._subject = "life of " + author
        # self._title = title
        # self._pages = pages


    # an improved approach
    def __init__(self, author, title, num_pages):
        '''(AutoBiography, str, str, int) -> NoneType

        Initialize this autobiography with the Author's name (author),
        the title of the book (title), and the number of pages. The
        subject of all autobiographies is assumed to be the life of the
        author
        REQ: num_pages > 0
        '''
        Book.__init__(self, author, title, "life of " + author, num_pages)

class KidsBook(Book):
    def __init__(self, author, title, subject, num_pages, min_age, max_age):
        '''(KidsBook, str, str, str, int, int, int) -> NoneType

        Initialize this kids book with the author's name (author), the
        title of the book (title), the subject that the book covers (subject)
        the total number of pages (num_pages), and the minimum and maximum
        ages for which this book is appropriate (min_age and max_age).

        Note that kids books are limited to 10 pages, any num_pages > 10
        will simply be truncated to 10 (I guess we'll throw out the rest
        of the pages or something)
        REQ: min_age, max_age > 0
        REQ: min_age <= max_age
        REQ: num_pages > 0
        '''
        #we're going to restrict kids books to a set number of pages
        if(num_pages > MAX_KIDS_BOOK_PAGES):
            num_pages = MAX_KIDS_BOOK_PAGES
        title = title.upper()
        Book.__init__(self, author, title, subject, num_pages)
        self._start_age = min_age
        self._age_rage = max_age - min_age

    '''First attempt
    def __str__(self):
        out = "Hi kids. Today we're going to learn about " + self._subject
        out += " in a book called: " + self._title
        return out
    '''

    def __str__(self):
        '''(KidsBook) -> str

        Return a kid-friendly string representation of this kid's book
        '''

        out = "Hi kids. Today we're going to learn about " + self.get_topic()
        out += " in a book called: " + self.get_title()
        return out

if(__name__ == "__main__"):
    geb = Book("Douglas Hoffstadter", "Godel Escher Bach",  "strange loops",
               650)
    bh = AutoBiography("Brian Harrington", "The untold story of a CS lecturer",
                       1000)
    vhc = KidsBook("Eric Carle", "The Very Hungry Caterpillar", "Eating disorders",
                   25, 2, 7)
    print(geb)
    print(bh)
    print(vhc)