'''
Julio Hernandez
Lab#4
CS2302
TTR 1:30
Lab Purpose: This lab was to test the efficiency of a hash table with information used in Lab #3
'''

#node for hash class
class HashNode:
    def __init__(self, word, next):
        self.word = word
        self.next = next

#hash table class
class HashTable:

    #constructor for hash class
    def __init__(self, size):
        loadFactor = int(size)
        self.table = [None] * loadFactor
        self.size = loadFactor

    #assigns location to each insertiom
    def hash(self, word):
        bucket = 0
        for i in range(len(word)):
            #ID is created to give each word a unique code
            ID = ord(word[i])
            bucket += (ID ** i)
        return bucket % self.size

    #insertion method
    def insert(self, word):
        compare = 0
        bucket = self.hash(word)

        if self.table[bucket] != None:
            compare += 1

        self.table[bucket] = HashNode(word, self.table[bucket])
        return compare
    #search method
    def search(self, word):
        bucket = self.hash(word)
        holder = self.table[bucket]

        while holder != None:
            #lower is used to compare words without filtering capitalized words
            if holder.word.lower() == word.lower():
                return True
            holder = holder.next
        return False

    #method created to calculate the load factor
    def loadFactor(self, bucketsInTable):
        return bucketsInTable / self.size

#method used to populate the hash table
def tableFill(table, file):
    counter = 0
    for line in file:
        counter += table.insert(line)
    return counter

#method to calculate the number of anagrams
def anagrams(word, table, wordList, prefix="" ):
    if len(word) <= 1:
        str = prefix + word
        if table.search(str) == True:
            wordList.append(str)
            print(str)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:]
            if cur not in before:
                anagrams(before + after, table, wordList, prefix + cur)
    #count number of occurrences via list size
    return len(wordList)

#main method
def main():
    fileName = ""
    status = False

    #while loop to attain a correct input
    while status is False:
        try:
            #count is initialized to determine the size of the hash table
            count = 0
            fileName = input("Enter file name (make sure the extension is provided [.txt]): ")
            read = open(fileName+".txt", "r").read().split("\n")
            for line in read:
                count += 1
            status = True
        except FileNotFoundError:
            print("File not found. Please try again\n")

    #creation of the hashtable
    table = HashTable(count)

    #method to compare words
    compare = tableFill(table, read)

    #user interaction
    #user display of load factor
    print("Load Factor: ", round(table.loadFactor(count), 3))
    print("Average Comparisons: ", round(compare/count, 3))
    print("Word count for %s.txt: %d" % (fileName, count))
    print("****************************************************************************\n")
    word = input("Please enter a word: ").lower()

    #list is initialized
    wordList = []
    print("*********************************Anagrams***********************************")
    #method called to compute number of anagrams
    wordCount = anagrams(word, table, wordList)
    print("\nPossible anagrams found: %d" % (wordCount))
    print("**************************************************************************")

#main method call
main()
#end of program