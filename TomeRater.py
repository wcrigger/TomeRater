#!/usr/bin/env python3
""" 
Codecademy Tome Rater Python Project
"""
__author__ = "Warren Crigger [warren.crigger@gmail.com]"
__copyright__ = "Copyright 2019 Warren Crigger.  All rights reserved."
__credits__ = ["Codecademy"]
__license__ = "GPLv3"
__version__ = "0.1"
__revision__ = "0"
__docformat__ = "reStructuredText"

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_books_read(self):
        """ Returns number of books read """
        return len(self.books)

    def get_email(self):
        """ Return email address """
        return self.email

    def get_name(self):
        """ Return name """
        return self.name

    def change_email(self, address):
        """ Email address update """
        self.email = address
        return "User {name}'s email address has been updated to {email}".format(name=self.name,email=self.email)

    def read_book(self, book, rating=None):
        """ Add read book to dict """
        if isinstance(book, Book):
            self.books.update({book: rating})
        else:
            print("{book} does not appear to be a Book object.".format(book=book))

    def get_average_rating(self):
        """ Calculate and return average rating """
        count = 0
        total = 0
        num_books = len(self.books)
        if num_books > 0:
            for rating in self.books.values():
                if rating:
                    count += 1
                    total += rating
            average = total / count
        if count > 0:
            return average
        else:
            print("Books with ratings not found for user {user}".format(user=self.name))

    def __repr__(self):
        """ Returns name, email, read count, and average rating """
        count=0
        for item in self.books.keys():
            count += 1
        return "User {name} with email address {email} has read {count} book(s) with an average rating of {rating}".format(name=self.name,email=self.email,count=count,rating=self.get_average_rating())

    def __eq__(self, other_user):
        """ Is one of these items not like the other? """
        if isinstance(other_user, User):
            return self.name == other_user.name and self.email == other_user.get_email()
        else:
            other_user_type = type(other_user)
            print("{other_user} is not a User object, it is of type: {type}".format(other_user=other_user, type=other_user_type))

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        """ Returns title """
        return self.title

    def get_isbn(self):
        """ Returns ISBN """
        return self.isbn

    def set_isbn(self, isbn):
        """ ISBN update """
        original_isbn = self.isbn
        self.isbn = isbn
        print("Updated {book}'s ISBN from {old} to {new}".format(book=self.title,old=original_isbn,new=self.isbn))

    def add_rating(self, rating):
        """ Adds a rating if it meets criteria """
        if not rating or rating < 0 or rating > 4:
            return "Rating {rating} is not valid.  Valid ratings are between 0 and 4".format(rating=rating)
        else:
            self.ratings.append(rating)

    def get_average_rating(self):
        """ Returns average rating or prints none available """
        count = 0
        total = 0
        ratings_length = len(self.ratings)
        if ratings_length > 0:
            for rating in self.ratings:
                count += 1
                total += rating
            average = total / count
            return average
        else:
            print("There does not seem to be any ratings for {book}".format(book=self.title))

    def __eq__(self):
        """ Is one of these items not like the other? """
        if isinstance(other_book, Book):
            return self.title == other_book.title and self.isbn == other_book.isbn
        else:
            type=type(other_book)
            print("{other_book} is of type: {type}, and should be a User type".format(other_book=other_book,type=type))

    def __hash__(self):
        """ Returns hash of book """
        return hash((self.title, self.isbn))


class Fiction(Book):
    """ Fiction Book subclass """
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        """ Returns author """
        return self.author

    def __repr__(self):
        return "{book} by {author}".format(book=self.title,author=self.author)


class Non_Fiction(Book):
    """ Fiction Book subclass """
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_level(self):
        """ Returns level """
        return self.level

    def get_subject(self):
        """ Returns subject"""
        return self.subject

    def __repr__(self):
        return "{book}, a {level} level book on {subject}.".format(book=self.title,level=self.level,subject=self.subject)


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        """ Returns a book instance """
        isbn_list = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbn_list:
            print("ISBN {isbn} already exists.  Please provide a unique ISBN.".format(isbn=isbn))
        else:
            return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        """ Returns Fiction Book instance """
        isbn_list = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbn_list:
            print("ISBN {isbn} already exists.  Please provide a unique ISBN.".format(isbn=isbn))
        else:
            return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        """ Returns Non-Fiction instance """
        isbn_list = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbn_list:
            print("ISBN {isbn} already exists.  Please provide a unique ISBN.".format(isbn=isbn))
        else:
            return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        """ Adds book and rating if exists """
        if self.users.get(email):
            self.users[email].read_book(book, rating)
            self.books[book] = self.books.get(book, 0) + 1
            if rating:
                book.add_rating(rating)
        else:
            print("{email} address not found.".format(email=email))

    def add_user(self, name, email, books=None):
        """ Adds user """
        user = self.users.get(email)
        if user:
            print("{email} address already exists for user {name}.  Please use a different email address.".format(email=email,name=user.get_name()))
        else:
            self.users.update({email: User(name, email)})
            if books:
                for book in books:
                    self.add_book_to_user(book, email)

    def print_catalog(self):
        """ Prints books in dictionary """
        for book in self.books.keys():
            print(book)

    def print_users(self):
        """ Prints users in dictionary """
        for user in self.users.values():
            print(user)
	
    def most_read_book(self):
        """ Returns most read book """
        reading_max = 0
        most_reads = ""
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > reading_max:
                most_reads = book
                reading_max = rating
            else:
                continue
        return most_reads

    def highest_rated_book(self):
        """ Returns highest rated book """
        rating_max = 0
        best_rated_book = ""
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > rating_max:
                rating_max = rating
                best_rated_book = rating
            else:
                continue
        return best_rated_book

    def most_positive_user(self):
        """ Returns user with highest average rating """
        rating_max = 0
        rating_max_user = ""
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > rating_max:
                rating_max = rating
                rating_max_user = user
            else:
                continue
        return rating_max_user

    def get_n_most_read_books(self, n):
        """ Returns the number of most read books """
        if type(n) != int:
            print("The argument n = {n} is not an integer.  Try again with an integer".format(n=n))
        else:
            sorted_books = [ book for book in sorted(self.books,key=self.books.get,reverse=True)]
            return sorted_books

    def __repr__(self):
        num_books = len(self.books)
        num_users = len(self.users)
        most_read = self.most_read_book()
        highest_rated = self.highest_rated_book()
        most_positive = self.most_positive_user()
        return "Number of books: {books} books.  Number of users: {users} users.  Most read book: {most_read}. High rated book (based on average rating): {highest_rated}.  Most positive reviews: {most_positive}.".format(books=num_books,users=num_users,most_read=most_read,highest_rated=highest_rated,most_positive=most_positive)
