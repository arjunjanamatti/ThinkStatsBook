





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
    # Histogram for birthweight in pounds looks like normal distribution

    hist_prglength = dict(data_live['birthwgt_oz'].value_counts().sort_index())

    plt.bar(hist_prglength.keys(), hist_prglength.values())
    plt.xlabel('Weight in ounces')
    plt.ylabel('Frequency')
    plt.title('Weight in ounces of new born baby')
    plt.show()
    # Histogram for birthweight in pounds looks like uniform distribution

    hist_prglength = dict(data_live['agepreg'].value_counts().sort_index())

    plt.bar(hist_prglength.keys(), hist_prglength.values())
    plt.xlabel("Mother's age at end of pregnancy")
    plt.ylabel('Frequency')
    plt.title("Mother's age at end of pregnancy")
    plt.show()
    # Histogram for mothers age at end of pregnancy also looks like normal distribution with bulk of mothers in their 20's and very few in 30's or 40's
    hist_prglength = dict(data_live['prglength'].value_counts().sort_index())

    plt.bar(hist_prglength.keys(), hist_prglength.values())
    plt.xlabel('Length of pregnancy in weeks')
    plt.ylabel('Frequency')
    plt.title('Length of pregnancy in weeks')
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


# LiveBirthHistogram(data)

# NotLiveBirthHistogram(data)

# From the above it is observed, when Live birth has more frequency in week 38 to 42, whereas otherwise more frequency is for week 10 to 15

##### Outliers
# Outliers are the extreme values which might be errors in measurement or might be accurate reports of rare events
# For example if we the pregnancy length in terms of weeks, there is very less chance for successful birth for baby to be borth
# within 10 weeks
print(data['prglength'].value_counts().sort_index())
# Also beyond 42 weeks, doctors recommend induced labor and this is also very unlikely.
# will consider the birth of babies after 27 weeks

data_1 = data.copy()
data_1 = data_1[data_1['prglength'] > 26]
print(data_1['prglength'].value_counts().sort_index())


##### FIRST BABIES
data_live = data_1[data_1['outcome'] == 1]
others = data_1[data_1['outcome'] != 1]
hist_prglength_live = dict(data_live['prglength'].value_counts().sort_index())
hist_prglength_others = dict(others['prglength'].value_counts().sort_index())

ax = plt.subplot(111)
w = 0.3
ax.bar(hist_prglength_live.keys(), hist_prglength_live.values(), width=w, color='b', align='center')
ax.bar(hist_prglength_others.keys(), hist_prglength_others.values(), width=w, color='r', align='center')
# ax.xlabel('Pregnancy Length in Weeks')
# ax.ylabel('Frequency')
# ax.title('Babies Histogram')

# plt.bar(hist_prglength_live.keys(), hist_prglength_live.values())
# plt.bar(hist_prglength_others.keys(), hist_prglength_others.values())
# plt.xlabel('Pregnancy Length in Weeks')
# plt.ylabel('Frequency')
# plt.title('Babies Histogram')
# plt.bar(hist_prglength_others.keys(), hist_prglength_others.values())
plt.show()

