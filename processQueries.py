"""This is the program "A3Q1.py" that provides the answer to
question 1.3 of Assignment 3.

Author: Lucas Papadatos
Student number: 20233257
"""
import A3Q1
import os
import glob

"""This is the readFiles function that takes an absolute path 
of the current working directory and attaches the filename to
add to a list of webpage index instances.
"""
def readFiles(path):
    webpageIndices = []
    docs = glob.glob(path+"doc*")
    for doc in docs:
        webpageIndices.append(A3Q1.WebPageIndex(doc))
    return webpageIndices

def main():
    # 3.3
    path = os.path.join(os.getcwd(),'data\\') # data folder path
    wpq = readFiles(path)
    queries = open("queries.txt","r").read().lower().splitlines()
    for query in queries:
        Q = A3Q1.WebpagePriorityQueue(query,wpq)
        print("Best match for '"+query+"': "+str(Q.peek(wpq)))
        print()

if __name__ == "__main__":
    main()