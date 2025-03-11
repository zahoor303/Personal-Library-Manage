# import sqlite3
# import streamlit as st
# import base64

# class LibraryManager:
#     def __init__(self, db_name="library.db"):
#         self.conn = sqlite3.connect(db_name)
#         self.cursor = self.conn.cursor()
#         self.create_table()

#     def create_table(self):
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
#                                 id INTEGER PRIMARY KEY,
#                                 title TEXT NOT NULL,
#                                 author TEXT NOT NULL,
#                                 year INTEGER,
#                                 genre TEXT)
#                             ''')
#         self.conn.commit()

#     def add_book(self, title, author, year, genre):
#         self.cursor.execute("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)",
#                             (title, author, year, genre))
#         self.conn.commit()

#     def view_books(self):
#         self.cursor.execute("SELECT * FROM books")
#         return self.cursor.fetchall()

#     def search_books(self, keyword):
#         self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
#         return self.cursor.fetchall()

#     def delete_book(self, book_id):
#         self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
#         self.conn.commit()

#     def update_book(self, book_id, title, author, year, genre):
#         self.cursor.execute("""UPDATE books SET title = ?, author = ?, year = ?, genre = ? WHERE id = ?""",
#                             (title, author, year, genre, book_id))
#         self.conn.commit()

#     def close(self):
#         self.conn.close()

# # Streamlit UI
# st.set_page_config(page_title="Personal Library Manager", page_icon="📚", layout="centered")

# # CSS Styling
# st.markdown("""
#     <style>
#     body {
#         background-color: #f5f5f5;
#     }
#     .stApp {
#         background: linear-gradient(135deg, #ff9a9e 10%, #fad0c4 100%);
#         padding: 20px;
#         border-radius: 15px;
#     }
#     .stButton>button {
#         background-color: #ff7eb3;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 20px;
#     }
#     .stTextInput>div>div>input {
#         border-radius: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.title("📚 Personal Library Manager")
# manager = LibraryManager()

# menu = ["Add Book", "View Books", "Search Book", "Delete Book", "Update Book"]
# choice = st.sidebar.selectbox("Menu", menu)

# if choice == "Add Book":
#     st.subheader("📖 Add a New Book")
#     title = st.text_input("Book Title")
#     author = st.text_input("Author")
#     year = st.number_input("Publication Year", min_value=0, max_value=2100, step=1)
#     genre = st.text_input("Genre")
#     if st.button("Add Book"):
#         manager.add_book(title, author, year, genre)
#         st.success("Book added successfully!")

# elif choice == "View Books":
#     st.subheader("📚 View Books")
#     books = manager.view_books()
#     if books:
#         for book in books:
#             st.write(f"**ID:** {book[0]} | **Title:** {book[1]} | **Author:** {book[2]} | **Year:** {book[3]} | **Genre:** {book[4]}")
#     else:
#         st.info("No books found.")

# elif choice == "Search Book":
#     st.subheader("🔍 Search Books")
#     keyword = st.text_input("Enter keyword")
#     if st.button("Search"):
#         books = manager.search_books(keyword)
#         if books:
#             for book in books:
#                 st.write(f"**ID:** {book[0]} | **Title:** {book[1]} | **Author:** {book[2]} | **Year:** {book[3]} | **Genre:** {book[4]}")
#         else:
#             st.warning("No books found.")

# elif choice == "Delete Book":
#     st.subheader("🗑 Delete a Book")
#     book_id = st.number_input("Enter Book ID to delete", min_value=1, step=1)
#     if st.button("Delete Book"):
#         manager.delete_book(book_id)
#         st.success("Book deleted successfully!")

# elif choice == "Update Book":
#     st.subheader("✏️ Update Book Information")
#     book_id = st.number_input("Enter Book ID to update", min_value=1, step=1)
#     title = st.text_input("New Title")
#     author = st.text_input("New Author")
#     year = st.number_input("New Publication Year", min_value=0, max_value=2100, step=1)
#     genre = st.text_input("New Genre")
#     if st.button("Update Book"):
#         manager.update_book(book_id, title, author, year, genre)
#         st.success("Book updated successfully!")

# manager.close()




# import sqlite3
# import streamlit as st
# import base64

# class LibraryManager:
#     def __init__(self, db_name="library.db"):
#         self.conn = sqlite3.connect(db_name)
#         self.cursor = self.conn.cursor()
#         self.create_table()

#     def create_table(self):
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
#                                 id INTEGER PRIMARY KEY,
#                                 title TEXT NOT NULL,
#                                 author TEXT NOT NULL,
#                                 year INTEGER,
#                                 genre TEXT)
#                             ''')
#         self.conn.commit()

#     def add_book(self, title, author, year, genre):
#         self.cursor.execute("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)",
#                             (title, author, year, genre))
#         self.conn.commit()

#     def view_books(self):
#         self.cursor.execute("SELECT * FROM books")
#         return self.cursor.fetchall()

#     def search_books(self, keyword):
#         self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
#         return self.cursor.fetchall()

#     def delete_book(self, book_id):
#         self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
#         self.conn.commit()

#     def update_book(self, book_id, title, author, year, genre):
#         self.cursor.execute("""UPDATE books SET title = ?, author = ?, year = ?, genre = ? WHERE id = ?""",
#                             (title, author, year, genre, book_id))
#         self.conn.commit()

#     def close(self):
#         self.conn.close()

# # Streamlit UI
# st.set_page_config(page_title="Personal Library Manager", page_icon="📚", layout="wide")

# # CSS Styling
# st.markdown("""
#     <style>
#     body {
#         background-color: #B7B1F2;
#     }
#     .stApp {
#         background: #B7B1F2;
#         padding: 20px;
#         border-radius: 15px;
#         color: black;
#     }
#     .stButton>button {
#         background-color: #6A5ACD !important;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 20px;
#         border: none;
#     }
#     .stTextInput>div>div>input {
#         border-radius: 10px;
#         padding: 10px;
#         border: 2px solid #8A7EF5;
#         background-color: rgba(255, 255, 255, 0.9);
#         color: black;
#     }
#     .stSidebar {
#         background-color: #D9D4FF;
#         color: black;
#         padding: 20px;
#         border-radius: 10px;
#     }
#     .stDataFrame {
#         background-color: #ffffff;
#         color: black;
#         border-radius: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.title("📚 Personal Library Manager")
# manager = LibraryManager()

# menu = ["Add Book", "View Books", "Search Book", "Delete Book", "Update Book"]
# choice = st.sidebar.selectbox("📖 Menu", menu)

# if choice == "Add Book":
#     st.subheader("➕ Add a New Book")
#     title = st.text_input("📖 Book Title")
#     author = st.text_input("✍️ Author")
#     year = st.number_input("📅 Publication Year", min_value=0, max_value=2100, step=1)
#     genre = st.text_input("🎭 Genre")
#     if st.button("✅ Add Book"):
#         manager.add_book(title, author, year, genre)
#         st.success("Book added successfully!")

# elif choice == "View Books":
#     st.subheader("📚 View Books")
#     books = manager.view_books()
#     if books:
#         st.table(books)
#     else:
#         st.info("No books found.")

# elif choice == "Search Book":
#     st.subheader("🔎 Search Books")
#     keyword = st.text_input("🔍 Enter keyword")
#     if st.button("🔎 Search"):
#         books = manager.search_books(keyword)
#         if books:
#             st.table(books)
#         else:
#             st.warning("No books found.")

# elif choice == "Delete Book":
#     st.subheader("🗑 Delete a Book")
#     book_id = st.number_input("Enter Book ID to delete", min_value=1, step=1)
#     if st.button("❌ Delete Book"):
#         manager.delete_book(book_id)
#         st.success("Book deleted successfully!")

# elif choice == "Update Book":
#     st.subheader("✏️ Update Book Information")
#     book_id = st.number_input("Enter Book ID to update", min_value=1, step=1)
#     title = st.text_input("📝 New Title")
#     author = st.text_input("✍️ New Author")
#     year = st.number_input("📅 New Publication Year", min_value=0, max_value=2100, step=1)
#     genre = st.text_input("🎭 New Genre")
#     if st.button("🔄 Update Book"):
#         manager.update_book(book_id, title, author, year, genre)
#         st.success("Book updated successfully!")

# manager.close()

import sqlite3
import streamlit as st
import base64

class LibraryManager:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY,
                                title TEXT NOT NULL,
                                author TEXT NOT NULL,
                                year INTEGER,
                                genre TEXT)
                            ''')
        self.conn.commit()

    def add_book(self, title, author, year, genre):
        self.cursor.execute("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)",
                            (title, author, year, genre))
        self.conn.commit()

    def view_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def search_books(self, keyword):
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
        return self.cursor.fetchall()

    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()

    def update_book(self, book_id, title, author, year, genre):
        self.cursor.execute("""UPDATE books SET title = ?, author = ?, year = ?, genre = ? WHERE id = ?""",
                            (title, author, year, genre, book_id))
        self.conn.commit()

    def close(self):
        self.conn.close()

# Streamlit UI
st.set_page_config(page_title="Personal Library Manager", page_icon="📚", layout="wide")

# CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #8E806A;
    }
    .stApp {
        background: #8E806A;
        padding: 20px;
        border-radius: 15px;
        color: black;
    }
    .stButton>button {
        background-color: #5C5346 !important;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
        border: 2px solid #A89F91;
        background-color: rgba(255, 255, 255, 0.9);
        color: black;
    }
    .stSidebar {
        background-color: #D7C7B6;
        color: black;
        padding: 20px;
        border-radius: 10px;
    }
    .stDataFrame {
        background-color: #ffffff;
        color: black;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Personal Library Manager")
manager = LibraryManager()

menu = ["Add Book", "View Books", "Search Book", "Delete Book", "Update Book"]
choice = st.sidebar.selectbox("📖 Menu", menu)

if choice == "Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("📖 Book Title")
    author = st.text_input("✍️ Author")
    year = st.number_input("📅 Publication Year", min_value=0, max_value=2100, step=1)
    genre = st.text_input("🎭 Genre")
    if st.button("✅ Add Book"):
        manager.add_book(title, author, year, genre)
        st.success("Book added successfully!")

elif choice == "View Books":
    st.subheader("📚 View Books")
    books = manager.view_books()
    if books:
        st.table(books)
    else:
        st.info("No books found.")

elif choice == "Search Book":
    st.subheader("🔎 Search Books")
    keyword = st.text_input("🔍 Enter keyword")
    if st.button("🔎 Search"):
        books = manager.search_books(keyword)
        if books:
            st.table(books)
        else:
            st.warning("No books found.")

elif choice == "Delete Book":
    st.subheader("🗑 Delete a Book")
    book_id = st.number_input("Enter Book ID to delete", min_value=1, step=1)
    if st.button("❌ Delete Book"):
        manager.delete_book(book_id)
        st.success("Book deleted successfully!")

elif choice == "Update Book":
    st.subheader("✏️ Update Book Information")
    book_id = st.number_input("Enter Book ID to update", min_value=1, step=1)
    title = st.text_input("📝 New Title")
    author = st.text_input("✍️ New Author")
    year = st.number_input("📅 New Publication Year", min_value=0, max_value=2100, step=1)
    genre = st.text_input("🎭 New Genre")
    if st.button("🔄 Update Book"):
        manager.update_book(book_id, title, author, year, genre)
        st.success("Book updated successfully!")

manager.close()