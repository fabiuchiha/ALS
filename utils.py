import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time, csv, pickle, os, itertools, random
from pathlib import Path
from random import choice
from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity
import csv
from itertools import combinations
import statistics

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def dataToJSON(data, filename):
    with open(filename, 'wb') as object_file:
        pickle.dump(data, object_file)

def JSONtoData(fileName):
    with open(fileName, 'rb') as object_file:
        data = pickle.load(object_file)
        return data

