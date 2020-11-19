import calendar
import pickle
data_data = calendar.calendar(2020)

with open("data.txt", 'wb') as f:
    pickle.dump(data_data, f)
