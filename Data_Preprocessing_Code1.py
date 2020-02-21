# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset=pd.read_csv('Data.csv')
X=dataset.iloc[:,:3].values
y=dataset.iloc[:,3].values

# Taking care of the misiing data
from sklearn.impute import SimpleImputer
missingvalues=SimpleImputer(missing_values=np.nan,strategy='mean',verbose=0)
missingvalues=missingvalues.fit(X[:,1:3])
X[:,1:3]=missingvalues.transform(X[:,1:3])


# Encoding the categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([('encoder',OneHotEncoder(),[0])],remainder='passthrough')
X=np.array(ct.fit_transform(X),dtype=np.float)

# Encoding Y data
from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(y)


# Splitting the dataset into train and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)

sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1,1))
















