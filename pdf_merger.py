

"""
TO DO:

-Add feature to merge all pdf files in folder.
-Add support for full path names when calling merge_pdfs_from_text_file()
-Add feature to create backup folder instead of deleting files.
-get module on PyPi
-rebuild as a class instead of just functions

"""




from PyPDF2 import PdfFileReader, PdfFileMerger
import os

# Reads a text file that contains a list of file names containing just the
# filename or the full filename and path and merges them into a pdf file.

# takes in a list of full-path-file-names and deletes them.
# returns a custom message
def del_list_of_files(fullPathFileNames, msg):
    for fn in fullPathFileNames:
        f = os.open(fn, os.O_RDONLY)
        os.close(f)
        os.remove(fn)
    print msg


def getFileNamesList(textFileName, isFullPath, containingFolder):
    # get the textFileNames/pathNames from the text file
    f = open(textFileName, "r")

    if isFullPath:
        textFileNames = [] # empty list
        for line in f:
            tmpStr = line
            tmpStr = tmpStr.replace("\n", "") # removes newline if it exists
            tmpStr = tmpStr.translate(None, "\"") # removes " if exist.
            textFileNames.append(tmpStr)
    else:
        textFileNames = [] # empty list
        for line in f:
            tmpStr = line
            tmpStr = tmpStr.replace("\n", "") # removes newline if it exists
            tmpStr = tmpStr.translate(None, "\"") # removes " if exist.
            tmpStr = containingFolder + "\\" + tmpStr
            textFileNames.append(tmpStr)
    f.close()

    return textFileNames

# takes in a list of strings that is a file's full path and filename
# and merges those pdfs into a single pdf
def merge_pdfs_from_text_file(textFileName,
                            mergedtextFileName,
                            containingFolder,
                            isFullPath,
                            delMergedFiles
                            ):
    mergedtextFileNameAndPath = containingFolder + "\\" + mergedtextFileName
    
    textFileNames = getFileNamesList(textFileName, isFullPath, containingFolder)

    merger = PdfFileMerger()
    pgNm = 1

    for fn in textFileNames:
        with open(fn, 'rb') as pdf:
            print "Merging: {}".format(fn)
            merger.merge(pgNm, pdf)
        pgNm += 1
    merger.write(mergedtextFileNameAndPath)

    if delMergedFiles:
        del_list_of_files(textFileNames,"Old files deleted.")
