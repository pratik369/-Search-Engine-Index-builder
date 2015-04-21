__author__ = 'vivek and pratik'


import StringIO
import nltk
import re
from nltk.corpus import stopwords

#check = re.compile(r"^[a-z0-9]")

"""

Following block of code is used to remove stop words from cleaned html page

"""


def removestopwords(wrd):

    str = ""
    str1 = ""
    stop = stopwords.words('english')
    for i in wrd.split():
        #str1 += i+" "
        if i not in stop:
            str += i+" "

    return str.strip()#, str1.strip()


"""
Following Block of code is used to find the ocurrence of the particular word and its frequency. Also it is used for delta Compression. 

"""

def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError as v:
            break

    extra_match = []

    # Delta Compression
    if len(indices) > 1:
        extra_match.append(indices[0])
        for i in range(1, len(indices)):
            extra_match.append(indices[i] - indices[i-1])

        return extra_match

    return indices


"""
Following Block of code is used to check the status of the page is 200 or not. If its not ok then we skip the file.

"""


def flagstatus(data):

    try:
        buf = StringIO.StringIO(data)

        line = buf.readline()

        if line.__contains__("200 OK"):
            return True
        else:
            return False
    except Exception as e:
        print "Test Function Error...!!!"
        print e
        return False


"""
Following block of code tokenizes the html page using nltk library and returns the list of words and their position as well as their frequency

"""



def parse(data):

    data = data.lower()

    global check

    if data.__contains__("<html"):

        index = data.index("<html")
        try:
            page = data[index:]

            page_clean = (nltk.clean_html(page)).strip()
            page_data = re.sub(r'[^a-z0-9 ]+', ' ', page_clean)

            page_clean_stop = removestopwords(page_data)

            #page_data = re.sub(r'[^a-z0-9 ]+', ' ', page_data)

            #page_data = page_data.split(' ')

            words = page_clean_stop.split(' ')

            dictionary = {}

            for word in words:

                if len(word) <= 25:

                    location = []
                    location = all_indices(word, page_data)
                    dictionary[word] = location

            return dictionary

        except Exception as e:
            print e
            return {}
    else:
        return {}