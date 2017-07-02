## Session Data

# Imports
import sys
import random
import string

# Author
__author__ = 'aje'

class SessionDAO:
    # The session Data Access Object handles interactions with the sessions collection
    def __init__(self, database):
        self.db = database
        self.sessions = database.sessions

    # will start a new session id by adding a new document to the sessions collection returns the sessionID or None
    def start_session(self, username):
        # will start a new session id by adding a new document to the sessions collection returns the sessionID or None
        session_id = self.get_random_str(32)
        session = {'username': username, '_id': session_id}

        # Exception Handling
        try:
            self.sessions.insert_one(session)
        except:
            print("Unexpected error on start_session:", sys.exc_info()[0])
            return None

        return str(session['_id'])

    def end_session(self, session_id):
        # will send a new user session by deleting from sessions table
        if session_id is None:
            return
        self.sessions.delete_one({'_id': session_id})
        return

    
    def get_session(self, session_id):
        # if there is a valid session, it is returned
        if session_id is None:
            return None

        session = self.sessions.find_one({'_id': session_id})
        return session

    def get_username(self, session_id):
        # get the username of the current session, or None if the session is not valid
        session = self.get_session(session_id)
        if session is None:
            return None
        else:
            return session['username']

    def get_random_str(self, num_chars):
        random_string = ""
        for i in range(num_chars):
            random_string = random_string + random.choice(string.ascii_letters)
        return random_string
