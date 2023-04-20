# Classification-of-Malicious-Code-by-ML-PY

## Intro
The goal of this project is to perform malware analysis on a given dataset from python scanned files to implement basic machine learning algorithms: Gaussian Naive Bayes, Random Forest Classifier, Decision Tree Classifier, and Linear SVC. We use two data sets, one is generated from exe/dll scanning files, and the other is a sample obtained from the Internet.

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
The scanner should take the output dataset csv from the exe file. By using the output csv we should be able to run ml for analysis. Use the following algorithm.

The following results are from the internet example dataset:
- Gaussian Naive Bayes model accuracy(in %): 32.24573030843742
- Random Forest model accuracy(in %): 98.44506755034412
- Decision Tree Classifier Accuracy: 71.32296711700229
- Linear SVC Classifier accuracy(in %): 96.06853296619245

## The next step:
Continue to study the PEFILE scanner. Make the dataset output complete and be able to identify and remove malicious files from exe programs.

## Credit To
GitHub - pratikpv/malware_detect2: Malware Classification using Machine learning

GitHub - aayuv17/Malware-Analysis: Malware Analysis using Machine Learning

GitHub - bindog/ToyMalwareClassification: Kaggle微软恶意代码分类

erocarrera/pefile: pefile is a Python module to read and work with PE (Portable Executable) files (github.com)

Machine learning for encrypted malicious traffic detection: Approaches, datasets and comparative study - ScienceDirect

## In the future
https://blog.csdn.net/weixin_46625757/article/details/124088469?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-8-124088469-blog-127131381.235^v29^pc_relevant_default_base3&spm=1001.2101.3001.4242.5&utm_relevant_index=10
