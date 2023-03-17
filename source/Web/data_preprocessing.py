# Read data
import pandas as pd
import numpy as np
import os
data_loc = pd.read_csv('../../data/water_potability.csv')
# Process missing value
# PH
data_loc['ph'] = data_loc['ph'].apply(lambda x: x if x > 0 else 0)
data_loc['ph'] = data_loc['ph'].apply(lambda x: x if x > 0 else data_loc['ph'].mean())
# Hardness
data_loc['Hardness'] = data_loc['Hardness'].apply(lambda x: x if x > 0 else 0)
data_loc['Hardness'] = data_loc['Hardness'].apply(lambda x: x if x > 0 else data_loc['Hardness'].mean())
# Solids
data_loc['Solids'] = data_loc['Solids'].apply(lambda x: x if x > 0 else 0)                                                
data_loc['Solids'] = data_loc['Solids'].apply(lambda x: x if x > 0 else data_loc['Solids'].mean())
# Chloramines
data_loc['Chloramines'] = data_loc['Chloramines'].apply(lambda x: x if x > 0 else 0)
data_loc['Chloramines'] = data_loc['Chloramines'].apply(lambda x: x if x > 0 else data_loc['Chloramines'].mean())
# Sulfate
data_loc['Sulfate'] = data_loc['Sulfate'].apply(lambda x: x if x > 0 else 0)
data_loc['Sulfate'] = data_loc['Sulfate'].apply(lambda x: x if x > 0 else data_loc['Sulfate'].mean())
# Conductivity
data_loc['Conductivity'] = data_loc['Conductivity'].apply(lambda x: x if x > 0 else 0)
data_loc['Conductivity'] = data_loc['Conductivity'].apply(lambda x: x if x > 0 else data_loc['Conductivity'].mean())
# Organic_carbon
data_loc['Organic_carbon'] = data_loc['Organic_carbon'].apply(lambda x: x if x > 0 else 0)
data_loc['Organic_carbon'] = data_loc['Organic_carbon'].apply(lambda x: x if x > 0 else data_loc['Organic_carbon'].mean())
# Trihalomethanes
data_loc['Trihalomethanes'] = data_loc['Trihalomethanes'].apply(lambda x: x if x > 0 else 0)
data_loc['Trihalomethanes'] = data_loc['Trihalomethanes'].apply(lambda x: x if x > 0 else data_loc['Trihalomethanes'].mean())
# Turbidity
data_loc['Turbidity'] = data_loc['Turbidity'].apply(lambda x: x if x > 0 else 0)
data_loc['Turbidity'] = data_loc['Turbidity'].apply(lambda x: x if x > 0 else data_loc['Turbidity'].mean())
