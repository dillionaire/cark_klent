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
df = pd.read_csv('201709-CAH_PulseOfTheNation_Raw.csv')


#%%
no.matrix(df)


#%%



