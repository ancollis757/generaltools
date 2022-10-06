import pandas as pd
from datetime import datetime


OUTPUT_LOCATION = 'C:\\Users\\nicko\\Desktop\\Reports\\DogReport_'
DOG_DICT = [
    {'owner': 'Lianne', 'plural': 0,
     'dog_s_punc': "Bailey's", "dog_s": 'Bailey',
     'photo_comment': "a very relaxed and friendly dog, he seems very chilled with that little boy and the lamb!"},

    {'owner': 'Muriel', 'plural': 0,
     'dog_s_punc': "Bertie's", "dog_s": 'Bertie',
     'photo_comment': "a nice young dog, looking out the window at what's going on!"},

    {'owner': 'Louise', 'plural': 0,
     'dog_s_punc': "Wilf's", "dog_s": 'Wilf',
     'photo_comment': "a very relaxed and friendly cockapoo, he seems very chilled sat in the car."},

    {'owner': 'Ron', 'plural': 0,
     'dog_s_punc': "Sydney's", "dog_s": 'Sydney',
     'photo_comment': "a very relaxed and friendly dog, looks very chilled there."},

    {'owner': 'Daniel', 'plural': 0,
     'dog_s_punc': "Ralph's", "dog_s": 'Ralph',
     'photo_comment': "a very relaxed and friendly dog, looks quite excited in the snow."},

    {'owner': 'Lucy', 'plural': 0,
     'dog_s_punc': "Rex's", "dog_s": 'Rex',
     'photo_comment': "a very relaxed and friendly dog, he seems very excited about his purple ball."}
]

output_text = []  # empty list to append to.

for dog in range(len(DOG_DICT)):

    text = f"Dear {DOG_DICT[dog]['owner']}, I saw {DOG_DICT[dog]['dog_s_punc']} profile, {DOG_DICT[dog]['photo_comment']}\n\nI" \
           f"'m local to Rushden and looking for a dog for my daughter " \
           f"(7) and I to walk.\n\nI have a car so I can pick up from the area around Rushden.\n\nHappy to spend {DOG_DICT[dog]['dog_s_punc']} " \
           f" time with us as you would suggest; happy to do exercise, grooming etc. If my daughter and I looking after " \
           f"{DOG_DICT[dog]['dog_s']} sometimes is possible, please let me know. happy to discuss dates and times that " \
           f"would work best. " \
           f"Best wishes,\n\nAlex "
    output_text.append(text)

#DOESN'T COME OUT IN THE DESIRED ORDER.


output_df = pd.DataFrame(output_text)
today = datetime.today().strftime('%Y-%m-%d')
filepath_out = OUTPUT_LOCATION + today + '.xlsx'
print(f"Here is your file's location: {filepath_out}")
output_df.to_excel(filepath_out)