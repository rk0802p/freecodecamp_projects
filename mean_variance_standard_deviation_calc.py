import numpy as np
from numpy import random


def calculate(listt):
  list1 = np.reshape(listt,(3,3))

  mean1 = np.mean(list1, axis=0) 
  mean2=np.mean(list1,axis=0) 
  mean3=np.mean(list1)

  variance1 = np.mean((list1- np.mean(list1))**2, axis = 0)
  variance2 = np.mean((list1- np.mean(list1))**2, axis = 1)
  variance3 = np.mean((list1- np.mean(list1))**2)

  standard_deviation1 = np.std(list1,axis =0)
  standard_deviation2 =np.std(list1,axis =1)
  standard_deviation3 = np.std(list1)

  min1 = np.min(list1,axis = 0)
  min2 = np.min(list1,axis = 1)
  min3 = np.min(list1)

  max1 = np.max(list1 ,axis = 0)
  max2 =np.max(list1,axis =1)
  max3 = np.max(list1)

  sum1 = np.sum(list1,axis = 0)
  sum2 = np.sum(list1 ,axis = 1)
  sum3 = np.sum(list1)

  calculations = {
    'mean':[mean1 ,mean2 ,mean3],
    'varience' :[ variance1,variance2,variance3],
    'standard_deviation' : [standard_deviation1,standard_deviation2,standard_deviation3],
    'min':[min1,min2,min3],
    'max':[max1,max2,max3],
    'sum':[sum1,sum2,sum3]
  }

  return calculations

l = np.array([1,11,21,31,41,51,61,71,81])
print(calculate(l))