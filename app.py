# library used to access directories and the .env file (NOT SHOWN for security reasons)
import os

# libraries to visualize and organize data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# libraries to treat categorical variables within the dataframe
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
# libraries to train the model

# libraries to load environment variables
from dotenv import load_dotenv

"""Process data from the data set"""
load_dotenv()
BASE_DIR = os.getenv("BASE_DIR")
diabetes_csv = pd.read_csv(os.path.join(BASE_DIR,"diabetes_prediction_india.csv"))

"""TODO: Clean Up Data """
diabetes_csv = diabetes_csv.drop_duplicates().dropna()

"""TODO: Treat Categorical Variables """

print(diabetes_csv.dtypes)

veg_le = LabelEncoder()

#diabetes_csv['Encoded Diet Type'] = veg_le.fit_transform(['Diet Type'])
#print(diabetes_csv)

diabetes_dict = diabetes_csv.to_dict()
print(diabetes_dict)
"""TODO: Train and Test the Model """