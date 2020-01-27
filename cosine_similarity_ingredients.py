import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import IPython

class IngredientClassifier():
    def __init__(self, link2ingredient_str):
        """ Build a matrix where each row is a recipe vector

            Args:
                takes a dictionary link2ingredient of {recipe_link1: string of ingredients} 
                    
        """
        self.links = []
        self.text = []

        for k, v in link2ingredient_str.items():
            self.links.append(k)
            self.text.append(v)

        self.vectorizer = CountVectorizer(self.text)
        self.vectorizer.fit(self.text)
        self.corpus_matrix = self.vectorizer.transform(self.text).toarray()
        self.normalized_corpus_matrix = self.corpus_matrix/np.linalg.norm(self.corpus_matrix)


    def query(self, query_str, normalized=True):
        """ 
            Args:
                takes a ingredient string from user input

            Returns:
                Link of closest match based on dot product which in this case is the same as cosine similarity
                    
        """

        self.query_vector = self.vectorizer.transform([query_str]).toarray()
        self.normalized_query_vector = self.query_vector/np.linalg.norm(self.query_vector)

        if np.max(self.query_vector) == 0:
            raise Exception("Query not in corpus")


        if normalized:
            scores = np.dot(self.normalized_query_vector, self.normalized_corpus_matrix.T)

        else:
            # Pre-normalization relates the term frequency, will skew towards repeated ingredient words
            scores = np.dot(self.query_vector, self.corpus_matrix.T)

             
        high_score_idx = np.argmax(scores)
        return self.links[high_score_idx]
