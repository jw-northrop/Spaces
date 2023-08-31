
#main SPACES code

#declare libraries
import nltk as nl
import numpy as np
import pandas as pd
import fuzzywuzzy as fuzz
import PyDictionary as pDict
import flask as fk #may split this into a diff sub



## IMPORT REVIT DATA

"""
user will need to point us to this
webapp this can just be uploaded sheet/csv
this is filler for now - clean
organize data...dictionary
"""

revitdata = pd.read_excel(io=r"C:\Users\jwiest\Desktop\SPACES_00.xlsx", sheet_name='Revit DATA')
#print(revitdata_df)

##IMPORT DESIGNATIONS

#will point to DB
"""
split list appropriately
organize data in standard way...search strings: designation
"""

designations = pd.read_excel(io=r"C:\Users\jwiest\Desktop\SPACES_00.xlsx", sheet_name='Designation DB')
print(designations)


##CLEAN REVIT NAMES

from nltk.corpus import stopwords
nl.download('stopwords') #default stopwords list, can append, can also avoid downloading this all the time - just store text file
stop_words = set(stopwords.words("english")) #start with def


#remove numbers - uses regular expression
revitdata['ROOM NAMES: REVIT'] = revitdata['ROOM NAMES: REVIT'].replace('\d+', '', regex=True)
#remove 'L.' - leftover from a level indicator
#Job Specific
revitdata['ROOM NAMES: REVIT'] = revitdata['ROOM NAMES: REVIT'].str.replace('L.', '')
#remove stopwords?? - this seems to have removed spaces. probably want custom list
#revitdata['ROOM NAMES: REVIT'] = revitdata['ROOM NAMES: REVIT'].apply(lambda x: ''.join([word for word in x.split() if word not in (stop_words)]))

#boolean to exclude for obvious excludes
revitdata.loc['ROOM NAMES: REVIT'] 


print(revitdata)
