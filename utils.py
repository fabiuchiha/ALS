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
from datetime import datetime as dt
from cdlib import algorithms, readwrite, evaluation, NodeClustering

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def dataToBinary(data, filename):
    with open(filename, 'wb') as object_file:
        pickle.dump(data, object_file)

def binaryToData(fileName):
    with open(fileName, 'rb') as object_file:
        data = pickle.load(object_file)
        return data
    
def averageDegree(network):
    degrees = [val for (node, val) in network.degree()]
    sum = 0
    for d in degrees:
        sum += d
    return sum/len(degrees)

def kin(network):
    nodes = network.nodes()
    sum = 0
    for n in nodes:
        sum += network.in_degree(n)
    return sum/len(nodes)

def kout(network):
    nodes = network.nodes()
    sum = 0
    for n in nodes:
        sum += network.out_degree(n)
    return sum/len(nodes)

def APL(network):
    if (nx.is_directed(network)):
        largestComponent = 0
        largestAPL = 0
        for C in (network.subgraph(c) for c in nx.weakly_connected_components(network)):
            if largestComponent<len(C.nodes):
                largestComponent = len(C.nodes)
                apl = nx.average_shortest_path_length(C)
                largestAPL = apl
        return largestAPL
    else:
        for C in (network.subgraph(c) for c in nx.connected_components(network)):
            return nx.average_shortest_path_length(C)

def networkInfo(network):
    print("Average degree:", averageDegree(network))
    if (nx.is_directed(network)):
        print("Internal average degree:", kin(network))
        print("External average degree:", kout(network))
    print("Clustering coefficient:", nx.average_clustering(network))
    print("Average Path Length (highest value):", APL(network))