# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 15:31:07 2022

@author: gmati
"""

import rdflib
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import matplotlib.pyplot as plt
import re
from random import sample
import graphdb
import pandas as pd

from SPARQLWrapper import SPARQLWrapper, JSON

from rdflib import Graph
graph = Graph()

#graph.parse('tache1/slodbi.ttl', format='ttl')
graph.parse('tache2/tbl2.ttl', format='ttl')

print(graph.serialize(format='ttl'))
