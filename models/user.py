import hashlib

class User:
    def __init__(self, db):
        self.collection = db['users']

    def create(self, email, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = {
            'email': email,
            'password_hash': password_hash,
            'created_at': datetime.datetime.utcnow()
        }
        return self.collection.insert_one(user).inserted_id

    def authenticate(self, email, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = self.collection.find_one({'email': email, 'password_hash': password_hash})
        return user