from sklearn import svm
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import pandas as pd

dataPath = r'C:\Users\irisv\Documents\SupplementalProject2\Data\mergedAskRed.csv'
df = pd.read_csv(dataPath)

words = df.comment_body

print(words)