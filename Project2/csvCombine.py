import pandas as pd
import glob
import os

path = r'/home/eligabel/redditStuff/my-dataset/11/antifeminists/'
all_files = glob.glob(os.path.join(path, "/*.csv"))

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

