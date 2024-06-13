import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import uuid

# DB Section

# Add a book function
def add_book(conn, book):
    query = '''INSERT INTO book_database(title,author,read)
                VALUES(?,?,?)'''
    cursor = conn.cursor()
    cursor.execute(query, book)
    conn.commit()
    return cursor.lastrowid

def remove_book(conn, book):
    query = '''DELETE FROM book_database WHERE title = %s '''
    cursor = conn.cursor()
    cursor.execute(query, book)
    conn.commit()
    print(cursor.rowcount, "Book removed")

# Helper functions

#helper to remove a book
def remove_book(book_id):
    for book in BOOKS:
        BOOKS.remove(book)
        return True
    return False


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# GET/ADD Book(s)
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

# Update book
@app.route('/books/<book_id>', methods=['PUT'])
def single_book(book_id):
    response_object = {'status':'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    return jsonify(response_object)

def main():
    try: 
        with sqlite3.connect('book_database.db') as conn:
    
            # Add a new book
            book = ('Tester Jones: The battle of SQLite', 'Tester Jones','True')
            book_id = add_book(conn, book)
            print(f'Create a new book with the id{book_id}')

    # Handle Errors with db
    except sqlite3.Error as error:
        print('Error occured - ', error)

    #Close DB connection irrespective of success or failure
    finally: 

        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection Closed')


if __name__ == '__main__':
    app.run()
