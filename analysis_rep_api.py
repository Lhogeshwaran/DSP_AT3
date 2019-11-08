# This python file provides an API to repeat the exercise/anaysis with new datasets 
# that the user may have recreated similar to the data in the github repo
# The API return visualization of analysis and csv file with sentiment scores

import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype
import matplotlib.pyplot as plt
import seaborn as sns
import re, sys, os
from scipy import stats
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_excel(sys.argv[1], sheet_name=sys.argv[2])

expected_cols = ['Person', 'Day', 'Date ', 'Sleep (hours)', 'Sleep (minutes)'
                 , 'Minutes of sleep', 'Sleep Quality (1 Very Bad - 5 Very Good)'
                 , 'How many times did you wake up during the night'
                 , 'Wakeup Time (HH:MM)', 'Bedtime (HH:MM)(night before)'
                 , 'Did you nap during the day (yes/ no)', 'Steps', 'KM'
                 , 'Any physical activity not recorded by health app (yes/no) (such as swiming)'
                 , 'Description of mood/experience during day. No word limit. Free text .'
                 , 'Personal Expenses']

provided_cols = list(df)

if provided_cols != expected_cols:
    raise ValueError('Expected data file column headers do not match with the provided data file column headers.\n'
    'Check if the all the columns are present in the uploaded dataset and in order :\n'
    f'{expected_cols}')

cats_day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
df['Day'] = df['Day'].astype(CategoricalDtype(categories=cats_day, ordered=True))

df['Date '] = pd.to_datetime(df['Date ']).apply(lambda x: x.date())


df['Sleep Quality (1 Very Bad - 5 Very Good)'] = df['Sleep Quality (1 Very Bad - 5 Very Good)'].fillna(0)
df['Sleep Quality (1 Very Bad - 5 Very Good)'] = df['Sleep Quality (1 Very Bad - 5 Very Good)'].astype(int)

df['Description of mood/experience during day. No word limit. Free text .'] = df['Description of mood/experience during day. No word limit. Free text .'].fillna(' ')

from my_utils.viz_utils import plot_1
plt1 = plot_1('Person', 'Minutes of sleep', 'box', 'Day', df)
plt1.savefig('By_day_of_week.png')

plt2 = plot_1('Person', 'Minutes of sleep', 'box', 'Person', df)
plt2.savefig('By_participant.png')

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score

df['VADER_SCORE'] = df['Description of mood/experience during day. No word limit. Free text .'].apply(sentiment_analyzer_scores)

df_dict_to_series = df['VADER_SCORE'].apply(pd.Series)
df = df.join(df_dict_to_series)
del df_dict_to_series
df = df.drop(columns='VADER_SCORE')

def sent_band(val):
    if val >= 0.05:
        band = 'Positive'
    elif val <= -0.05:
        band = 'Negative'
    else:
        band = 'Neutral' 
    return band

df['sentiment_band'] = df['compound'].apply(lambda x: sent_band(x))

df.to_csv('processed_data.csv')
PWD = os.getcwd()
print(f'Processed data file with sentiment scores and results of analysis have been saved at {PWD}.')