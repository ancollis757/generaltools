import pandas as pd
import random

FILEPATH = r'C:\Users\nicko\Desktop\Stoic-Quotes-20230302.ods'
quotes = pd.read_excel(FILEPATH, engine="odf")
num_quotes = len(quotes)
# select a random index
random_index = random.randint(0,num_quotes-1)
quote_of_the_day = quotes['QUOTE'].iloc[random_index]
quote_of_the_day_author = quotes['AUTHOR'].iloc[random_index]

print(f"The quote of the day:\n\n{quote_of_the_day}\n{quote_of_the_day_author}")

