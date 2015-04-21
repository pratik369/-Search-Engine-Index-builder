__author__ = 'Pratik Patel and Vivek Desai'

import ParseFiles
import merge


def main():

    ParseFiles.read_files()			# calls read_files() function which is defined in ParseFiles class.
    MergeFiles.mergeFiles()				# calls mergeFiles function which is defined in merge class.


if __name__=='__main__':
    main()
