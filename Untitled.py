
# coding: utf-8

#     # Importing numpy and sklearn

# In[765]:

import numpy as np


# In[766]:

from sklearn import datasets
from scipy.spatial import distance

def eucledean(a,b):
        return distance.euclidean(a,b)


#     # Load iris data

# In[767]:

iris = datasets.load_iris()


# In[768]:

iris_X = iris.data


# In[769]:

iris_y = iris.target


# In[770]:

np.unique(iris_y)


# In[771]:

np.random.seed(0)


# In[772]:

indices = np.random.permutation(len(iris_X))


# In[773]:

iris_X_train = iris_X[indices[:105]]
iris_y_train = iris_y[indices[:105]]
iris_X_test  = iris_X[indices[105:]]
iris_y_test  = iris_y[indices[105:]]

print(len(iris_X_test))
print(len(iris_y_test))
#iris_X_train, iris_X_test, iris_y_train, iris_y_test = train_test_split(iris_X,iris_y,test_size = 0.3)


# In[774]:

class myCustomClassifier():
    
    
    def fit(self,iris_X_train,iris_y_train):
        self.iris_X_train = iris_X_train
        self.iris_y_train = iris_y_train
        
    def closest(self,row):
        closest_distance = eucledean(row,self.iris_X_train[0])
        closest_index = 0
        for i in range(1,len(iris_X_train)):
            dist = eucledean(row,self.iris_X_train[i])
            if dist < closest_distance:
                closest_distance = dist
                closest_index = i
                
        return self.iris_y_train[closest_index]
        
    def predict(self,iris_X_test):
        predictions = []
        for row in iris_X_test:
            
            label = self.closest(row)
            predictions.append(label)
        return predictions
        


# In[775]:

from sklearn.neighbors import KNeighborsClassifier
knn = myCustomClassifier()
knn.fit(iris_X_train, iris_y_train) 


# In[776]:

#len(iris_y_test)
len(iris_X_test)


# In[777]:

Final_predictions = knn.predict(iris_X_test)
print(len(Final_predictions))
print(Final_predictions)


# In[778]:

from sklearn.metrics import accuracy_score
print(accuracy_score(iris_y_test,Final_predictions))


# In[ ]:




# In[ ]:




# In[ ]:



