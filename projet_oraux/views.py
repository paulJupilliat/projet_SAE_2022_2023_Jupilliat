##views permet de definir les routes de l app donc des differents pages

from .app import app
from flask import render_template, request,url_for , redirect
from .models import *
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField,PasswordField
# from wtforms.validators import DataRequired
from hashlib import sha256
from flask_login import login_user , current_user,logout_user

# class AuthorForm(FlaskForm):
#     id = HiddenField("id")
#     name = StringField("Name",validators=[DataRequired()])
# class BookForm(FlaskForm):
#     id = HiddenField("id")
#     title = StringField("Title",validators=[DataRequired()])
#     price = StringField("Price",validators=[DataRequired()])
#     url = StringField("Url",validators=[DataRequired()])
#     img = StringField("Picture(link)",validators=[DataRequired()])
#     #champ pour le choix de l auteur liste déroulante
#     author = StringField("Author",validators=[DataRequired()])
#     genres = StringField("Genres(separated by comma)",validators=[DataRequired()])
# class GenreForm(FlaskForm):
#     id = HiddenField("id")
#     name = StringField("Name",validators=[DataRequired()])
# class FiltersForm(FlaskForm):
#     author = StringField("Author")
#     genre = StringField("Genre")
#     price_min = StringField("Price min")
#     price_max = StringField("Price max")
#     order = StringField("Order(by title, author, genre, price)")

class LoginForm ( FlaskForm ):
    username = StringField("Username")
    password = PasswordField("Password")
    
    def get_authenticated_user(self):
        # user = User.query.get(self.username.data)
        user = None
        if self.username.data == "celine":
            m = sha256()
            user = {"password" : m.update("01234")}
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.password else None

# class RegisterForm ( FlaskForm ):
#     username = StringField("Username")
#     password = PasswordField("Password")
#     confirm = PasswordField("Confirm password")

# class EditUserForm ( FlaskForm ):
#     username = StringField("Actual username")
#     password = PasswordField("Actual password")
#     newpsswd = PasswordField("New password")
#     confirm = PasswordField("Confirm new password")


@app.route("/")
def route():
    return render_template("index.html",title="Projet soutien", admin=True)

@app.route("/ResQCM")
def ResQCM():
    return render_template("ResQCM.html",title="Resultat QCM", admin=True)

@app.route("/Acceuil")
def Acceuil():
    return render_template("Acceuil.html",title="Acceuil", admin=False)

@app.route("/connexionAdm")
def connexionAdm():
    return render_template("connexionAdm.html",title="Connexion Administrateur")

@app.route("/connexionProf")
def connexionProf():
    return render_template("connexionProf.html",title="Connexion Professeur")

@app.route("/Dispo")
def Dispo():
    return render_template("Dispo.html",title="Disponibilité", admin=True)

@app.route("/paramAdm")
def paramAdm():
    return render_template("paramAdm.html",title="Paramètres Administrateur")

@app.route("/save/paramAdm",methods=("POST",))
def save_paramAdm():
    return render_template("paramAdm.html",title="Paramètres Administrateur")

@app.route("/paramEns")
def paramEns():
    return render_template("paramEns.html",title="Paramètres Enseignant")

@app.route("/save/paramEns",methods=("POST",))
def save_paramEns():
    return render_template("paramEns.html",title="Paramètres Enseignant")
@app.route("/res_sond")
def res_sond():
    return render_template("res_sond.html",title="Resultat sondage", admin=True)

@app.route("/Soutien")
def Soutien():
    return render_template("Soutien.html",title="Soutien", admin=True)

@app.route("/Suivie_etu")
def Suivie_etu():
    return render_template("Suivie_etu.html",title="Suivie étudiant", admin=True)

@app.route("/SuivieGenEtu")
def SuivieGenEtu():
    return render_template("SuiviGenEtu.html",title="Suivie général étudiant", admin=True)

@app.route("/search/",methods=("POST",))
def search():
    search = request.form.get("recherche")
    search = search.lower()
    eleve = Eleve.query.filter(Eleve.nom.lower().like("%"+search+"%")).all()
    prof = Professeur.query.filter(Professeur.nom.lower().like("%"+search+"%")).all()
    return render_template("SuivieGenEtu.html",title="Recherche", eleve=eleve, prof=prof)

# @app.route("/")
# def home():
#     return render_template(
#         "index.html",
#         title="Projet soutien",
#         books=get_books(),authors=get_authors(),genres=get_genres())
# # @app.route("/books/<int:id>",methods=("POST","GET"))
# def books(id):
#     f=FiltersForm()
#     if not f.author.data and not f.genre.data and not f.price_min.data and not f.price_max.data and not f.order.data:
#         books=get_books_sample(15,id)
#         return render_template(
#             "books.html",
#             title="My Books ["+str(id)+"] !",
#             books=books,nbp=get_nb_pages(15,"books"),id=id,form=f)
#     if not f.author.data:
#         f.author.data=""
#     if not f.genre.data:
#         f.genre.data=""
#     if not f.price_min.data:
#         f.price_min.data=""
#     if not f.price_max.data:
#         f.price_max.data=""
#     if not f.order.data:
#         f.order.data=""
#     books=get_books_sample_filtered(15,id,f.author.data,f.genre.data,f.price_min.data,f.price_max.data,f.order.data)
#     return render_template(
#         "books.html",
#         title="My Books ["+str(id)+"] !",
#         books=books,nbp=get_nb_books_filtered(15,f.author.data,f.genre.data,f.price_min.data,f.price_max.data),id=id,form=f)

# @app.route("/authors/<int:id>")
# def authors(id):
#     authors=get_authors_sample(15,id)
#     return render_template(
#         "authors.html",
#         title="My Authors ["+str(id)+"] !",
#         authors=authors,nbp=get_nb_pages(15,"authors"),id=id)
# @app.route("/genres/<int:id>")
# def genres(id):
#     genres=get_genres_sample(15,id)
#     return render_template(
#         "genres.html",
#         title="My Genres !",
#         genres=genres,nbp=get_nb_pages(15,"genres"),id=id)
# @app.route("/detail/<id>")
# def detail(id):
#     book=get_book(id)
#     return render_template(
#     "detail.html",
#     book=book,genres=get_book_genres(book.id))

# @app.route ("/edit/author/<int:id>")
# def edit_author(id):
#     if not current_user.is_authenticated:
#         next="edit_author"
#         id=id
#         return redirect(url_for("login",next=next,id=id))
#     a = get_author(id)
#     f = AuthorForm (id=a.id , name=a.name)
#     return render_template (
#         "edit-author.html",
#         author =a, form=f)
# @app.route("/detail/author/<int:id>")
# def detail_author(id):
#     if id is None:
#         return render_template("add-author.html",form=AuthorForm())
#     a = get_author(id)
#     return render_template(
#         "detail-author.html",
#         author=a)

# @app.route("/save/author/", methods =("POST",))
# def save_author():
#     a = None
#     f = AuthorForm()
#     #si c'est une modification
#     if f.validate_on_submit():
#         if f.id.data:
#             a = get_author(f.id.data)
#             a.name = f.name.data
#             id=int(f.id.data)
#             db.session.commit()
#             return redirect(url_for("detail_author", id=a.id ))
#         else:
#             #recupere l'id du dernier auteur
#             id =int(get_nb_authors()) +1  
#             a = Author(id=id,name=f.name.data)
#             db.session.add(a)
#             db.session.commit()
#             return redirect(url_for("detail_author", id=a.id ))
#     a = get_author(int(f.id.data))
#     return render_template(
#         "edit-author.html",
#         author =a, form=f)

# @app.route("/add/author/")
# def add_author():
#     if not current_user.is_authenticated:
#         next="add_author"
#         return redirect(url_for("login",next=next))
#     return render_template("add-author.html",form=AuthorForm(id=None,name=None))

# @app.route("/delete/author/<int:id>")
# def delete_author(id):
#     if not current_user.is_authenticated:
#         next="delete_author"
#         id=id
#         return redirect(url_for("login",next=next,id=id))
#     a = get_author(id)
#     db.session.delete(a)
#     books = get_books()
#     for book in books:
#         if book.author_id == id:
#             db.session.delete(book)
#     db.session.commit()
#     return redirect(url_for("home"))
# @app.route("/add/book/")
# def add_book():
#     if not current_user.is_authenticated:
#         next="add_book"
#         return redirect(url_for("login",next=next))
#     return render_template("add-book.html",form=BookForm(id=None,title=None,price=None,url=None,img=None,author_id=None,genres=None))

# @app.route("/save/book/", methods =("POST",))
# def save_book():
#     b = None
#     f = BookForm()
#     #si c'est une modification
#     if f.validate_on_submit():
#         price=f.price.data
#         if not price.replace('.','',1).isdigit() or float(f.price.data) < 0:
#             f.price.errors.append("Price must be an integer greater than 0")
#             return render_template(
#                 "edit-book.html",
#                 book =b, form=f)
#         if f.id.data:
#             b = get_book(f.id.data)
#             b.title = f.title.data
#             b.price = f.price.data
#             b.url = f.url.data
#             b.img = f.img.data
#             auth= get_author_by_name(f.author.data)
#             if auth is None:
#                 auth = Author(id=get_nb_authors() +1,name=f.author.data)
#                 db.session.add(auth)
#             b.author_id = auth.id
#             supress_book_genres(b.id)
#             f.genres.data = f.genres.data.split(",")
#             for genre in f.genres.data:
#                 g = get_genre_by_name(genre)
#                 if g is None:
#                     g = Genre(id=get_nb_genres() +1,name=genre)
#                     db.session.add(g)
#                 #si le livre n'a pas deja ce genre
#                 if g not in get_book_genres(b.id):
#                     add_genre_to_book(b.id,g.id)
#             id=int(f.id.data)
#             db.session.commit()
#             return redirect(url_for("detail", id=b.id ))
#         else:
#             #recupere l'id du dernier livre
#             id =get_nb_books()+1  
#             auth= get_author_by_name(f.author.data)
#             if auth is None:
#                 auth = Author(id=get_nb_authors()+1,name=f.author.data)
#                 db.session.add(auth)
            
#             b = Book(id=id,title=f.title.data,price=f.price.data,url=f.url.data,img=f.img.data,author_id=auth.id)
#             f.genres.data = f.genres.data.split(",")
#             for genre in f.genres.data:
#                 g = get_genre_by_name(genre)
#                 if g is None:
#                     g = Genre(id=get_nb_genres() +1,name=genre)
#                     db.session.add(g)
#                 add_genre_to_book(b.id,g.id)
#             db.session.add(b)
#             db.session.commit()
#             return redirect(url_for("detail", id=b.id ))
#     b = get_book(int(f.id.data))
#     return render_template(
#         "edit-book.html",
#         book =b, form=f)

# @app.route("/edit/book/<int:id>")
# def edit_book(id):
#     if not current_user.is_authenticated:
#         next="edit_book"
#         id=id
#         return redirect(url_for("login",next=next,id=id))
#     b = get_book(id)
#     g = get_book_genres(id)
#     genres=""
#     for genre in g:
#         genres+=genre.name +","
#     f = BookForm (id=b.id , title=b.title,price=b.price,url=b.url,img=b.img,author=b.author.name,genres=genres)
#     return render_template (
#         "edit-book.html",
#         book =b, form=f)

# @app.route("/delete/book/<int:id>")
# def delete_book(id):
#     if not current_user.is_authenticated:
#         next="delete_book"
#         id=id
#         return redirect(url_for("login",next=next,id=id))
#     b = get_book(id)
#     #supprime le livre du genre
#     supress_book_genres(id)
#     db.session.delete(b)
#     db.session.commit()
#     return redirect(url_for("home"))
# @app.route("/detail/genre/<int:id>")
# def detail_genre(id):
#     g = get_genre(id)
#     books=get_genre_books(id)
#     return render_template("detail-genre.html",genre=g,books=books)
# @app.route("/add/genre/")
# def add_genre():
#     if not current_user.is_authenticated:
#         next="add_genre"
#         return redirect(url_for("login",next=next))
#     return render_template("add-genre.html",form=GenreForm(id=None,name=None))
# @app.route("/save/genre/", methods =("POST",))
# def save_genre():
#     f = GenreForm()
#     if f.validate_on_submit():
#         if f.id.data:
#             g = get_genre(f.id.data)
#             g.name = f.name.data
#             db.session.commit()
#             return redirect(url_for("detail_genre", id=g.id ))
#         else:
#             #recupere l'id du dernier genre
#             id =get_nb_genres()+1  
#             g = Genre(id=id,name=f.name.data)
#             db.session.add(g)
#             db.session.commit()
#             return redirect(url_for("detail_genre", id=g.id ))
#     return render_template("add-genre.html",form=f)
# @app.route("/edit/genre/<int:id>")
# def edit_genre(id):
#     if not current_user.is_authenticated:
#         next="edit_genre"
#         id=id
#         return redirect(url_for("login",next=next,id=id))
#     g = get_genre(id)
#     f = GenreForm(id=g.id,name=g.name)
#     return render_template("add-genre.html",form=f)
# @app.route("/delete/genre/<int:id>")
# def delete_genre(id):
#     if not current_user.is_authenticated:
#         next="delete_genre"
#         id=id
#         return redirect(url_for("login",next=next,id=id))
#     g = get_genre(id)
#     #supprime le genre des livres
#     for book in get_genre_books(id):
#         remove_genre_from_book(book.id,id)
#     db.session.delete(g)
#     db.session.commit()
#     return redirect(url_for("home"))
# @app.route("/search/", methods =("POST",))
# def search():
#     #recupere la valeur du champ de recherche
#     search = request.form.get("search")
#     #recupere les livres dont le titre contient la valeur de recherche
#     books = Book.query.filter(Book.title.like("%"+search+"%")).all()
#     authors = Author.query.filter(Author.name.like("%"+search+"%")).all()
#     return render_template( "search-result.html", books=books,authors=authors)

# @app.route ("/login/", methods =("GET","POST",))
# def login():
#     f = LoginForm ()
#     if not f.is_submitted():
#         f.next.data = request.args.get("next")
#         f.id.data = request.args.get("id")
#     elif f.validate_on_submit():
#         user = f.get_authenticated_user()
#         if user is None and User.query.filter_by(username=f.username.data).first() is None:
#             f.username.errors.append("Unknown username")
#             return render_template (
#             "login.html",
#             form=f)
#         elif user is None:
#             f.password.errors.append("Invalid password")
#             return render_template (
#             "login.html",
#             form=f)
#         else:
#             login_user(user)
#             next = f.next.data
#             id = f.id.data
#             if next=="" or next is None or not next:
#                 next = "home"
#             elif next=="edit_user":
#                 url=url_for(next,name=user.username)
#             if id:
#                 url=url_for(next,id=id)
#             else:
#                 url=url_for(next)
#             return redirect(url)
#     return render_template (
#     "login.html",
#     form=f)
# @app.route("/register/", methods =("GET","POST",))
# def register():
#     f = RegisterForm ()
#     if f.validate_on_submit():
#         if User.query.filter_by(username=f.username.data).first():
#             f.username.errors.append("This username is already taken")
#             return render_template (
#             "register.html",
#             form=f)
#         if f.password.data != f.confirm.data:
#             f.confirm.errors.append("The passwords do not match")
#             return render_template (
#             "register.html",
#             form=f)
#         m =sha256()
#         m.update(f.password.data.encode())
#         u = User(username =f.username.data , password=m.hexdigest ())
#         db.session.add(u)
#         db.session.commit()
#         login_user(u)
#         return redirect(url_for("home"))
#     return render_template (
#     "register.html",
#     form=f)
# @app.route("/edit/user/<name>", methods =("GET","POST",))
# def edit_user(name):
#     f=EditUserForm()
#     if not current_user.is_authenticated:
#         next="edit_user"
#         return redirect(url_for("login",next=next))
#     if f.validate_on_submit():
#         if User.query.get(name).username != f.username.data:
#             f.username.errors.append("Username error")
#             return render_template (
#             "edit-user.html",
#             form=f)
#         if f.newpsswd.data != f.confirm.data:
#             f.confirm.errors.append("The passwords do not match")
#             return render_template (
#             "edit-user.html",
#             form=f)
#         m=sha256()
#         m.update (f.password.data.encode())
#         if User.query.get(name).password != m.hexdigest():
#             f.password.errors.append("Invalid password")
#             return render_template (
#             "edit-user.html",
#             form=f)
#         m = sha256()
#         m.update(f.newpsswd.data.encode())
#         u = User.query.get(name)
#         u.password = m.hexdigest()
#         db.session.commit()
#         return redirect(url_for("home"))
#     return render_template (
#     "edit-user.html",
#     form=f,name=name)
# @app.route("/logout/")
# def logout():
#     logout_user()
#     return redirect(url_for('home'))


@app.route("/Connexion/<origin>", methods = ("POST",))
def Connexion(origin):
    f = LoginForm()
    if f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            return redirect(url_for("Acceuil"))
    if origin == "Admin":
        return redirect(url_for("connexionAdm"))
    else:
        return redirect(url_for("connexionProf"))

