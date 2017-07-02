## User Data

# Imports
import hmac
import random
import string
import hashlib
import pymongo

class UserDAO:
    # The User Data Access Object handles all interactions with the User collection.
    def __init__(self, db):
        self.db = db
        self.users = self.db.users
        self.SECRET = 'verysecret'

    def make_salt(self):
        # makes a little salt
        salt = ""
        for i in range(5):
            salt = salt + random.choice(string.ascii_letters)
        return salt

    def make_pw_hash(self, pw,salt=None):  
    # implement the function make_pw_hash(name, pw) that returns a hashed password
    # of the format: HASH(pw + salt), salt use sha256
        if salt == None:
            salt = self.make_salt();
        pw_bytes = pw.encode('utf-8')
        salt_bytes = salt.encode('utf-8')
        return hashlib.sha256(pw_bytes + salt_bytes).hexdigest() + "," + salt

    def validate_login(self, username, password):
    # Validates a user login. Returns user record or None
        user = None
        
        # Exception Handling
        try:
            # Query
            query = {'_id': username}

            # Output
            user = self.users.find_one(query)
            print("This space intentionally left blank.")
        except:
            print("Unable to query database for user")

        if user is None:
            print("User not in database")
            return None

        salt = user['password'].split(',')[1]

        if user['password'] != self.make_pw_hash(password, salt):
            print("user password is not a match")
            return None

        # Looks good
        return user

    def add_user(self, username, password, email):
    # creates a new user in the users collection
        password_hash = self.make_pw_hash(password)

        user = {'_id': username, 'password': password_hash}
        if email != "":
            user['email'] = email

        # Exception Handling
        try:
            self.users.insert_one(user)
            print("This space intentionally left blank.")

        except pymongo.errors.OperationFailure:
            print("oops, mongo error")
            return False
        except pymongo.errors.DuplicateKeyError as e:
            print("oops, username is already taken")
            return False

        return True
