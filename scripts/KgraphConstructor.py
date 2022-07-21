from ast import keyword
import re
import os
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore
from rdflib import URIRef, RDF, Namespace, Literal, Graph
import pandas as pd
from sparql_dataframe import get




#my ontology classes URI 
#main class
literaryDiaryIRI="http://www.semanticweb.org/victor/ontologies/2022/6/ontoMeditations/literary_diary"
#sub class
abstractFigureIRI="https://w3id.org/arco/ontology/core/AbstractFigure"
agentRoleIRI="https://w3id.org/arco/ontology/core/AgentRole"
chaptersIRI="https://w3id.org/arco/ontology/core/chapters"
conceptIRI="https://w3id.org/arco/ontology/core/Concept"
sentimentIRI="https://w3id.org/arco/ontology/core/Sentiment"
#sub sub class of abstractfigure
menIRI="https://w3id.org/arco/ontology/core/AbstractFigure/men"
godIRI=""
#sub sub class of chapters
fragmentIRI="https://w3id.org/arco/ontology/core/fragments"
#sub sub class of sentiments
negativeIRI="https://w3id.org/arco/ontology/core/negative_sentiment"
positiveIRI="https://w3id.org/arco/ontology/core/positive_sentiment"

#my ontology URI for Object Properties
hasAssociatedAgent="https://w3id.org/arco/ontology/core/hasAssociatedAgent"
hasAssociatedConcept="https://w3id.org/arco/ontology/core/hasAssociatedConcept"
hasAssociatedFigure="https://w3id.org/arco/ontology/core/hasAssociatedFigure"
hasAssociatedsentimentIRI="https://w3id.org/arco/ontology/core/hasAssociatedSentiment"
hasCharacteristicIRI="https://w3id.org/arco/ontology/core/hasCharacteristic"
hasConstituentIRI="https://w3id.org/arco/ontology/core/hasConstituent"
hasPartIRI="https://w3id.org/arco/ontology/core/hasPart"
# sub class of has part IRI
isPartOfIRI="https://w3id.org/arco/ontology/core/isPartOf"
isCategoryOfIRI="https://w3id.org/arco/ontology/core/isCategoryOf"
isCompoentOfIRI="https://w3id.org/arco/ontology/core/isComponentOf"
oppositveOfIRI="https://w3id.org/arco/ontology/core/oppositeOf"
sameasIRI="https://w3id.org/arco/ontology/core/sameAs"



providenceIRI="https://w3id.org/arco/ontology/core/Category/providence"
justiceIRI="https://w3id.org/arco/ontology/core/Category/justice"


#Data properties
hasAttributedAuthorIRI="https://w3id.org/arco/ontology/core/hasAttributedAuthor"
hasCitationIRI="https://w3id.org/arco/ontology/core/hasCitation"
keywordURI="https://w3id.org/arco/ontology/core/keyword"
synonymIRI="https://w3id.org/arco/ontology/core/synonym"

#dat types
schemaIRI = "http://www.w3.org/2000/01/rdf-schema#"
LiteralIRI="http://www.w3.org/2000/01/rdf-schema#Literal"



# accept the natural txt to work on
allTxt = []
'''
Reading text methods

The file object provides you with three methods for reading text from a text file:

    read() - read all text from a file into a string. This method is useful if you have a small file and you want to manipulate the whole text of that file.
    readline() - read the text file line by line and return all the lines as strings.
    readlines() - read all the lines of the text file and return them as a list of strings.

'''

def uploadtxt(filepath):
    with open(filepath) as f:
        chapter = f.read()
        allTxt.append(chapter)
        f.close
    fragmentor(chapter)
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
    fragment =re.split('\d+\.', txt)
    print(fragment)
    print(os.linesep)
    return

# itterate over the list of fragments in books and create a URI for all
def KGraphcreator():
    #da fare
    endpointURI = "http://127.0.0.1:9999/blazegraph/sparql"

    #read CSV to get extracted data

uploadtxt("txt/MeditationsBook1.txt")
