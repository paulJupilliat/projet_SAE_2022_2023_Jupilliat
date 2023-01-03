## Models permet de definir les données de l app


from .app import db
from flask_login import UserMixin
from .app import login_manager

class Author(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100))
    def __repr__(self):
        return "<Author (%d) %s>" % (self.id, self.name)
class Book(db.Model ):
    id = db.Column(db.Integer, primary_key =True)
    price = db.Column(db.Float)
    title = db.Column(db.String(500))
    url = db.Column(db.String(200))
    img = db.Column(db.String(100))
    # relation pour avoir les auteurs d un livre
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    # relation inverse pour avoir les livres d un auteur
    author = db.relationship("Author",
        backref=db.backref("books", lazy="dynamic"))
    genre= db.relationship("Genre", secondary="book_genre")
    def __repr__ (self ):
        return "<Book (%d) %s>" % (self.id, self.title)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100))
    book=db.relationship("Book", secondary="book_genre",overlaps="genre")
    def get_id(self):
        return self.id
    def __repr__(self):
        return "<Genre (%d) %s>" % (self.id,self.name)
class BookGenre(db.Model):
    __tablename__ = "book_genre"
    id= db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), primary_key=True)
    book = db.relationship(Book, backref=db.backref("books", cascade="all, delete-orphan"),overlaps="book,genre")
    genre = db.relationship(Genre, backref=db.backref("genres", cascade="all, delete-orphan"),overlaps="book,genre")

class User(db.Model , UserMixin ):
    username = db.Column(db.String(50) , primary_key=True)
    password = db.Column(db.String(64))
    
    def get_id(self):
        return self.username
    def __repr__(self):
        return "<User (%s)>" % (self.username)
def get_book(id):
    return Book.query.get(id)
def get_books():
    return Book.query.order_by(Book.title).all()
def get_books_sample(nb_by_page, page):
    return Book.query.order_by(Book.title).limit(nb_by_page).offset((page-1)*nb_by_page).all()
def get_books_sample_filtered(nb_by_page,page,author,genre,price_min,price_max,order):
    query = Book.query.join(Author).join(BookGenre).join(Genre)
    if author != "":
        query = query.filter(Author.name.like("%"+author+"%"))
    if genre != "":
        query = query.filter(Genre.name.like("%"+genre+"%"))
    if price_min != "":
        query = query.filter(Book.price>=price_min)
    if price_max != "":
        query = query.filter(Book.price<=price_max)
    if order == "":
        order = "title"
    if order == "title":
        query = query.order_by(Book.title)
    elif order == "price":
        query = query.order_by(Book.price)
    elif order == "author":
        query = query.order_by(Author.name)
    elif order == "genre":
        query = query.order_by(Genre.name)
    return query.limit(nb_by_page).offset((page-1)*nb_by_page).all()
def get_nb_books_filtered(nb_by_page,author,genre,price_min,price_max):
    query = Book.query.join(Author).join(BookGenre).join(Genre)
    if author is not None:
        query = query.filter(Author.name.like("%"+author+"%"))
    if genre is not None:
        query = query.filter(Genre.name.like("%"+genre+"%"))
    if price_min is not None:
        query = query.filter(Book.price>=price_min)
    if price_max is not None:
        query = query.filter(Book.price<=price_max)
    return int(query.count()/nb_by_page)+1
def get_nb_pages(nb_by_page,types):
    if types=="books":
        return int(Book.query.count()/nb_by_page)+1
    elif types=="authors":
        return int(Author.query.count()/nb_by_page)+1
    elif types=="genres":
        return int(Genre.query.count()/nb_by_page)+1
def get_nb_books():
    return Book.query.count()
def get_author(id):
    return Author.query.get(id)
def get_author_by_name(name):
    return Author.query.filter_by(name=name).first()
def get_authors():
    return Author.query.order_by(Author.name).all()
def get_authors_sample(nb_by_page, page):
    #authors are ordered by name
    return Author.query.order_by(Author.name).limit(nb_by_page).offset((page-1)*nb_by_page).all()
def get_nb_authors():
    return Author.query.count()
def get_genre(id):
    return Genre.query.get(id)
def get_genres():
    return Genre.query.order_by(Genre.name).all()
def get_genres_sample(nb_by_page, page):
    return Genre.query.order_by(Genre.name).limit(nb_by_page).offset((page-1)*nb_by_page).all()
def get_genre_by_name(name):
    return Genre.query.filter_by(name=name).first()
def get_nb_genres():
    return Genre.query.count()
def get_book_genres(id):
    genres=[]
    for g in BookGenre.query.filter_by(book_id=id).all():
        genres.append(get_genre(g.genre_id))
    return genres
def get_genre_books(id):
    books=[]
    for b in BookGenre.query.filter_by(genre_id=id).all():
        books.append(get_book(b.book_id))
    return books
def get_nb_book_genres(id):
    return BookGenre.query.filter_by(book_id=id).count()
def add_genre_to_book(book_id, genre_id):
    book_genre = BookGenre(id=get_nb_book_genres(book_id)+1, book_id=book_id, genre_id=genre_id)
    db.session.add(book_genre)
    db.session.commit()
def remove_genre_from_book(book_id, genre_id):
    book_genre = BookGenre.query.filter_by(book_id=book_id, genre_id=genre_id).first()
    db.session.delete(book_genre)
    db.session.commit()
def supress_book_genres(book_id):
    for book_genre in BookGenre.query.filter_by(book_id=book_id).all():
        db.session.delete(book_genre)
    db.session.commit()
@login_manager.user_loader
def load_user(username):
    return User.query.get(username)