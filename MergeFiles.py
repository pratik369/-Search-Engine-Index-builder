import heapq
from os import listdir
import re


sortList = []


def mergeFiles():
    try:
        path = "/Users/vivek/PycharmProjects/inverted_index"        # path of intermediate index files
        index_file = []

        for f in listdir(path):                                     # Following block of code is used to find all the intermediate index files
            if re.search('index-', f):
                index_file.append(f)

        print index_file

        filept = []                                                 # following block of code copies the content of index_file list into filept list                                                
        for i in range(len(index_file)):
            filept.append(i)

        index = 0
        for file in index_file:                                     # In Following block of code n files are opened to perform n-way merge.
            filept[index] = open(file, 'rb')
            index += 1

        f3 = open("result.txt", 'wb')                               # Final inverted Index is stored in this file.
        lexfile = open("lexicon.txt", 'wb')                         # Lexicon structure is stored in this file.

        print "Start...!!!"

        document_list = []
        frequency_list = []

        for i in range(len(filept)):                                # Following block of code pushes the first line of all the intermidiate index files into heap
            heapq.heappush(sortList, (filept[i].readline(), i))

        word_extra = heapq.heappop(sortList)                        
        first = word_extra[0].split(' ')
        previous = first[0]
        heapq.heappush(sortList, (word_extra[0], word_extra[1]))

        line = 0
        templine = 0
        startline = 1

        
        """
        Following block of code implements N n-way merge sort.

        """

        while len(sortList) > 0:

            word = heapq.heappop(sortList)
            temp = word[0].split(' ')

            if previous == temp[0]:
                document_list.append(temp[1])
                frequency_list.append(temp[2])
                templine += 1

            else:
                if len(document_list) == 0:
                    document_list.append(temp[1])
                    frequency_list.append(temp[2])

                f3.write(previous+" "+str(document_list)+" "+str(frequency_list)+"\n")
                lexfile.write(previous+" "+str(startline)+" "+str(templine)+"\n")

                #lexfile.write(previous + " " + str(startline) + " " + str(templine) + "\n")
                startline = line
                previous = temp[0]
                templine = 1

                document_list = []
                frequency_list = []

            #f3.write(word[0])

            text1 = filept[word[1]].readline()
            if text1:
                heapq.heappush(sortList, (text1, word[1]))


            line += 1



        if previous == temp[0]:
            #lexfile.write(previous + " " + str(startline) + " " + str(templine) + "\n")
            f3.write(previous+" "+str(document_list)+" "+str(frequency_list)+"\n")
            lexfile.write(previous+" "+str(startline)+" "+str(templine)+"\n")

        print "End...!!!"

        for file in filept:
            file.close()

        lexfile.close()
        f3.close()

    except Exception as e:
        print e