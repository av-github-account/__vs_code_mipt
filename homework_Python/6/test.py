import uuid
from pydantic import BaseModel, EmailStr, Field, UUID4


class Book(BaseModel):
    title: str
    author: str
    year: int 
    available: bool
    categories: list[str]
    quantity: int = Field(ge=1)

    def __hash__(self): 
        return hash(self.title)
    

class User(BaseModel):
    name: str
    email: EmailStr
    membership_id: UUID4 = Field(default_factory=uuid.uuid4)
    borrowed_books: dict[Book, int]

    def __hash__(self):
        return hash(self.name)


class Libarary(BaseModel):
    free_books: dict[Book, int]
    borrowed_books: dict[Book, int]
    users: list[User]


    def add_book(self, book: Book, user: User) -> any:
        '''
        Пользователь берет 1 книгу book
        '''
        # проверка есть ли книга в принципе
        if self.find_book(book=book.title) == None:
            print('Not found or out of stock')
            return None
        else:
            # проверка есть ли хотябы одна книга в наличии
            if self.free_books[book] == 0:
                print('Not found or out of stock')
                return None
            else:
                self.free_books[book] -= 1
                # проверка, есть ли книга в списке взятых книг у пользователя
                if user.borrowed_books.get(book, None) == None:
                    # создаем книгу у пользователя
                    user.borrowed_books[book] = 1
                else:
                    user.borrowed_books[book] += 1
                # проверка, есть ли книга в списке взятых книг библиотеки
                if self.borrowed_books.get(book, None) == None:
                    # создаем книгу во взятых в библиотеке
                    self.borrowed_books[book] = 1
                else:
                    self.borrowed_books[book] += 1
        print (f'{self.free_books[book]} in stock after user {user.name} took one')
        pass

    def find_book(self, book: str) -> any:
        for kniga in self.free_books.keys():
            if (
                book.lower().strip() in kniga.author.lower() or 
                book.lower().strip() in kniga.title.lower() or 
                book.lower().strip() in kniga.categories and 
                self.free_books[kniga] >= 0
                ):
                print(f'Successfully found: title: {kniga.title}, author: {kniga.author}, year: {kniga.year}, {self.free_books[kniga]} in stock')
                return kniga
        print('Not found or out of stock')
        return None
    
    def is_book_borrow(self, book: str) -> bool:
        '''
        Проверяет, все ли книги разобрали
        '''
        if self.free_books[self.find_book(book)] == 0:
            raise BookNotAvailable('Not found or out of stock')
        return False
    
    def return_book(self, book: Book, user: User) -> None:
        '''
        Пользователь возвращает 1 книгу
        '''
        # проверка есть ли у пользователя книга
        if user.borrowed_books.get(book, None) == None:
            print(f'User {user.name} has no book {book.title}')
            return None
        else:
            user.borrowed_books[book] -= 1
            self.free_books[book] += 1
            self.borrowed_books[book] -=1
        pass

    def total_books(self) -> None:
        for borrowed in self.free_books:
            if borrowed == cap:
                pass
            else:
                print(f'Book: {borrowed.title}, in stock: {self.free_books[borrowed]}, borrowed: {borrowed.quantity - self.free_books[borrowed]}')

class BookNotAvailable(Exception):
    pass

# cap книга заглушка к сожалению
cap = Book(title='', author='', year=0, available=False, categories=[''], quantity=1)
