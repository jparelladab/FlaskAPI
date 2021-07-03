# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from model import *
# import json

# # engine = create_engine("mysql://<USERNAME>:<PASSWORD>@<HOST>/Test")
# # Base.metadata.bind = engine
# # DBSession = sessionmaker(bind=engine)
# session = DBSession()

# def GetBookList():
#     books = session.query(Books).all()

#     bookList = []
#     for item in books:
#         book = {
#             "id": item.BookId,
#             "name": item.BookName,
#             "author": item.BookAuthor
#         }

#         bookList.append(book)
#     return json.dumps(bookList)

# def InsertBook(book):
#     newBook = Books(
#         BookName = book["name"],
#         BookAuthor = book["author"]
#     )

#     session.add(newBook)
#     session.commit()
#     session.close()

#     return json.dumps({"status": "Added", "book": book["name"], "author": book["author"]})

# def UpdateBook(book):
#     bookToUpdate = session.query(Books).filter(Books.BookName == book["name"]).one()

#     bookToUpdate.BookName = book["name"]
#     bookToUpdate.BookAuthor = book["author"]

#     session.commit()
#     session.close()

#     return json.dumps({"status": "Updated", "book": book["name"], "author": book["author"]})
