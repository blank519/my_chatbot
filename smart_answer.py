import nmslib # study 
from sentence_transformers import SentenceTransformer, util #study 
import pandas as pd 
from sys import argv
import os
 
class SmartAnswer(object):

    THRESHOLD = 0.6

    def __init__ (self, fname):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self._load_base(fname)
        self.index = self._create_vector()

    def _load_base(self, fname):
        """
        INPUT: csv, 
        RETURN
          self.df_corpus  ["question", "answer"]
        """
        if os.path.isfile(fname):
            self.df_corpus = pd.read_csv(fname)
            self.df_corpus['Question'] = self.df_corpus['Question'].apply(lambda x: self._clean(x))
        else:
            raise Exception(f"Invalid file name {fname}")


    def _clean(self, question):
        """
        Cleans the question by removing extra whitespace and the "?" from the end of the string and turning the string to lowercase.
        """
        question = question.strip().lower()
        if question.endswith("?"):
            question = question[:-1]
        return question


    def _create_vector(self):
        """
        
        """
        self.index = nmslib.init(method='hnsw', space='cosinesimil')
        self.index.addDataPointBatch(self.model.encode(self.df_corpus['Question'].tolist(), convert_to_tensor=True))
        self.index.createIndex({'post': 2}, print_progress=False)
        return self.index


    def answer(self, question):
        """
        Matches the question with
        """
        question = self._clean(question)
        res = self.index.knnQuery(self.model.encode(question, convert_to_tensor=True), k=3)    
        
        for i, sim in zip(res[0].tolist(), res[1].tolist()):
            print("similarity:%f\t%s"%(1. - sim, self.df_corpus.iloc[i]['Question']))
        
        if 1-res[1][0] < self.THRESHOLD:
            return None
        return [self.df_corpus.iloc[res[0][0]]['Question'], self.df_corpus.iloc[res[0][0]]['Answer']]


if __name__ == "__main__":
    fname = argv[1]
    sa = smartAnswer(fname)
    print(sa.answer(argv[2]))
