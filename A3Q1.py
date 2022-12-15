"""This is the program "A3Q1.py" that provides the answer to
questions 1.1 and 1.2 of Assignment 3.

Author: Lucas Papadatos
Student number: 20233257
"""
import os

class WebPageIndex:
    """This is the initialization function that removes all punctuation
    and stores each word of the file into an array. It has the file path
    as a parameter.
    """
    def __init__(self,file):
        self.file = file
        doc = open(file,"r")
        text = doc.read().lower()
        comma = text.replace(","," ")
        lbracket = comma.replace("("," ")
        rbracket = lbracket.replace(")"," ")
        period = rbracket.replace("."," ")
        colon = period.replace(":"," ")
        words = colon.replace("/"," ")
        self.wordList = words.split()

    """This is the get count that returns the number of times a word is
    in a document.
    """
    def getCount(self,s):
        count = 0
        for word in self.wordList:
            if word == s.lower():
                count+=1
        return count        

class WebpagePriorityQueue:
    """This is the initialization function for the WebpagePriorityQueue
    class that takes a query and a set of webpage index instances. It creates
    a list of priority values and creates a max heap with the priority values
    and document names.
    """
    def __init__(self,query,wpIndex):
        self.priorityVals = []
        if (" " in query): # checks if query contains more than one word
            queries = query.split()
            for doc in wpIndex:
                sum = 0
                for word in queries:
                    sum += doc.getCount(word)
                self.priorityVals.append(sum)
        else:
            for doc in wpIndex:
                self.priorityVals.append(doc.getCount(query))
        # made copy of priority list to keep index for priorities
        self.priorityCopy = self.priorityVals.copy()
        WebpagePriorityQueue.buildHeap(self.priorityCopy, len(self.priorityCopy))
        WebpagePriorityQueue.printHeap(self.priorityVals, self.priorityCopy, wpIndex)

    """This is the heapify function which is recursively called to create a
    max heap with the priority values as a list.
    """
    def heapify(pri,len,i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len and pri[left] > pri[largest]: # left child larger than root
            largest = left
        if right < len and pri[right] > pri[largest]: #  right child larger than root
            largest = right
        if largest != i: # largest is not root
            pri[i], pri[largest] = pri[largest], pri[i]
            WebpagePriorityQueue.heapify(pri, len, largest)
    
    """This is the buildHeap function that builds the max heap from the 
    priority values list.
    """
    def buildHeap(pri,len):
        start = len // 2 - 1
        for i in range(start, -1, -1):
            WebpagePriorityQueue.heapify(pri, len, i)

    """This is the printHeap function to print the heap in list form.
    """
    def printHeap(priO,pri,wpIndex):
        l = len(priO)
        print("Max Heap:")
        for i in range(l):
            print(pri[i],end=" ")
        print()

    """This is the peek function that returns the WebpageIndex with the
    highest priority, without removing it.
    """
    def peek(self,wpIndex):
        hp = self.priorityCopy[0]
        index = self.priorityVals.index(hp)   
        doc = wpIndex[index].file
        return doc
    
    """This is the poll function that removes and returns the WebpageIndex 
    with the highest priority.
    """
    def poll(self,wpIndex):
        hp = self.priorityCopy[0]
        index = self.priorityVals.index(hp)
        doc = wpIndex[index].file
        wpIndex.pop(index)
        return doc
    
    """This is the reheap function that takes a new query as a parameter 
    and reheaps the WebpagePriorityQueue.
    """
    def reheap(self,query,wpq):
        WebpagePriorityQueue.__init__(self,query,wpq)

    def get(self,key):
        #h1 = hash1fun(key)
        #h2 = hash2fun(key)
        h1 = 1
        h2 = 2
        while self.table[h1] is not None and not self.table[h1].key==key:
            h1 += h2
            h2 %= self.TABLE_SIZE
        return self.table[h1].value
def main():
    # 1.1
    path = os.path.join(os.getcwd(),'data\\')
    doc1 = path+"doc1-arraylist.txt"
    doc2 = path+"doc2-graph.txt"
    doc3 = path+"doc3-binarysearchtree.txt"
    doc4 = path+"doc4-stack.txt"
    doc5 = path+"doc5-queue.txt"
    doc6 = path+"doc6-AVLtree.txt"
    doc7 = path+"doc7-redblacktree.txt"
    doc8 = path+"doc8-heap.txt"
    doc9 = path+"doc9-hashtable.txt"

    # Must be initialized for 1.2 to work
    D1 = WebPageIndex(doc1)
    D2 = WebPageIndex(doc2)
    D3 = WebPageIndex(doc3)
    D4 = WebPageIndex(doc4)
    D5 = WebPageIndex(doc5)
    D6 = WebPageIndex(doc6)
    D7 = WebPageIndex(doc7)
    D8 = WebPageIndex(doc8)
    D9 = WebPageIndex(doc9)
    webpageIndices = [D1,D2,D3,D4,D5,D6,D7,D8,D9]
    print(D1.getCount("array"))

    # 1.2
    Q = WebpagePriorityQueue("binary tree", webpageIndices)
    print("Peek:", Q.peek(webpageIndices))
    Q.poll(webpageIndices)
    Q.reheap("array", webpageIndices)
    print("Peek:", Q.peek(webpageIndices))

if __name__ == "__main__":
    WebpagePriorityQueue.get("hell",3)