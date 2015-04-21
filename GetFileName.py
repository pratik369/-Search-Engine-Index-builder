from os import listdir
import re


def getFiles(path):

    print path

    index_list = []                     # saves the list of index files
    data_list = []                      # saves the list of data files

    for f in listdir(path):             # Following block of code is used to get list of index and data files from a given directory
        #print f
        if re.search('_index', f):  
            index_list.append(f)
        if re.search('_data', f):
            data_list.append(f)
           #print f

    index_list.sort()                   # used to sort the index list
    data_list.sort()                    # used to sort the data list

    return index_list, data_list        # returns both index and data list


