import re
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore
from rdflib import URIRef, RDF, Namespace, Literal, Graph
import pandas as pd
from sparql_dataframe import get

#my ontology classes URI

Bookname = "https:\\bookname"
Chapter = "https:\\chaptername"
Fragment = "https:\\fragment"

ConceptInstance = "https:\\JustinceInstance1"
Concept = "https:\\conceptname"


allTxt = []
fragmentlist =[]

# accept the natural txt to work on
'''
Reading text methods

The file object provides you with three methods for reading text from a text file:

    read() - read all text from a file into a string. This method is useful if you have a small file and you want to manipulate the whole text of that file.
    readline() - read the text file line by line and return all the lines as strings.
    readlines() - read all the lines of the text file and return them as a list of strings.

'''

def uploadtxt(filepath):
    # da fare
    with open(filepath) as f:
        chapter = f.read()
        allTxt.append(chapter)
        f.close
    return

def uploadextractedSentiments(filepath):
    sentiDf = pd.read_csv(filepath)

def uploadextractedConceptInstances(filepath):
    conceptInstanceDf = pd.read_csv(filepath)
    
def fragmentlistcreator():
    for item in allTxt:
        fragmentlist.append(item)

# create the list of fragments for each book
def fragmentor(txt):
    # da fare
    # logic from chloe's code
    pass

# itterate over the list of fragments in books and create a URI for all
def KGraphcreator():
    #da fare
    endpointURI = "http://127.0.0.1:9999/blazegraph/sparql"

    #read CSV to get extracted data

