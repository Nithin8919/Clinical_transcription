import datetime

class Transcription:
    def __init__(self, db):
        self.collection = db['transcriptions']

    def save(self, user_id, raw_transcription, soap_note):
        doc = {
            'user_id': user_id,
            'raw_transcription': raw_transcription,
            'soap_note': soap_note,
            'created_at': datetime.datetime.utcnow()
        }
        return self.collection.insert_one(doc)

    def get_all(self, user_id):
        return list(self.collection.find({'user_id': user_id}))