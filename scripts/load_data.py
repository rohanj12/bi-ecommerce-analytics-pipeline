#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sqlalchemy import create_engine

# 1. Load CSV file into pandas DataFrame
df = pd.read_csv('../data/OnlineRetail.csv', encoding='ISO-8859-1')

# 2. Clean column names: remove spaces, make lowercase
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# 3. Set up connection to PostgreSQL
# Replace the username, password, and database name as needed
engine = create_engine('postgresql://postgres:Rohanj12!!@localhost:5432/ecomdb')

# 4. Load DataFrame into PostgreSQL
df.to_sql('raw_retail_data', engine, index=False, if_exists='replace')

# 5. Done!
print("✅ Data successfully loaded into PostgreSQL.")

