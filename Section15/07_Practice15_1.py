class Book:
    def set_info(self, title, writer):
        self.title = title
        self.writer = writer

    def print_book_info(self):
        print(f'책 제목 :{self.title}')
        print(f'책 저자 :{self.writer}')


book1 = Book()
book2 = Book()

book1.set_info("파이썬", "민경태")
book2.set_info("어린왕자", "생텍쥐페리")

book_list = [book1, book2]

for book in book_list:
    book.print_book_info()
