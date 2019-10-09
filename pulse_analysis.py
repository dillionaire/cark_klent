# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'cark_klent'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd
import missingno as no

#%%
df = pd.read_csv('/Users/thomas/Documents/Python/gitRepos/cark_klent/201709-CAH_PulseOfTheNation_Raw.csv')


#%%
no.matrix(df)


#%%
df.shape


#%%
df.head()


#%%
df.info()

#%%
len(df.columns)

#%%
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



#%%
df.shape

#%%
df.describe()


#%%
df.info()#%%

#%%
