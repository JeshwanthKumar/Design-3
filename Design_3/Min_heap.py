#Time Complexity: getMin() - O(1), insert - O(1), extractMin()- O(1)
#Space Complexity: O(n)

class MinHeap:
    def __init__(self):
        self.heap =[]   #Initializing the heap
        
    def getMin(self):
        return self.heap[0] #Return the first value in the heap
        
    def bubbleUp(self,index):   #Bubble up the minimum element to the top of the heap
        parentIndex = (index-1)//2  #Calculating the parent index by dividing the index-1 by 2
        
        if parentIndex < 0: #If the parentIndex is less than 0 then just return
            return 
        
        if self.heap[parentIndex] < self.heap[index]:   #If the element in the parentIndex is less than the element in the index the just return
            return
        self.heap[parentIndex], self.heap[index] = self.heap[index], self.heap[parentIndex] #Swap the elements in parentIndex and index
        self.bubbleUp(parentIndex)      #Recursively call the bubblUp method until the heap satisfies
        
            
    def bubbleDown(self, index):    #Bubble down the parent element to the last
        leftChild = 2*index+1   #Calculating the index of leftChild by multiplying the index wuth 2 and adding 1
        rightChild = 2*index+2  #Calculating the index of rightChild by multiplying the index wuth 2 and adding 2
        temp = index    #Assigning a variable temp to index
        
        #-----Checking the leftChild first and then the rightChild because it's a binary search tree-----#
        
        if leftChild < len(self.heap) and self.heap[temp] > self.heap[leftChild]:   #If the leftChild is less than length of the heap and the element in the temp index is less than the element in the leftChild, then change temp to leftChild
            temp = leftChild
            
            
        if rightChild < len(self.heap) and self.heap[temp] > self.heap[rightChild]: #If the rightChild is less than length of the heap and the element in the temp index is less than the element in the rightChild, then change temp to rightChild
            temp = rightChild
            
        if temp == index:   #If the temp is equal to index then return nothing
            return
        self.heap[temp], self.heap[index] = self.heap[index], self.heap[temp]   #Swap the elements in parentIndex and index
        self.bubbleDown(temp) #Recursively call the bubblDown method until the heap satisfies 
        
    def insert(self, key):  #Insert the value into the heap
        self.heap.append(key)   #Append the value to the heap
        self.bubbleUp(len(self.heap)-1) #Call bubbleUp method to do the bubble up and align the heap in the correct order
        
        
    def extractMin(self):   #Extract the minimum element in the heap and delete it
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]   #Swap the first and last element in the heap
        temp = self.heap.pop()  #Store the element that is popped out of the heap
        self.bubbleDown(0)  #Perform the bubbleDown method to do the bubble down and align the heap in the correct order
        return temp #Return the temp
        
    def size(self):
        return len(self.heap)   #Return the size of the heap
    
    
    
    
    
h = MinHeap()
h.insert(5);
h.insert(3);
h.insert(17);
h.insert(11);
h.insert(79);
h.insert(19);
h.insert(6);
h.insert(25);
h.insert(9);
print(h.heap)
print(h.getMin())
for i in range(len(h.heap)):
    print(h.extractMin())
    