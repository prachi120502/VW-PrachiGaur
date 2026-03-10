from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Prachi123#@localhost:3307/library_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ------------------------------
# Book Model
# ------------------------------
class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    copies = db.Column(db.Integer, nullable=False)



# Create tables manually

with app.app_context():
    db.create_all()



# Add Book

@app.route('/books', methods=['POST'])
def add_book():

    data = request.get_json()

    new_book = Book(
        title=data["title"],
        author=data["author"],
        copies=data["copies"]
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify({"message": "Book added successfully"})



# Display All Books

@app.route('/books', methods=['GET'])
def get_books():

    books = Book.query.all()

    result = []

    for book in books:
        result.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "copies": book.copies
        })

    return jsonify(result)



# Borrow Book

@app.route('/borrow/<int:book_id>', methods=['POST'])
def borrow_book(book_id):

    book = Book.query.get(book_id)

    if not book:
        return jsonify({"message": "Book not found"}), 404

    if book.copies == 0:
        return jsonify({"message": "Book unavailable"}), 400

    book.copies -= 1
    db.session.commit()

    return jsonify({
        "message": "Book borrowed successfully",
        "remaining_copies": book.copies
    })



# Unavailable Books

@app.route('/books/unavailable', methods=['GET'])
def unavailable_books():

    books = Book.query.filter(Book.copies == 0).all()

    result = []

    for book in books:
        result.append({
            "id": book.id,
            "title": book.title,
            "author": book.author
        })

    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True)