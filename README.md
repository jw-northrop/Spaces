# Spaces

This is essentially a text mataching algorithm to compare a list of names (Architectural Room names exported from Revit) vs a database of categorizations for different disciplines (IE acoustic vs mech vs elect...)

Python backend will handle the language processing (comparison) 

Intent is to use flask as framework with python and combine with a react frontend to allow this to be deployed and used as a webapp

Will include % match when not 100% (ie when fuzzy string is used) and will look to have user correct errors that are fed back into the database
