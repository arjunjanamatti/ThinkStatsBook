





# Histogram shows the frequency of each value. Here frequency is the number of times each value appears.
import pickle
import matplotlib.pyplot as plt
import pandas as pd

filename = "C:/Users/Arjun Janamatti/PycharmProjects/thinkstats_book/Data/preg_df.pickle"

with open(filename, 'rb') as read_file:
    data = pickle.load(read_file)

data = data[data['prglength'] < 51]

##### For LIVE birth
# selecting only outcome ==1 which is live birth
data_live = data[data['outcome'] == 1]

# Histogram for the pregnancy length
hist_prglength = dict(data_live['prglength'].value_counts().sort_index())

plt.bar(hist_prglength.keys(), hist_prglength.values())
plt.xlabel('Pregnancy Length in Weeks')
plt.ylabel('Frequency')
plt.title('Live Birth Histogram')
plt.show()
