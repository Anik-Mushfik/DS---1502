import pandas as pd

data = {
    'Name': ['Tamanna', 'Faysal', 'Tarek', 'Raisa', 'Ismail'],
    'Age': [24,27,22,32,24],
    'City': ['Dhaka', 'Cumilla', 'Bagura', 'Khulna', 'Barishal']

}

df = pd.DataFrame(data)

print(df)