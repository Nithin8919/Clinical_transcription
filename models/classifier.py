import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

class SOAPClassifier:
    def __init__(self):
        self.categories = ['subjective', 'objective', 'assessment', 'plan']
        self.tokenizer = Tokenizer(num_words=100)
        self.max_length = 20
        
        # Training data
        training_texts = [
            "Patient reports chest pain",
            "Blood pressure is 120/80",
            "Likely hypertension",
            "Prescribe medication"
        ]
        training_labels = [0, 1, 2, 3]
        
        self.tokenizer.fit_on_texts(training_texts)
        sequences = self.tokenizer.texts_to_sequences(training_texts)
        padded_sequences = pad_sequences(sequences, maxlen=self.max_length)
        
        self.model = Sequential([
            Embedding(100, 16, input_length=self.max_length),
            GlobalAveragePooling1D(),
            Dense(16, activation='relu'),
            Dense(4, activation='softmax')
        ])
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.model.fit(padded_sequences, np.array(training_labels), epochs=10, verbose=0)

    def classify(self, transcription):
        sentences = transcription.split('.')
        soap_note = {'subjective': '', 'objective': '', 'assessment': '', 'plan': ''}
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            sequence = self.tokenizer.texts_to_sequences([sentence])
            padded = pad_sequences(sequence, maxlen=self.max_length)
            prediction = self.model.predict(padded, verbose=0)
            category_idx = np.argmax(prediction)
            soap_note[self.categories[category_idx]] += sentence + '. '
        
        return {k: v.strip() for k, v in soap_note.items()}