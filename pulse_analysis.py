# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'cark_klent'))
    current_dir = os.getcwd()
    print(current_dir)
except:
    pass

#%%
import pandas as pd
import missingno as no

# (must install package too: conda install vega --channel conda-forge)
import altair.vegalite.v3 as alt

#%%
# of all the different alt.renderers.names() for our Altair graphs
# we use vegascope because it let's us load all our
# graphs into the same browser window
alt.renderers.enable('vegascope')

# read data in and look at it
df_raw = pd.read_csv('/Users/thomas/Documents/Python/gitRepos/cark_klent/201709-CAH_PulseOfTheNation_Raw.csv')
df = df_raw.copy()

# rename the columns
df.columns = [
    'income',
    'gender',
    'age',
    'age_range',
    'party',
    'trump_job_approval',
    'education',
    'edu_other',
    'race',
    'race_other',
    'relationship',
    'relationship_other',
    'q8x',
    'robots_job',
    'climate_change',
    'transformer_movies_seen',
    'q11x',
    'benevolent_scientists',
    'vaccines_safe',
    'books_read_yearly',
    'q14x',
    'believe_in_ghosts',
    'federal_govt_budget_spent_science',
    'q16x',
    'funding_for_science',
    'earth_farther_from_sun_in_winter',
    'smart_sad_or_happy_dumb',
    'pee_in_shower',
    ]

#  look at it
no.matrix(df)

#%%
df.head()
df.info()
df.describe()

# #%%
# # column dictionary
# column_key = dict(zip(df.columns, df_raw.columns))

# # function to recode some string values
# # can be used in a lambda function (see below)
# def recode_likely(*args):
#     arguments = list(arg for arg in args)
#     arg = arguments[0]
#     if (isinstance(arg, str)):
#         if ('unlikely' in arg.lower()):
#             arg = 0
#         elif ('likely' in arg.lower()):
#             arg = 1
#         else:
#             arg=''
#     return arg

# #%%
# df['robot_job_coded'] = df['robots_job'].apply(lambda x: recode_likely(x)).dropna()

# #%%
# # df.columns

#%%
# Altair includes a Chart.serve() method which will
# seamlessly convert a chart to HTML, start a webserver
# serving that HTML, and open your system’s default
# web browser to view it. But Chart.display() is better
chart = alt.Chart(df).mark_bar().encode(
    x='income:Q',
    y='robots_job:O',
    color='pee_in_shower:N',
    row=alt.Row('smart_sad_or_happy_dumb:N', sort=['Smart and Sad', 'Dumb and happy'])
).properties(height=150, width=600)
chart.display()

#%%
area = alt.Chart(df).mark_bar(opacity=1).encode(
    x="robots_job:O",
    y="trump_job_approval:N",
    color="income:Q"
)
area.display()

#%%
df.smart_sad_or_happy_dumb

#%%
