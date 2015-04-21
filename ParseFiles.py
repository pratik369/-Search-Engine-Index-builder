import FileName
import os
import gzip
import tokenize
import pickle


def read_files():

    #path = "/Users/PRATIK/PycharmProjects/InvertedIndex/nz2_merged/"
    path = "/Users/vivek/PycharmProjects/inverted_index/nz2_merged"
    index_list, data_list = GetFileName.getFiles(path)                     # gets all the index and data files names into their respective lists

    j = 0
    link = []
    test1 = ""
    fileindex = 0
    counter = 1

    filept = open('temp', 'wb')                                         # temporary file in which temporary postings are saved

    for i in range(len(index_list)):
        try:
            fname = path+"/"+index_list[i]                              # fname keeps the name of current index file which will be processed
            dname = path+"/"+data_list[i]                               # dname keeps the name of current data file which will be processed
            print "Index: "+str(fname)
            print "Data: "+str(dname)
            with gzip.open(fname, "rb") as f:                           # Following block of code is used to parse the html page..tokenize the words..and create the intermediate index files
                with gzip.open(dname, "rb") as datapt:
                    for line in f:
                        test1 = line
                        temp = []
                        temp = line.split()

                        data = datapt.read(int(temp[3]))

                        flag = tokenizeWords.flagstatus(data)

                        dictionary = {}

                        if flag:

                            dictionary = tokenizeWords.parse(data)
                            #print dictionary
                            if len(dictionary) != 0:
                                link.append(temp[0])

                                for word in dictionary:

                                    data = dictionary[word]

                                    if counter == 150000:
                                        filept.close()
                                        os.system("sort -b --output=index-"+str(fileindex)+" temp")
                                        os.remove('temp')
                                        fileindex += 1
                                        filept = open('temp', 'wb')
                                        counter = 1

                                    counter += 1

                                    filept.write(word+" "+str(data)+" "+str(len(data))+" "+str(j)+"\n")

                                    #text_string = word+" "+str(data)+" "+str(len(data))+" "+str(j)+"\n"
                                    #pickle.dump(text_string, filept)

                                j += 1


        except Exception as e:
            print "Error..."
            print "Index: "+str(fname)
            print "Link: "+str(test1)
            print e
            pass

    if counter > 0 and counter < 150000:
        filept.close()
        os.system("sort -b --output=index-"+str(fileindex)+" temp")
        os.remove('temp')


    final = open("Url_Table.txt", 'w')

    print "Length: "+str(len(link))

    for j in range(len(link)):
        final.write(str(j) + "\t" + link[j] + "\r")

    final.close

    return

