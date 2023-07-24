import pandas as pd

def convert_date_format(date_str):
    # Assuming the input date format is 'day/month/year'
    # We use strptime to parse the date and strftime to format it to 'year/month/day'
    date_obj = pd.to_datetime(date_str, format='%d/%m/%Y')
    return date_obj.strftime('%Y-%m-%d')


#def convert_strange_char(name):
    

# Replace 'input.csv' with the path to your CSV file
input_file = r'C:\Users\jdrem\Documents\Project1\catalan-waters\data\data1.csv'
output_file = 'data1Prep.csv'

# Read the CSV file
df = pd.read_csv(input_file)

# Convert the 'date' column to the new format
df['Dia'] = df['Dia'].apply(convert_date_format)
#df['Estació'] = df['Estació'].apply()

# Save the modified DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print(f"Dates converted successfully. Output saved to {output_file}")
