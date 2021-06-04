





# Histogram shows the frequency of each value. Here frequency is the number of times each value appears.
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

filename = "C:/Users/Arjun Janamatti/PycharmProjects/thinkstats_book/Data/preg_df.pickle"

with open(filename, 'rb') as read_file:
    data = pickle.load(read_file)

data = data[data['prglength'] < 51]
data = data[data['birthwgt_lb'] < 51]
print(data['outcome'].value_counts())

print(data.columns)
selected_variables_data = data.copy()
def data_cleaning():
    selected_variables_data['agepreg'] = selected_variables_data['agepreg'].apply(lambda x: x / 100)
    na_vals = [97, 98, 99]
    selected_variables_data.loc[selected_variables_data['birthwgt_lb'] > 20, 'birthwgt_lb'] = np.nan
    selected_variables_data['birthwgt_lb'] = selected_variables_data['birthwgt_lb'].apply(lambda x:x if x not in na_vals else np.nan)
    selected_variables_data['birthwgt_oz'] = selected_variables_data['birthwgt_oz'].apply(lambda x:x if x not in na_vals else np.nan)
    selected_variables_data['totalwgt_lb'] = selected_variables_data['birthwgt_lb'] + (selected_variables_data[
        'birthwgt_oz'] / 16.0)
    return selected_variables_data

data = data_cleaning()

##### For LIVE birth

def LiveBirthHistogram(data):
    # selecting only outcome ==1 which is live birth
    data_live = data[data['outcome'] == 1]

    ##### PREGRNANCY LENGTH HISTOGRAM
    hist_prglength = dict(data_live['prglength'].value_counts().sort_index())

    # plt.bar(hist_prglength.keys(), hist_prglength.values())
    # plt.xlabel('Pregnancy Length in Weeks')
    # plt.ylabel('Frequency')
    # plt.title('Live Birth Histogram')
    # plt.show()

    ##### Just born baby weight histogram
    hist_prglength = dict(data_live['birthwgt_lb'].value_counts().sort_index())

    plt.bar(hist_prglength.keys(), hist_prglength.values())
    plt.xlabel('Weight in lbs')
    plt.ylabel('Frequency')
    plt.title('Weight in lbs of new born baby')
    plt.show()

def NotLiveBirthHistogram(data):
    # selecting only outcome ==1 which is live birth
    data_live = data[data['outcome'] != 1]
    hist_prglength = dict(data_live['prglength'].value_counts().sort_index())

    plt.bar(hist_prglength.keys(), hist_prglength.values())
    plt.xlabel('Pregnancy Length in Weeks')
    plt.ylabel('Frequency')
    plt.title('Live Birth Histogram')
    plt.show()


LiveBirthHistogram(data)

# NotLiveBirthHistogram(data)

# From the above it is observed, when Live birth has more frequency in week 38 to 42, whereas otherwise more frequency is for week 10 to 15