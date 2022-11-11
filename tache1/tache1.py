# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:27:40 2022

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
graph.parse('tache1/dipcas_prov.ttl', format='ttl')

#print(graph.serialize(format='ttl'))


"""

G = rdflib_to_networkx_multidigraph(graph)

# Plot Networkx instance of RDF Graph
pos = nx.spring_layout(G, scale=2)
edge_labels = nx.get_edge_attributes(G, 'r')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw(G, with_labels=True)

#if not in interactive mode for 
plt.show()

"""


#http://LAPTOP-CS19OKIS:7200/repositories/tach1


sparql = SPARQLWrapper(
    "http://LAPTOP-CS19OKIS:7200/repositories/tach1"
)
sparql.setReturnFormat(JSON)
#http://localhost:7200/sparql?name=&infer=true&sameAs=true&query=select%20*%20where%20%7B%20%0A%09%3Fs%20%3Fp%20%3Fo%20.%0A%7D%20limit%20100%20%0A
# gets the first 3 geological ages
# from a Geological Timescale database,
# via a SPARQL endpoint
queryString = "SELECT * WHERE { ?s ?p ?o. } LIMIT 4"

queryString1=" PREFIX slodbi: <http://krono.act.uji.es/schemas/slodbi#> select ?s ?numap where { ?s slodbi:num-apartamentos-estandar  ?numap .} limit 20 "

queryString2="""PREFIX slodbi: <http://krono.act.uji.es/schemas/slodbi#>
PREFIX esadm: <http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio#>
select ?s ?hotel where { 
    ?s esadm:autonomia slodbi:Comunidad_Valenciana.
    ?s slodbi:tiene-hoteles  ?hotel .
} LIMIT 5
"""

queryString3="""
PREFIX slodbi: <http://krono.act.uji.es/schemas/slodbi#> 
PREFIX geosparql: <http://www.opengis.net/ont/geosparql#>
SELECT ?quoi WHERE{
    slodbi:hotel-f8ee71c19e02085c5b57ed5843356be44ca7c26f slodbi:ubicacion ?p.
    ?p geosparql:asWKT ?quoi
    }

"""

queryString4="""
SELECT ?o ?p ?s WHERE{
    ?o ?p ?s
    }

"""



#slodbi:ubicacion [ a sf:Point ; geosparql:asWKT "POINT(40.051330000000064 0.040119966000020005)"^^geosparql:wktLiteral ] ;    

sparql.setQuery(queryString4)

test=[]
dataf={}
try:
    ret = sparql.queryAndConvert()
    dataf['o']=[]
    dataf['p']=[]
    dataf['s']=[]
    for r in ret["results"]["bindings"]:
        #print(r)
        #print(r["o"]["value"])
        dataf['o'].append(r["o"]["value"])
        dataf['p'].append(r["p"]["value"])
        dataf['s'].append(r["s"]["value"])
        if r["o"]["value"] not in test:
            test.append(r["o"]["value"])
        if r["s"]["value"] not in test:    
            test.append(r["s"]["value"])
    
        
except Exception as e:
    print(e)


df=pd.DataFrame(dataf)
"""
r = re.compile(".*wikidata.*")
#.*[Cc]astell[óo].*
newlist = list(filter(r.match, test))
for t in newlist:
    print(t)
    
print("\n")
"""

for t in sample(test,10):
    print(t)
    print(re.sub(r'.*\/(.)',r'\1',t))
    print("\n")


print(df.head())
