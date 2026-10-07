from flask import Flask, render_template, jsonify, request, url_for, redirect, abort

app = Flask(__name__)

# danh sach sach
books = [
    {
        "id": 1,
        "title": "Lap trinh Python co ban",
        "author": "Nguyen Van A",
        "year": 2024,
        "category": "Lap trinh",
        "available": True
    },
    {
        "id": 2,
        "title": "Flask Web Development",
        "author": "Miguel Grinberg",
        "year": 2023,
        "category": "Lap trinh",
        "available": True
    },
    {
        "id": 3,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "category": "Lap trinh",
        "available": False
    },
    {
        "id": 4,
        "title": "Dac Nhan Tam",
        "author": "Dale Carnegie",
        "year": 1936,
        "category": "Ky nang",
        "available": True
    }
]


# trang chu
@app.route("/")
def home():
    return redirect(url_for("books_page"))


# danh sach sach + loc theo the loai
@app.route("/books")
def books_page():
    category = request.args.get("category")

    if category:
        danh_sach = []

        for book in books:
            if book["category"] == category:
                danh_sach.append(book)
    else:
        danh_sach = books

    # lay danh sach the loai
    categories = []

    for book in books:
        if book["category"] not in categories:
            categories.append(book["category"])

    return render_template(
        "books.html",
        books=danh_sach,
        categories=categories,
        selected_category=category
    )


# chi tiet sach
@app.route("/books/<int:book_id>")
def book_detail(book_id):
    book = None

    for item in books:
        if item["id"] == book_id:
            book = item
            break

    if book is None:
        abort(404)

    return render_template(
        "book_detail.html",
        book=book
    )


# API - lay tat ca sach
@app.route("/api/books")
def api_books():
    return jsonify(books)


# API - lay mot sach theo id
@app.route("/api/books/<int:book_id>")
def api_book_detail(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)

    return jsonify({
        "error": "Khong tim thay sach"
    }), 404


# xu ly loi 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)