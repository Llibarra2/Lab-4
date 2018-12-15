class HashNode:
    def __init__(self, word, next):
        self.word = word
        self.next = next

class HashTable:
    '''
    load factor - is practically how much data we have in our table.
    
    (number of entries)
    -------------------
      (size of table)
    
    if we have an array of size 100 and 25 indexes are occupied then the laod factor is .25
    
    '''
    def __init__(self, size):
        #simple default loadFactor
        loadFactor = int(size * 1.2) #default is .75 but we needed to make it a little bit faster than that
        self.table = [None] * loadFactor #make all table indexes None since we're working with chaining
        self.size = loadFactor
    
    '''
    'hash' funtion takes the ascii value of a string and returns that value % table.size
    this will gurantee less collisons. 
    '''
    def hash(self, word):
        index = 0 #index where word should be inserted
        for i in range(len(word)): #get the ascii value of each letter in the word
            #use the ord function to get the ascii value of each letter
            asciiValueOfWord = ord(word[i])
            index += (asciiValueOfWord ** i)
            
        return index % self.size
    
    '''
    'insertWord' method simply checks if the current index is not empty,
    if it's not empty then that means comparasions are being made
    if the index is empty then we simply inser the Node that contains the word.
    '''
    def insertWord(self, word):
        comparedTimes = 0
        index = self.hash(word) #calls the hash function that return the index
        
        #check if the table is not empty
        #if the table is not empty then
        #a comparison needs to be made.
        if self.table[index] != None: 
            comparedTimes += 1
            
        self.table[index] = HashNode(word, self.table[index])
        return comparedTimes
        
    '''
    'search' method takes a word as a parameter, it checks the correct location 
    of where the word should be found (you must call the hash function to check)
    if the word is found then return 1 if not then return false (0)
    '''
    def search(self, word):
        #call the hash function in order to check
        #the corresponding index where the word belongs
        index = self.hash(word) 
        holder = self.table[index] #hoder is the head of the list at the ceratin location
        
        while holder != None:
            if holder.word == word:
                return True
            holder = holder.next
        return False
    
    '''
    'loadFactor' method simply applies the formula stated in line 14 of this file 
    
    (number of entries)
    -------------------
      (size of table)
    '''
    def loadFactor(self, bucketsInTable):
        return bucketsInTable / self.size