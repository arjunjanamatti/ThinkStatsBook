





# Histogram shows the frequency of each value. Here frequency is the number of times each value appears.
import pickle
import matplotlib.pyplot as plt
import pandas as pd

filename = "C:/Users/Arjun Janamatti/PycharmProjects/thinkstats_book/Data/preg_df.pickle"

with open(filename, 'rb') as read_file:
    data = pickle.load(read_file)

data = data[data['prglength'] < 51]

# Histogram for the pregnancy length
hist_prglength = dict(data['prglength'].value_counts().sort_index())

print(hist_prglength)
print(min(hist_prglength.values()), max(hist_prglength.values()))
print(min(data['prglength']), max(data['prglength']))
plt.bar(hist_prglength.keys(), hist_prglength.values())
plt.show()


# check for grouping
date_list = ['25-01-2020', '25-01-2020', '26-01-2020']
name_list = ['A', 'A', 'A']
check_df = pd.DataFrame()
check_df['name_list'] = name_list
check_df['date_list'] = date_list
check_df['date_list'] = pd.to_datetime(check_df['date_list'],dayfirst=True)

print(check_df.groupby(by=['name_list'])['date_list'].count())