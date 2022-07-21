from ast import keyword
from platform import node
import re
import os
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore
from rdflib import URIRef, RDF, Namespace, Literal, Graph
import pandas as pd
from sparql_dataframe import get




#my ontology classes URI 
#main class
literaryDiaryIRI=URIRef("http://www.semanticweb.org/victor/ontologies/2022/6/ontoMeditations/literary_diary")
#sub class
abstractFigureIRI=URIRef("https://w3id.org/arco/ontology/core/AbstractFigure")
agentRoleIRI=URIRef("https://w3id.org/arco/ontology/core/AgentRole")
chaptersIRI=URIRef("https://w3id.org/arco/ontology/core/chapters")
conceptIRI=URIRef("https://w3id.org/arco/ontology/core/Concept")
sentimentIRI=URIRef("https://w3id.org/arco/ontology/core/Sentiment")
#sub sub class of abstractfigure
menIRI=URIRef("https://w3id.org/arco/ontology/core/AbstractFigure/men")
godIRI=""
#sub sub class of chapters
fragmentIRI=URIRef("https://w3id.org/arco/ontology/core/fragments")
#sub sub class of sentiments
negativeIRI=URIRef("https://w3id.org/arco/ontology/core/negative_sentiment")
positiveIRI=URIRef("https://w3id.org/arco/ontology/core/positive_sentiment")

#my ontology URI for Object Properties
hasAssociatedAgent=URIRef("https://w3id.org/arco/ontology/core/hasAssociatedAgent")
hasAssociatedConcept=URIRef("https://w3id.org/arco/ontology/core/hasAssociatedConcept")
hasAssociatedFigure=URIRef("https://w3id.org/arco/ontology/core/hasAssociatedFigure")
hasAssociatedsentimentIRI=URIRef("https://w3id.org/arco/ontology/core/hasAssociatedSentiment")
hasCharacteristicIRI=URIRef("https://w3id.org/arco/ontology/core/hasCharacteristic")
hasConstituentIRI=URIRef("https://w3id.org/arco/ontology/core/hasConstituent")
hasPartIRI=URIRef("https://w3id.org/arco/ontology/core/hasPart")
# sub class of has part IRI
isPartOfIRI=URIRef("https://w3id.org/arco/ontology/core/isPartOf")
isCategoryOfIRI=URIRef("https://w3id.org/arco/ontology/core/isCategoryOf")
isCompoentOfIRI=URIRef("https://w3id.org/arco/ontology/core/isComponentOf")
oppositveOfIRI=URIRef("https://w3id.org/arco/ontology/core/oppositeOf")
sameasIRI=URIRef("https://w3id.org/arco/ontology/core/sameAs")



providenceIRI=URIRef("https://w3id.org/arco/ontology/core/Category/providence")
justiceIRI=URIRef("https://w3id.org/arco/ontology/core/Category/justice")


#Data properties
hasTitleIRI = URIRef("https://w3id.org/arco/ontology/core/hasTitle")
hasAttributedAuthorIRI=URIRef("https://w3id.org/arco/ontology/core/hasAttributedAuthor")
hasCitationIRI=URIRef("https://w3id.org/arco/ontology/core/hasCitation")
keywordURI=URIRef("https://w3id.org/arco/ontology/core/keyword")
synonymIRI=URIRef("https://w3id.org/arco/ontology/core/synonym")

#data types
schemaIRI = URIRef("http://www.w3.org/2000/01/rdf-schema#")
LiteralIRI=URIRef("http://www.w3.org/2000/01/rdf-schema#Literal")

baseIRI = "https://w3id.org/arco/ontology/core/"

# accept the natural txt to work on
#my global variables
literaryDiaryname = ""
allTxt = []
txtnumber = 0         #<-- STORES ALL THE TEXTS
fragmentlist = []   #<-- STORES ALL THE FRAGMENTS, MAYBE DICT IS MORE SUITABLE?
allFragments = {}
'''
Reading text methods

The file object provides you with three methods for reading text from a text file:

    read() - read all text from a file into a string. This method is useful if you have a small file and you want to manipulate the whole text of that file.
    readline() - read the text file line by line and return all the lines as strings.
    readlines() - read all the lines of the text file and return them as a list of strings.

'''
#THIS FUNCTION ACCEPTS THE TEXT AND STORES IT IN A LOCAL LIST VARIABLE CALLED allTxt
def uploadtxt(filepath):
    if allTxt == []:
        globals()['literaryDiaryname']= input("This text you are uploading belongs to which book? Please provide a name for it")
    with open(filepath,"r",encoding="UTF-8") as f:
        chapter = f.read()
        allTxt.append(chapter)
        f.close
    return

#THIS FUNCTION ACCEPTS THE EXTRACTED SENTIMENTS FOR EACH FRAGMENT
def uploadextractedSentiments(filepath):
    sentimentsDf = pd.read_csv(filepath)

#THIS FUNCTION ACCEPTS THE EXTRACTED INSTANCES OF OUR CONCEPTS IN THE FRAMENTS
def uploadextractedConceptInstances(filepath):
    #da fare
    conceptInstanceDf = pd.read_csv(filepath)
    print(conceptInstanceDf)
    
def fragmentdictcreator(fragment,fragmentlen):
    globals()['txtnumber'] +=1
    data = {"fragmentlist":fragment,"fragmentscount":fragmentlen}
    allFragments.update({txtnumber:data})
    return

# create the list of fragments for each book
def fragmentor(txt):
    #THIS FUNCTION CREATOS FRAGMENTS FROM THE TEXT USING REGEX SPLITER AND STORES THEM IN THE 
    for item in allTxt:
        fragment =re.split('\d+\.', item)  #this creates a list of fragments
        #CHECK IF THERE ARE ANY BLANK FRAGMENTS
        for item in fragment:
            if item == "":  
                fragment.remove(item)
        fragementlen = len(fragment)
        fragmentdictcreator(fragment,fragementlen)     
    return

# itterate over the list of fragments in books and create a URI for all
def KGraphcreator():
    #da fare
    chaptersDict = {}
    fragIRIdict = {}
    myGraph = Graph()
    #create triples for your author here
    authorIRI = URIRef("https://w3id.org/arco/ontology/core/MarcusAurelius")
    #other agent roles IRIs
    DemocritusIRI = URIRef("https://w3id.org/arco/ontology/core/Democritus")
    EpictetusIRI = URIRef("https://w3id.org/arco/ontology/core/Epictetus")
    EuripidesIRI = URIRef("https://w3id.org/arco/ontology/core/Euripides")
    HeraclitusIRI = URIRef("https://w3id.org/arco/ontology/core/Heraclitus")
    HomerIRI = URIRef("https://w3id.org/arco/ontology/core/Homer")

    #create your triples for literary diary here
    subj = URIRef(baseIRI + literaryDiaryname)
    myGraph.add((subj,RDF.type,literaryDiaryIRI))
    myGraph.add((subj,hasTitleIRI,Literal(literaryDiaryname)))
    myGraph.add((subj,hasAttributedAuthorIRI,authorIRI))
    #create your triples for books/chapters here
    bookId = 1
    for items in allTxt:
        chaptersubj = URIRef(baseIRI + "Book" + str(bookId))
        #create your triples for book class instance here
        #create triples for each fragment of individual chapter
        for key in allFragments:
            for key2 in allFragments[key]:
                fragLocalID = 1
                fragUniID = str(bookId) + "." + str(fragLocalID)    #for example 1.1
                if key2 == "fragmentlist":
                    for item in allFragments[key][key2]:
                        fragIRI = URIRef(baseIRI + str(fragUniID))   
                        #append the fragIRI to a dict
                        fragIRIdict.update({"chapter":bookId,"fraglocation":fragUniID,"fragIRI":fragIRI,"text":item})
                        myGraph.add((chaptersubj,hasPartIRI,fragIRI))
        #store all the IRIs in a dict with the booknumber as key
        chaptersDict.update({bookId:chaptersubj})
        #change the localID for the next book/chapter here
        bookId +=1
    #create your triples for fragments here
    '''
    for key in allFragments:
        chapterNum = key
        localID = 1 #this is the id for the frament, keeping this outside the loop so that it does not get reset when iterating over the fragments of one chapter
        for value in allFragments[key]:
            #print(value) <-- this contains one paragraph
            UniversalID = chapterNum + "." + localID #we create unique number for each fragment
            subj = baseIRI + "fragment" + UniversalID
            #create all the triples for this fragment below
            triple1 = 1  
            triple2 = 2
            triple3 = 3
            #change the localID for the next frament below
            localID +=1
    '''
    dbupdater(myGraph)
    return True

def dbupdater(graphvariable):
    store = SPARQLUpdateStore()
    # The URL of the SPARQL endpoint is the same URL of the Blazegraph
    # instance + '/sparql'
    # It opens the connection with the SPARQL endpoint instance
    endpointURI = "http://127.0.0.1:9999/blazegraph/sparql"  #this is a bit forcing and may not work with multiple dbs with different endpoints
    store.open((endpointURI,endpointURI))

    for triple in graphvariable.triples((None, None, None)):
        store.add(triple)       
    # close connection 
    store.close()
    return

#read CSV to get extracted data
#DRIVER CODE FOR UPLOADING CORE TEXT

uploadtxt("txt/MeditationsBook1.txt")
uploadtxt("txt/MeditationsBook2.txt")
uploadtxt("txt/MeditationsBook3.txt")

fragmentor(allTxt)

#DRIVER CODE FOR VIEWING THE DICT OF FRAMENTS >>
'''
for key in allFragments:
    print(key)
    for key2 in allFragments[key]:
        print(allFragments[key][key2])
'''        

#print(literaryDiaryname)
#DRIVER CODE FOR UPLOADING THE EXTRACTED CONCEPTS
'''
uploadextractedConceptInstances("extractedSentiments/book1_occ/concept_occ0.csv") #<-- instances of extracted concept(Justice) keywords
uploadextractedConceptInstances("extractedSentiments/book1_occ/concept_occ1.csv") #<-- instances of extracted concept(Reason) keywords
'''
#DRIVER CODE FOR CREATING THE KNOWLEDGE GRAPH FROM THE TEXT
KGraphcreator()