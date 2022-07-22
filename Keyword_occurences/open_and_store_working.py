# import re
# import os
# from pandas import DataFrame 


# #This is a function that takes as input a text file (in case each book) and our list of concepts. 
# #It splits each book into its fragments and retrieves the number of concept occurences in each fragment.

# def create_csv(text_file_path, concept_list,chapter_num_path):
#     with open(text_file_path,encoding='UTF-8') as f:

#         book = f.read()
#         book_l=re.split('\d+\.', book)
#         bookch=list()
#         text=list()
#         for index, chapter in enumerate(book_l, start=0):
#             bookch.append(index)
#             text.append(chapter)
#             #!Extra code if we want chapters and text into a dataframe
#             # data={'BookChapter':bookch, "Text":text}
#             # book1_df=DataFrame(data,index=None)
#             # book1_df=book1_df.iloc[1: , :]
#             # book1_df.reset_index(drop=True)   #Store the book text in a dataframe where each row is a chapter
    
#     def count_concept_occ(text,keyword_l):
#         chapter_l=[]
#         word_l=[]
#         count_l=[]
#         for index, chapter in enumerate(text,start=0):
#             for i in keyword_l:
#                 if i in chapter:
#                     chapter_l.append(index)
#                     word_l.append(i)
#                     count_l.append(chapter.count(i))

#         keyword_dict={"Chapter":chapter_l,"Concept Instance":word_l, "Occurences":count_l } 
#         df_occ=DataFrame.from_dict(keyword_dict)
#         return df_occ
        

#     os.makedirs(chapter_num_path, exist_ok=True) 

#     num=0
#     for l in concept_list:
#         a_path=chapter_num_path
#         a_file="concept_occ"
#         a=(count_concept_occ(text,l))
        
#         a_file=a_file+str(num)
#         a.to_csv(os.path.join(a_path, (a_file+'.csv')))
#         num+=1
    
#     return True



# justice=['justice','action','blame','fault','honour','temperance']
# reason=['reason','ignorance','judgement','mind','principle','truth']
# power=['power','corrupt','employment','glory','governing self','obstacle',]
# providence=['providence','atoms','divinity','fate','fortune','god']
# psy_body=['psyche and body','psyche','body','flesh','impulse','souls','vital spirit']
# nature=['nature','law','matter', 'necessity','universe','whole']
# death=['death','dissolution','extinct','life','sick','time']  #life and time is super general?? can lead to bias

# concept_instances=[justice,reason,power,providence,psy_body,nature,death]

# concept_instances_str=[i[0] for i in concept_instances] #as a way to get columns/filenames based on concept name later

# #Book_1
# print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook1.txt',concept_instances,"book_1_occ"))

    
import re
import os
from pandas import DataFrame 


#This is a function that takes as input a text file (in our case case each book) and our list of concepts. 
#It splits each book into its fragments and retrieves the number of concept occurences in each fragment.
reg='[\.?;!]*\b'
def create_csv(text_file_path, concept_list,chapter_num_path):
    with open(text_file_path,encoding='UTF-8') as f:

        book = f.read()
        book_l=re.split('\d+\.', book)
        bookch=list()
        text=list()
        for index, chapter in enumerate(book_l, start=0):
            bookch.append(index)
            text.append(chapter)
            #!Extra code if we want chapters and text into a dataframe
            data={'BookChapter':bookch, "Text":text}
            book1_df=DataFrame(data,index=None)
            book1_df=book1_df.iloc[1: , :]
            book1_df.reset_index(drop=True)   #Store the book text in a dataframe where each row is a chapter
            #print(book1_df)
    
    def count_concept_occ(text,keyword_l):
        chapter_l=[]
        word_l=[]
        count_l=[]
        for index, chapter in enumerate(text,start=0):
            for i in keyword_l:
                if re.search(i, chapter):
                     #regex matches optional word boundary and punctuation
                    chapter_l.append(index)
                    word_l.append("God")
                    count_l.append(len(re.findall(i,chapter)))
        #keyword_l_str=[i[0] for i in keyword_l]
        keyword_dict={"Chapter":chapter_l,'Word':word_l, "Occurences":count_l } 
        df_occ=DataFrame.from_dict(keyword_dict)
        return df_occ
        

    os.makedirs(chapter_num_path, exist_ok=True) 

    num=0
    for l in concept_list:
        a_path=chapter_num_path
        a_file="abstr_occ"
        a=(count_concept_occ(text,l))
        
        a_file=a_file+str(num)
        a.to_csv(os.path.join(a_path, (a_file+'.csv')))
        num+=1
    
    return True



justice=['justice','action','blame','fault','honour','temperance']
reason=['reason','ignorance','judgement','mind','principle','truth']
power=['power','corrupt','employment','glory','governing self','obstacle',]
providence=['providence','atoms','divinity','fate','fortune','god']
psy_body=['psyche and body','psyche','body','flesh','impulse','souls','vital spirit']
nature=['nature','law','matter', 'necessity','universe','whole']
death=['death','dissolution','extinct','life','sick','time']  #life and time is super general?? can lead to bias

concept_instances=[justice,reason,power,providence,psy_body,nature,death]

concept_instances_str=[i[0] for i in concept_instances] #as a way to get columns/filenames based on concept name later
god=['(?<!\w)(G|g)od[s]*(?!\w)']
men=['(?<!\w)(M|m)(e|a)n(?!\w)']
abstract_fig=[god]
#Book_1
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook1.txt',abstract_fig,"book1_occ"))
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook2.txt',abstract_fig,"book2_occ"))
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook3.txt',abstract_fig,"book3_occ"))
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook4.txt',abstract_fig,"book4_occ"))
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook5.txt',abstract_fig,"book5_occ"))
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook6.txt',abstract_fig,"book6_occ"))
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook7.txt',abstract_fig,"book7_occ"))
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook8.txt',abstract_fig,"book8_occ"))
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook9.txt',abstract_fig,"book9_occ"))
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook10.txt',abstract_fig,"book10_occ"))
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook11.txt',abstract_fig,"book11_occ"))
print(create_csv('/Users/macuser/Desktop/KRKE-Meditations/MAtext Occurences/MAtext/MeditationsBook12.txt',abstract_fig,"book12_occ"))
