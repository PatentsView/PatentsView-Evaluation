import stringcompare
import pandas as pd
import numpy as np
import wget
import zipfile
import os
from timeit import timeit

if not os.path.isfile("rawinventor.tsv"):
    wget.download("https://s3.amazonaws.com/data.patentsview.org/download/rawinventor.tsv.zip")
    with zipfile.ZipFile("rawinventor.tsv.zip", 'r') as zip_ref:
        zip_ref.extractall(".")
    os.remove("rawinventor.tsv.zip")

def get_word(name):
    index = name.find(' ')
    if(index != -1):
        return name[0: index]
    else:
        return name

def get_sequence(patent_id, name_first, name_last, name_middle, suffix):

    if patent_id in rawinventor.index:
        #combined names
        first_half = name_first
        second_half = name_last

        #concat middle name/initial
        if name_middle != "&":
            first_half += " " + name_middle

        #concat suffix
        if suffix != "&":
            if suffix == "2nd":
                suffix == "II"
            elif suffix == "3rd":
                suffix == "III"
            second_half += " " + suffix

        #dat = rawinventor[rawinventor.patent_id == patent_id]
        dat = rawinventor.loc[patent_id]
        last_distances = comparator.pairwise([second_half.lower()], dat.name_last.str.lower().values)[0]
        first_distances = comparator.pairwise([first_half.lower()], dat.name_first.str.lower().values)[0]

        #one last name match
        if sum(last_distances == 0) == 1: 
            return np.argmin(last_distances)

        #multiple last name matches
        elif sum(last_distances == 0) > 1:
            return np.argmin(first_distances)

        #close matches
        elif sum(last_distances < 0.2) >= 1:
            #record close data to close_match and return sequence number
            index = np.argmin(last_distances + first_distances)
            dict = {'patent_id': patent_id, 'name_last': second_half, 'name_first': first_half, 'index': index, 
                'referenced_last': dat.name_last[index], 'referenced_first': dat.name_first[index], 'type': "Close Match"}
            results.append(dict)
            return index
        
        #vague matches
        elif sum(last_distances < 0.3) >= 1 or sum(first_distances < 0.3) >= 1:
            #record vague data to vague_match and return sequence number
            index = np.argmin(last_distances + first_distances)
            dict = {'patent_id': patent_id, 'name_last': second_half, 'name_first': first_half, 'index': index, 
                'referenced_last': dat.name_last[index], 'referenced_first': dat.name_first[index], 'type': "Vague Match"}
            results.append(dict)
            return index

        #no matches
        else:
            #get first word for each name
            firsts = dat.apply(lambda x: get_word(x.name_first), axis=1)
            lasts = dat.apply(lambda x: get_word(x.name_last), axis=1)
            name_last = get_word(name_last)
            name_first = get_word(name_first)
            
            last_distances = comparator.pairwise([name_last.lower()], lasts.str.lower().values)[0]
            first_distances = comparator.pairwise([name_first.lower()], firsts.str.lower().values)[0]

            #check if first word matches -> half match, otherwise no match
            if sum(last_distances < 0.2) >= 1 and sum(first_distances < 0.2) >= 1:
                #record half word data to half_match and return sequence number
                index = np.argmin(last_distances + first_distances)
                dict = {'patent_id': patent_id, 'name_last': second_half, 'name_first': first_half, 'index': index, 
                    'referenced_last': dat.name_last[index], 'referenced_first': dat.name_first[index], 'type': "Half Match"}
                results.append(dict)
                return index
            else:
                #still record data but return "NaN"
                index = np.argmin(last_distances + first_distances)
                dict = {'patent_id': patent_id, 'name_last': second_half, 'name_first': first_half, 'index': index, 
                    'referenced_last': dat.name_last[index], 'referenced_first': dat.name_first[index], 'type': "No Match"}
                results.append(dict)
                return "NaN"
    else:
        #if key is not present in rawinventors.tsv
        dict = {'type': "No Match"}
        results.append(dict)
        return "NaN"

#reference dataset    
rawinventor = pd.read_csv("rawinventor.tsv", sep="\t", usecols=["patent_id", "sequence", "name_first", "name_last"], 
    dtype={"patent_id": "string", "sequence": "int16", "name_first": "string", "name_last": "string"})

#sort to improve speed
rawinventor.set_index(['patent_id', 'sequence'], inplace=True)
rawinventor.sort_index(inplace=True)

comparator = stringcompare.Levenshtein()

#lai_benchmark = pd.read_excel("benchmark.xlsx", dtype=str).iloc[3:, :]
lai_benchmark = pd.read_csv("patents_2005_012.tsv", sep="\t", usecols=["patent", "fname", "mname", "lname", "suffix"], 
    dtype="string")

#stored variable
results = []
lai_benchmark["sequence"] = lai_benchmark.apply(lambda x: get_sequence(x.patent, x.fname, x.lname, x.mname, x.suffix), axis=1)

#write to two files
lai_benchmark.to_csv('patents_2005_012_autosequence.csv')
pd.DataFrame(results).to_csv('results.csv')