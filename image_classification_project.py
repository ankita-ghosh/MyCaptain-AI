#importing dependencies 


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

%matplotlib inline

#using pandas to read the database stored in the same folder

data = pd.read_csv("/Users/ankitaghosh/mnist_train.csv")

#viewing the column heads

data.head()

#extracting data from the dataset and viewing them up close

a = data.iloc[2,1:].values

#reshaping the extracted data into a reasonable size

a=a.reshape(28,28).astype('uint8')
plt.imshow(a)

#Note: an array of size 784 can only be reshaped into sizes that form 784. Example: 28*28, 16*49, etc. 

#preparing the data
#separating labels and data values

df_x = data.iloc[:,1:]
df_y = data.iloc[:,0]


# In[34]:


#creating test and train sizes /batches

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)


#check data

y_train.head()

#call rf classifier

rf = RandomForestClassifier(n_estimators=100)

#fit the model

rf.fit(x_train,y_train)

#prediction on test data

pred = rf.predict(x_test)

pred

#check prediction accuracy

s=y_test.values

#calculate number of correctly predicted values 

count=0
for i in range(len(pred)):
    if pred[i]==s[i]:
        count+=1
print(count)

#total values that the prediction was run on

len(pred)

#accuracy

11621/12000
