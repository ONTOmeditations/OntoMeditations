from ast import keyword
from operator import contains
from platform import node
import re
import os
from numpy import empty
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
neutralIRI=URIRef("https://w3id.org/arco/ontology/core/neutral_sentiment")

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
reasonIRI=URIRef("https://w3id.org/arco/ontology/core/Category/reason")
powerIRI=URIRef("https://w3id.org/arco/ontology/core/Category/power")
deathIRI=URIRef("https://w3id.org/arco/ontology/core/Category/death")
natureIRI=URIRef("https://w3id.org/arco/ontology/core/Category/nature")
psychebodyIRI=URIRef("https://w3id.org/arco/ontology/core/Category/psyche&body")


#Data properties
containsTextIRI = URIRef("https://www.semanticweb.org/victor/ontologies/2022/6/untitled-ontology-5#containsText")
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
FragmentsIRIdata = {}
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
    return sentimentsDf
book1sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book1.csv")
book2sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book2.csv")
book3sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book3.csv")
book4sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book4.csv")
book5sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book5.csv")
book6sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book6.csv")
book7sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book7.csv")
book8sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book8.csv")
book9sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book9.csv")
book10sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book10.csv")
book11sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book11.csv")
book12sentimentsDF = uploadextractedSentiments("Sentimentscsv/SA_df_book12.csv")

allSentimentsDict = {"1":book1sentimentsDF,"2":book2sentimentsDF,"3":book3sentimentsDF,"4":book4sentimentsDF,"5":book5sentimentsDF,"6":book6sentimentsDF,"7":book7sentimentsDF,"8":book8sentimentsDF,"9":book9sentimentsDF,"10":book10sentimentsDF,"11":book11sentimentsDF,"12":book12sentimentsDF}

#THIS FUNCTION ACCEPTS THE EXTRACTED INSTANCES OF OUR CONCEPTS IN THE FRAMENTS
def uploadextractedConceptInstances(filepath):
    conceptInstanceDf = pd.read_csv(filepath)
    return conceptInstanceDf

book1justiceDF = uploadextractedConceptInstances("extractedSentiments/book1_occ/concept_occ0.csv")
book1reasonDF = uploadextractedConceptInstances("extractedSentiments/book1_occ/concept_occ1.csv")
book1powerDF = uploadextractedConceptInstances("extractedSentiments/book1_occ/concept_occ2.csv")
book1providenceDF = uploadextractedConceptInstances("extractedSentiments/book1_occ/concept_occ3.csv")
book1psyche_bodyDF = uploadextractedConceptInstances("extractedSentiments/book1_occ/concept_occ4.csv")
book1natureDF = uploadextractedConceptInstances("extractedSentiments/book1_occ/concept_occ5.csv")
book1deatheDF = uploadextractedConceptInstances("extractedSentiments/book1_occ/concept_occ6.csv")
book1conceptsDict = {"justice":book1justiceDF,"reason":book1reasonDF,"power":book1powerDF,"providence":book1providenceDF,"pscyche_body":book1psyche_bodyDF,"nature":book1natureDF,"death":book1deatheDF}

book2justiceDF = uploadextractedConceptInstances("extractedSentiments/book2_occ/concept_occ0.csv")
book2reasonDF = uploadextractedConceptInstances("extractedSentiments/book2_occ/concept_occ1.csv")
book2powerDF = uploadextractedConceptInstances("extractedSentiments/book2_occ/concept_occ2.csv")
book2providenceDF = uploadextractedConceptInstances("extractedSentiments/book2_occ/concept_occ3.csv")
book2psyche_bodyDF = uploadextractedConceptInstances("extractedSentiments/book2_occ/concept_occ4.csv")
book2natureDF = uploadextractedConceptInstances("extractedSentiments/book2_occ/concept_occ5.csv")
book2deatheDF = uploadextractedConceptInstances("extractedSentiments/book2_occ/concept_occ6.csv")
book2conceptsDict = {"justice":book2justiceDF,"reason":book2reasonDF,"power":book2powerDF,"providence":book2providenceDF,"pscyche_body":book2psyche_bodyDF,"nature":book2natureDF,"death":book2deatheDF}

book3justiceDF = uploadextractedConceptInstances("extractedSentiments/book3_occ/concept_occ0.csv")
book3reasonDF = uploadextractedConceptInstances("extractedSentiments/book3_occ/concept_occ1.csv")
book3powerDF = uploadextractedConceptInstances("extractedSentiments/book3_occ/concept_occ2.csv")
book3providenceDF = uploadextractedConceptInstances("extractedSentiments/book3_occ/concept_occ3.csv")
book3psyche_bodyDF = uploadextractedConceptInstances("extractedSentiments/book3_occ/concept_occ4.csv")
book3natureDF = uploadextractedConceptInstances("extractedSentiments/book3_occ/concept_occ5.csv")
book3deatheDF = uploadextractedConceptInstances("extractedSentiments/book3_occ/concept_occ6.csv")
book3conceptsDict = {"justice":book3justiceDF,"reason":book3reasonDF,"power":book3powerDF,"providence":book3providenceDF,"pscyche_body":book3psyche_bodyDF,"nature":book3natureDF,"death":book3deatheDF}

book4justiceDF = uploadextractedConceptInstances("extractedSentiments/book4_occ/concept_occ0.csv")
book4reasonDF = uploadextractedConceptInstances("extractedSentiments/book4_occ/concept_occ1.csv")
book4powerDF = uploadextractedConceptInstances("extractedSentiments/book4_occ/concept_occ2.csv")
book4providenceDF = uploadextractedConceptInstances("extractedSentiments/book4_occ/concept_occ3.csv")
book4psyche_bodyDF = uploadextractedConceptInstances("extractedSentiments/book4_occ/concept_occ4.csv")
book4natureDF = uploadextractedConceptInstances("extractedSentiments/book4_occ/concept_occ5.csv")
book4deatheDF = uploadextractedConceptInstances("extractedSentiments/book4_occ/concept_occ6.csv")
book4conceptsDict = {"justice":book4justiceDF,"reason":book4reasonDF,"power":book4powerDF,"providence":book4providenceDF,"pscyche_body":book4psyche_bodyDF,"nature":book4natureDF,"death":book4deatheDF}


allConceptObjDict = {"1":book1conceptsDict,"2":book2conceptsDict,"3":book3conceptsDict,"4":book4conceptsDict}

'''
for key in allConceptObjDict:
        print(key)
        for key2 in allConceptObjDict[key]:
            if key2 == "justice":
                justiceDf = allConceptObjDict[key][key2]
                for row_idx, row in justiceDf.iterrows():
                    print(type(row))
                    for item_idx, item in row.iteritems():
                        if item_idx == "Chapter" and item == 17:
                            print(item_idx, "-->", item)
                            print("This is the concept keyword - ", row['Word'])          #create triple for adding the keyword  here - needs a URI creation script!!
                            print("This is the number of occurances -",row['Occurences']) #create triple for adding the number of occurences here
                            print("Philosophical concept being refferd to is -", key2)    #create triple for adding the concept class of keyword here
'''

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

# da fare >> need to add the uri creator and triple creator
def addconceptstriples(fragIRI,booknum,position):
    triples = Graph()
    for key in allConceptObjDict:
        if key == str(booknum):
            for key2 in allConceptObjDict[key]:
                if key2 == "justice":
                    justiceDf = allConceptObjDict[key][key2]
                    for row_idx, row in justiceDf.iterrows():
                        for item_idx, item in row.iteritems():
                            if item_idx == "Chapter" and item == position:
                                print(item_idx, "-->", item)
                                row_word = str(row['Word'])
                                row_word.replace(" ","_")
                                print("This is the concept keyword - ", row['Word']) #"https://w3id.org/arco/ontology/core/keyword/"         #create triple for adding the keyword
                                triples.add((fragIRI,hasAssociatedConcept,URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/")))
                                print("This is the number of occurances -",row['Occurences']) 
                                #triples.add(())      #create triple for adding the number of occurences here #UPDATE ONTOLOGY!
                                print("Philosophical concept being refferd to is -", key2) 
                                triples.add((URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/"),isCategoryOfIRI,justiceIRI))   
                                #triples.add(())      #create triple for adding the concept class of keyword here

                elif key2 == "reason":
                    reasonDf = allConceptObjDict[key][key2]
                    for row_idx, row in reasonDf.iterrows():
                        for item_idx, item in row.iteritems():
                            if item_idx == "Chapter" and item == position:
                                print(item_idx, "-->", item)
                                row_word = str(row['Word'])
                                row_word.replace(" ","_")
                                print("This is the concept keyword - ", row['Word'])          #create triple for adding the keyword  here - needs a URI creation script!!
                                triples.add((fragIRI,hasAssociatedConcept,URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/")))
                                print("This is the number of occurances -",row['Occurences']) #create triple for adding the number of occurences here
                                print("Philosophical concept being refferd to is -", key2)    #create triple for adding the concept class of keyword here
                                triples.add((URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/"),isCategoryOfIRI,reasonIRI))

                elif key2 == "power":
                    powerDf = allConceptObjDict[key][key2]
                    for row_idx, row in powerDf.iterrows():
                        for item_idx, item in row.iteritems():
                            if item_idx == "Chapter" and item == position:
                                print(item_idx, "-->", item)
                                row_word = str(row['Word'])
                                row_word.replace(" ","_")
                                print("This is the concept keyword - ", row['Word'])          #create triple for adding the keyword  here - needs a URI creation script!!
                                triples.add((fragIRI,hasAssociatedConcept,URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/")))
                                print("This is the number of occurances -",row['Occurences']) #create triple for adding the number of occurences here
                                print("Philosophical concept being refferd to is -", key2)    #create triple for adding the concept class of keyword here
                                triples.add((URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/"),isCategoryOfIRI,powerIRI))

                elif key2 == "providence":
                    providenceDf = allConceptObjDict[key][key2]
                    for row_idx, row in providenceDf.iterrows():
                        for item_idx, item in row.iteritems():
                            if item_idx == "Chapter" and item == position:
                                print(item_idx, "-->", item)
                                row_word = str(row['Word'])
                                row_word.replace(" ","_")
                                print("This is the concept keyword - ", row['Word'])          #create triple for adding the keyword  here - needs a URI creation script!!
                                triples.add((fragIRI,hasAssociatedConcept,URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/")))
                                print("This is the number of occurances -",row['Occurences']) #create triple for adding the number of occurences here
                                print("Philosophical concept being refferd to is -", key2)    #create triple for adding the concept class of keyword here
                                triples.add((URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/"),isCategoryOfIRI,providenceIRI))

                elif key2 == "pscyche_body":
                    bodyDf = allConceptObjDict[key][key2]
                    for row_idx, row in bodyDf.iterrows():
                        for item_idx, item in row.iteritems():
                            if item_idx == "Chapter" and item == position:
                                print(item_idx, "-->", item)
                                row_word = str(row['Word'])
                                row_word.replace(" ","_")
                                print("This is the concept keyword - ", row['Word'])          #create triple for adding the keyword  here - needs a URI creation script!!
                                triples.add((fragIRI,hasAssociatedConcept,URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/")))
                                print("This is the number of occurances -",row['Occurences']) #create triple for adding the number of occurences here
                                print("Philosophical concept being refferd to is -", key2)    #create triple for adding the concept class of keyword here
                                triples.add((URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/"),isCategoryOfIRI,psychebodyIRI))

                elif key2 == "nature":
                    natureDf = allConceptObjDict[key][key2]
                    for row_idx, row in natureDf.iterrows():
                        for item_idx, item in row.iteritems():
                            if item_idx == "Chapter" and item == position:
                                print(item_idx, "-->", item)
                                row_word = str(row['Word'])
                                row_word.replace(" ","_")
                                print("This is the concept keyword - ", row['Word'])          #create triple for adding the keyword  here - needs a URI creation script!!
                                triples.add((fragIRI,hasAssociatedConcept,URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/")))
                                print("This is the number of occurances -",row['Occurences']) #create triple for adding the number of occurences here
                                print("Philosophical concept being refferd to is -", key2)    #create triple for adding the concept class of keyword here
                                triples.add((URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/"),isCategoryOfIRI,natureIRI))
                    
                elif key2 == "death":
                    deathDf = allConceptObjDict[key][key2]
                    for row_idx, row in deathDf.iterrows():
                        for item_idx, item in row.iteritems():
                            if item_idx == "Chapter" and item == position:
                                print(item_idx, "-->", item)
                                row_word = str(row['Word'])
                                row_word.replace(" ","_")
                                print("This is the concept keyword - ", row['Word'])          #create triple for adding the keyword  here - needs a URI creation script!!
                                triples.add((fragIRI,hasAssociatedConcept,URIRef("https://w3id.org/arco/ontology/core/"+row['Word'].replace(" ","_")+"/")))
                                print("This is the number of occurances -",row['Occurences']) #create triple for adding the number of occurences here
                                print("Philosophical concept being refferd to is -", key2)    #create triple for adding the concept class of keyword here
                                triples.add((URIRef("https://w3id.org/arco/ontology/core/"+row_word+"/"),isCategoryOfIRI,deathIRI))

    return triples

def addsentimentstriples(fragIRI,booknum,position):
    triples = Graph()
    for key in allSentimentsDict:
        if key == str(booknum):
            datadf = allSentimentsDict[key]
            for row in datadf.itertuples():
                row = pd.Series(row, index=['index','unnamed','Book', 'BookChapter','Negative','Neutral','Positive'])
                if row['BookChapter'] == float(position):
                    print("This fragment has ",row['Positive']*100,"% positive sentiments")
                    #print("This fragment has ",row['Negative']*100,"% negative sentiments")
                    #print("This fragment has ",row['Neutral']*100,"% neutral sentiments")
                    triples.add((fragIRI,positiveIRI,Literal(row['Positive']*100)))
                    triples.add((fragIRI,negativeIRI,Literal(row['Negative']*100)))
                    triples.add((fragIRI,neutralIRI,Literal(row['Neutral']*100)))
    #create the triples for the instance if required
    
    return triples
# da fare >>  pin point the position before making triples!
def addAgentsTriples(fragIRI,booknum,position):
    #other agent roles IRIs
    DemocritusIRI = URIRef("https://w3id.org/arco/ontology/core/Democritus")
    EpictetusIRI = URIRef("https://w3id.org/arco/ontology/core/Epictetus")
    EuripidesIRI = URIRef("https://w3id.org/arco/ontology/core/Euripides")
    HeraclitusIRI = URIRef("https://w3id.org/arco/ontology/core/Heraclitus")
    HomerIRI = URIRef("https://w3id.org/arco/ontology/core/Homer")
    triples = Graph()
    for key in allFragments:
            if key == booknum:
                for key2 in allFragments[key]:
                    if key2 == "fragmentlist":
                        location = 1
                        for item in allFragments[key][key2]:
                            if location == position:
                                one = "<Democritus>"
                                
                                two = '<Epictetus>'
                            
                                three = '<Euripides>'

                                four = '<Heraclitus>'

                                five = '<Homer>'
                                if one in item:
                                    print("HAS SOMETHING ")
                                    triples.add((fragIRI,hasAssociatedAgent,DemocritusIRI))
                                if two in item:
                                    print("HAS SOMETHING ")
                                    triples.add((fragIRI,hasAssociatedAgent,EpictetusIRI))
                                if three in item:
                                    print("HAS SOMETHING ")
                                    triples.add((fragIRI,hasAssociatedAgent,EuripidesIRI))
                                if four in item:
                                    print("HAS SOMETHING ")
                                    triples.add((fragIRI,hasAssociatedAgent,HeraclitusIRI))
                                if five in item:
                                    print("HAS SOMETHING ")
                                    triples.add((fragIRI,hasAssociatedAgent,HomerIRI))
                            location += 1
    return triples

# da fare >>
def addAbstractFigure(fragIRI,booknum,position):
    pass

# itterate over the list of fragments in books and create a URI for all
def KGraphcreator():
    #da fare
    chaptersDict = {}
    fragIRIdict = {}
    myGraph = Graph()
    #create triples for your author here
    authorIRI = URIRef("https://w3id.org/arco/ontology/core/MarcusAurelius")
    

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
            if key == bookId:
                for key2 in allFragments[key]:
                    fragLocalID = 1
                        #for example 1.1
                    if key2 == "fragmentlist":
                        for item in allFragments[key][key2]:  # item stores the fragment text data here
                            fragUniID = str(bookId) + "." + str(fragLocalID)
                            fragIRI = URIRef(baseIRI + str(fragUniID))   
                            #append the fragIRI to a dict
                            fragIRIdict.update({fragUniID:fragIRI})
                            
                            #connect the frag to the chapter
                            myGraph.add((chaptersubj,hasPartIRI,fragIRI))
                            myGraph.add((fragIRI,containsTextIRI,Literal(item))) #adds the text to the fragment 

                            #add concepts to this fragment
                            C_triples = addconceptstriples(fragIRI,bookId,fragLocalID)
                            myGraph = myGraph + C_triples

                            #add sentiments to this fragment 
                            S_triples = Graph()
                            S_triples = addsentimentstriples(fragIRI,bookId,fragLocalID)
                            myGraph = myGraph + S_triples
                            
                            #add agents to this fragment
                            A_triples =addAgentsTriples(fragIRI,bookId,fragLocalID)
                            myGraph = myGraph + A_triples
                            
                            #add abstract figures to this fragment
                            #abst_triples = Graph(addAbstractFigure(fragIRI,bookId,fragLocalID))
                            #myGraph = myGraph + abst_triples
                            
                            #now change the id for the next fragment
                            fragLocalID += 1
                            #pushing the data for this fragment and its URI to a bigger dict called FragmentsIRIdata
                            FragmentsIRIdata.update({fragUniID:fragIRIdict})
            else:
                pass      
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
uploadtxt("txt/MeditationsBook4.txt")

fragmentor(allTxt)

#DRIVER CODE FOR VIEWING THE DICT OF FRAMENTS >>
'''
for key in allFragments:
    print(key)
    for key2 in allFragments[key]:
        print(allFragments[key][key2])
'''        

#print(literaryDiaryname)

#DRIVER CODE FOR CREATING THE KNOWLEDGE GRAPH FROM THE TEXT
KGraphcreator()
#print(FragmentsIRIdata)

'''

def traveller():
    for items in allTxt:
        #create your triples for book class instance here
        #create triples for each fragment of individual chapter
        for key in allFragments:
            for key2 in allFragments[key]:
                if key2 == "fragmentlist":
                    #print (allFragments[key][key2])
                    for item in allFragments[key][key2]:
                        print(item)
'''
#traveller()

#TESTING THE CONCEPT TRIPLE TRAVELLER
#addconceptstriples(fragmentIRI,2,11)

#TESTING THE SENTIMENTS TRIPLE TRAVELLER
#addsentimentstriples(fragmentIRI,"2",11)