# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:47:21 2019

@author: Lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'to ignore the quoting in file! quoting paramter = 3'  

dataset = pd.read_csv('Restaurant_Reviews.tsv' , delimiter = '\t' , quoting = 3)

import re
import nltk
import nltk.stem.porter import PorterStemmer
 
nltk.download('stopwords')
from nltk.corpus import stopwords
review = re.sub('[^a-zA-Z]' , ' ' , dataset['Review'][0])
review = review.lower()

review = review.split()
review = [word for word in review if not word in set(stopwords.words('english'))]
#using set to increasing the rate of algorithm


#learn about aspect mining
#chatbot #speech recogniztion

