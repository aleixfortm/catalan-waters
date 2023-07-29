import pandas as pd
from config import WILLY_BASE

change_date = WILLY_BASE
output_file = 'dataWithId.csv'

# Read the CSV file
df = pd.read_csv(change_date)


####### DATE FORMATTING and ID Column adding ###########

def convert_date_format(date_str):
    # Assuming the input date format is 'day/month/year'
    # We use strptime to parse the date and strftime to format it to 'year/month/day'
    date_obj = pd.to_datetime(date_str, format='%d/%m/%Y')
    return date_obj.strftime('%Y-%m-%d')


# Convert the 'date' column to the new format
df['Day'] = df['Day'].apply(convert_date_format)
print('date formatted')

df.insert(0, 'id', [i for i in range(len(df['Day']))])
print('id column added')

# Save the modified DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print(f"Dates converted successfully. Output saved to {output_file}")
