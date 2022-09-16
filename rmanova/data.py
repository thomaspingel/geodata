# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 11:43:15 2022

@author: Thomas Pingel
"""

import pandas as pd
import numpy as np

from statsmodels.stats.anova import AnovaRM

#%% Girdan 3, 1 factor that is repeated

a=[10,19,27,28,9,13,25,29,4,10,20,18,5,6,12,17]
b = np.tile([1,2,3,4],4)
c = np.repeat([1,2,3,4],4)

df = pd.DataFrame({'y':a,'x':b,'subject':c})

df.to_csv('girdan_3.csv',index=False)


#%% Girdan 5, page 44, Table 5.1.  Sex is a between-subjects variable
# and explanation is a within-subjects variable

a=[48,31,24,29,46,34,25,31,45,37,27,35,37,39,30,38,45,34,29,32,28,17,19,20,32,18,20,22,35,19,22,24,39,16,19,22,31,15,20,22]
b=np.repeat([1,2],20)
c=np.tile([1,2,3,4],10)
d=np.repeat(range(10),4)
         
df = pd.DataFrame({'y':a,'sex':b,'explanation':c,'subject':d})

df.to_csv('girdan_5.csv',index=False)


#%% Girden 6, 3F1R (FIX THIS)

a=[6,6.5,9,10,5,6,7.3,10,7,7.5,9,9.5,6,7,8,8.5,8,9,11,12,6,7,8,11,8,9.5,11,12,6,6.9,7,11,11,12.5,15,16.5,7,8.1,9.7,14.5,4,4,5,5.5,4,4.5,5.8,5,5,7,7,7,4,4.5,5.5,4,5,6,7,7,4,5,7,6,5,6,6,6.5,3,5,7,6,6,7,10,9,5,6,9.7,9]
b=[1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2]
c=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
d=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
e=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

df = pd.DataFrame({'observations':a,'sex':b,'location':c,'time':d,'subject':e})

df.to_csv('girdan_6.csv',index=False)


#%% Myers 14

a = [82,48,41,53,72,70,51,45,43,35,30,12,77,41,61,31,43,43,21,29,67,39,30,40,71,53,50,62,89,67,76,68,82,84,83,71,56,56,55,45,64,44,44,52,76,74,64,74,84,80,75,77,84,72,63,81,76,54,57,61,84,66,61,77,67,69,55,69,61,67,55,61]
b = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
c = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
d = [11,11,11,11,21,21,21,21,31,31,31,31,41,41,41,41,51,51,51,51,61,61,61,61,12,12,12,12,22,22,22,22,32,32,32,32,42,42,42,42,52,52,52,52,62,62,62,62,13,13,13,13,23,23,23,23,33,33,33,33,43,43,43,43,53,53,53,53,63,63,63,63]

df = pd.DataFrame({'dependent':a,'bs_factor':b,'ws_factor':c,'subjects':d})

df.to_csv('myers_14.csv',index=False)


#%% Trujillo

X=[7,1,1,1,1,22,1,1,2,1,13,1,1,3,1,14,1,1,4,1,25,1,1,1,2,10,1,1,2,2,17,1,1,3,2,24,1,1,4,2,50,1,1,1,3,36,1,1,2,3,49,1,1,3,3,23,1,1,4,3,16,1,1,1,4,38,1,1,2,4,34,1,1,3,4,24,1,1,4,4,33,1,1,1,5,25,1,1,2,5,24,1,1,3,5,25,1,1,4,5,10,1,1,1,6,7,1,1,2,6,23,1,1,3,6,26,1,1,4,6,13,1,1,1,7,33,1,1,2,7,27,1,1,3,7,24,1,1,4,7,22,1,1,1,8,20,1,1,2,8,21,1,1,3,8,11,1,1,4,8,4,1,1,1,9,0,1,1,2,9,12,1,1,3,9,0,1,1,4,9,17,1,1,1,10,16,1,1,2,10,20,1,1,3,10,10,1,1,4,10,0,1,2,1,11,6,1,2,2,11,22,1,2,3,11,26,1,2,4,11,0,1,2,1,12,16,1,2,2,12,12,1,2,3,12,15,1,2,4,12,0,1,2,1,13,8,1,2,2,13,0,1,2,3,13,0,1,2,4,13,15,1,2,1,14,14,1,2,2,14,22,1,2,3,14,8,1,2,4,14,27,1,2,1,15,18,1,2,2,15,24,1,2,3,15,37,1,2,4,15,0,1,2,1,16,0,1,2,2,16,0,1,2,3,16,0,1,2,4,16,4,1,2,1,17,27,1,2,2,17,21,1,2,3,17,3,1,2,4,17,26,1,2,1,18,9,1,2,2,18,9,1,2,3,18,12,1,2,4,18,0,1,2,1,19,0,1,2,2,19,14,1,2,3,19,1,1,2,4,19,0,1,2,1,20,0,1,2,2,20,12,1,2,3,20,0,1,2,4,20,0,2,1,1,21,0,2,1,2,21,0,2,1,3,21,0,2,1,4,21,69,2,1,1,22,56,2,1,2,22,14,2,1,3,22,36,2,1,4,22,5,2,1,1,23,0,2,1,2,23,0,2,1,3,23,5,2,1,4,23,4,2,1,1,24,24,2,1,2,24,0,2,1,3,24,0,2,1,4,24,35,2,1,1,25,8,2,1,2,25,0,2,1,3,25,0,2,1,4,25,7,2,1,1,26,0,2,1,2,26
,9,2,1,3,26,37,2,1,4,26,51,2,1,1,27,53,2,1,2,27,8,2,1,3,27,26,2,1,4,27,25,2,1,1,28,0,2,1,2,28,0,2,1,3,28,15,2,1,4,28,59,2,1,1,29,45,2,1,2,29,11,2,1,3,29,16,2,1,4,29,40,2,1,1,30,2,2,1,2,30,33,2,1,3,30,16,2,1,4,30,15,2,2,1,31,28,2,2,2,31,26,2,2,3,31,15,2,2,4,31,0,2,2,1,32,0,2,2,2,32,0,2,2,3,32,0,2,2,4,32,6,2,2,1,33,0,2,2,2,33,23,2,2,3,33,0,2,2,4,33,0,2,2,1,34,0,2,2,2,34,0,2,2,3,34,0,2,2,4,34,25,2,2,1,35,28,2,2,2,35,0,2,2,3,35,16,2,2,4,35,36,2,2,1,36,22,2,2,2,36,14,2,2,3,36,48,2,2,4,36,19,2,2,1,37,22,2,2,2,37,29,2,2,3,37,2,2,2,4,37,0,2,2,1,38,0,2,2,2,38,5,2,2,3,38,14,2,2,4,38,0,2,2,1,39,0,2,2,2,39,0,2,2,3,39,0,2,2,4,39,0,2,2,1,40,0,2,2,2,40,0,2,2,3,40,0,2,2,4,40]
X = np.reshape(X,(-1,5))

df = pd.DataFrame(data=X,columns=['observations','intervention','sex','time','subjects'])

df.to_csv('trujillo.csv',index=False)


#%%% Friedman Popcorn data from Matlab documentation

a = [5.5,4.5,3.5,5.5,4.5,4,6,4,3,6.5,5,4,7,5.5,5,7,5,4.5]
b = np.tile([1,2,3],6) # Gourmet, National, Generic
c = np.repeat([1,2],9)

df = pd.DataFrame({'yield':a,'brand':b,'popper':c})

df.to_csv('friedman.csv',index=False)

