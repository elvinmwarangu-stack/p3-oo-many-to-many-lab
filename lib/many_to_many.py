
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        """return name property"""
        return self._name
    
    @name.setter
    def name(self, name):
        """name setter method"""
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError('name must be a String')
        
    def contracts(self):
        return [l for l in Contract.all if l.author == self]
    
    def books(self):
        return [b.book for b in Contract.all if b.author == self ]
    
    def sign_contract(self, book, date, royalties):
        the_contract = Contract(self, book, date, royalties)
        return the_contract
    
    def total_royalties(self):
        r_list = [r.royalties for r in Contract.all if r.author == self]
        total = 0
        for r in r_list:
            total += r
        return total

class Book:
    all = []
    def __init__(self,title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        """return title property"""
        return self._title
    
    @title.setter
    def title(self, title):
        """title setter method"""
        if isinstance(title, str):
            self._title = title
        else:
            raise TypeError('title must be a String')
        
    def contracts(self):
        return [b for b in Contract.all if b.book == self]
    
    def authors(self):
        return [b.author for b in Contract.all if b.book == self]

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)


    @property
    def author(self):
        """return author property"""
        return self._author

    @author.setter
    def author(self, auth):
        """author setter method"""
        if isinstance(auth, Author):
            self._author = auth
        else:
            raise TypeError('author must be an instance of Author class')

    @property
    def book(self):
        """return book property"""
        return self._book

    @book.setter
    def book(self, book):
        """book setter method"""
        if isinstance(book, Book):
            self._book = book
        else:
            raise TypeError('book must be a Book object')

    @property
    def date(self):
        """return date property"""
        return self._date

    @date.setter
    def date(self, date):
        """date setter method"""
        if isinstance(date, str):
            self._date = date
        else:
            raise TypeError('date must be a string')

    @property
    def royalties(self):
        """return royalties property"""
        return self._royalties

    @royalties.setter
    def royalties(self, ryls):
        """royalties setter method"""
        if isinstance(ryls, int):
            self._royalties = ryls
        else:
            raise TypeError('royalties must be an integer')
        
    @classmethod
    def contracts_by_date(cls,date):
        return [d for d in Contract.all if d.date == date]
    
