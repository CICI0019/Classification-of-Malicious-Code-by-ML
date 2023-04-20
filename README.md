# Classification-of-Malicious-Code-by-ML-PY

## Intro


## About PEFILE
Refers to a file in a certain format, executable files exe dynamic link library (dll) driver files (sys) are all PE file formats。
Pefile can parse, read or modify PE files.
- The structure of a PE file when it is stored on disk is different from the structure after it is loaded into memory.
- When the PE file is loaded into the memory through the Windows loader, the version in the memory is called a module (Module).
- The starting address of the mapping file is called the module handle (hModule), also known as the base address (ImageBase).

## Install
````python
pip install pefile
```````````````````````
## Import
````python
import pefile
import os, string, shutil, re
import sys
import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics 
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_predict
`````````````````````````````````````````````````````````

## Usage
```````python
python scan_file <insert exe file>
Read <Input>.csv Manually input the csv file from the scanFile
```````````````````````````````````
## What to expect?
- Gaussian Naive Bayes model accuracy(in %): 32.24573030843742
- Random Forest model accuracy(in %): 98.44506755034412
- Decision Tree Classifier Accuracy: 71.32296711700229
- Linear SVC Classifier accuracy(in %): 96.06853296619245

## The next step:


## Credit To
