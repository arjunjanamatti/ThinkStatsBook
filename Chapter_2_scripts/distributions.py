





# Histogram shows the frequency of each value. Here frequency is the number of times each value appears.
import pickle
from glob import glob

filename = "C:/Users/Arjun Janamatti/PycharmProjects/thinkstats_book/Data/preg_df.pickle"

with open(filename, 'rb') as read_file:
    data = pickle.load(read_file)

print(data['prglength'].value_counts().index)
print(dict(data['prglength'].value_counts()))
print(list(data['prglength'].value_counts()))

hist = {}
for x in data['prglength']:
    hist[x] = hist.get(x, 0) + 1

print(hist)

