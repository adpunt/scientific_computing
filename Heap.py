# Priority Queue implemented using a binary minheap data structure

# Each element in the heap is an Item.  That Item contains the value (label)
# associated with a vertex as well as the number of that vertex.
# The minheap is based on the values, so that the Item with smallest value
# is a the top of the heap.

# We also overload the < (lt) and > (gt) operators so that Items can be compared 
# based on their values.

class Item:
    def __init__(self, value, vertex, predecessor = None):
        self.value = value
        self.vertex = vertex
        
        # predecessor is the vertex that gave this vertex its value/label.
        self.predecessor = predecessor 

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return "<value: " + str(self.value) + " vertex: " + str(self.vertex) + ">"

class Heap:
    def __init__(self, length):
        self.length = length    # initial length of array representing heap      
        self.elements = 0       # number of elements currently in heap
        self.array = [None] * self.length  
        self.index = [None] * self.length

    def insert(self, item):
        """ insert a new Item into the heap. """
        self.elements += 1   
        if self.elements >= self.length:  
            self.extend()
        self.array[self.elements] = item  
        self.index[item.vertex] = self.elements  # set the index in the heap
        currentIndex = self.elements             
        while currentIndex > 1 and self.array[int(currentIndex/2)] > \
                self.array[currentIndex]:
            # swap child and parent
            self.swap(currentIndex, int(currentIndex/2))
            currentIndex = int(currentIndex/2)
        
    def extend(self):
        """ extend the arrays when they fill. """
        newArray = [None] * self.length*2
        newIndex = [None] * self.length*2
        for i in range(self.length):
            newArray[i] = self.array[i]
            newIndex[i] = self.index[i]
        self.array=newArray
        self.index = newIndex
        self.length *= 2

    def deleteMin(self):
        """ delete and return the Item with smallest value from the heap. """
        if self.elements == 0: return None
        else:
            output = self.array[1]
            self.swap(1, self.elements)
            self.elements -= 1
            current = 1
            while current < self.elements:
                leftChildIndex = current * 2
                rightChildIndex = current * 2 + 1
                if leftChildIndex > self.elements:
                    break
                elif leftChildIndex <= self.elements and rightChildIndex > self.elements:
                    if self.array[current] > self.array[leftChildIndex]:
                        self.swap(current, leftChildIndex)
                    break
                elif self.array[current] > self.array[leftChildIndex] or \
                     self.array[current] > self.array[rightChildIndex]:
                    if self.array[leftChildIndex] < self.array[rightChildIndex]:
                        self.swap(current, leftChildIndex)
                        current = leftChildIndex
                    else:
                        self.swap(current, rightChildIndex)
                        current = rightChildIndex
                else: 
                    break
            return output

    def decreaseKey(self, vertex, newValue, predecessor):
        """ Takes a vertex, newValue, and a predecessor vertex as input.
            Offers the vertex the newValue.  The vertex takes this new value
            if it is better than its current value, in which case it also
            records that it received this value from the given predecessor."""
        currentIndex = self.index[vertex]
        if newValue < self.array[currentIndex].value: 
            self.array[currentIndex] = Item(newValue, self.array[currentIndex].vertex, predecessor)
            parent = currentIndex // 2
            while (parent > 0 and self.array[parent] > self.array[currentIndex] and currentIndex > 1):
                self.swap(currentIndex, parent)
                currentIndex = parent
                parent = currentIndex // 2

    def swap(self, index1, index2):
        """ Swap the Items at index1 and index2 in the heap.  
        Since index1 and index2 are the indices of Items in the heap, they each
        correspond to vertices in the heap; call them vertex1 and vertex2.  When
        this swap is performed, we also update self.index so that we can find
        these Items from the self.index table. """
        temp1 = self.array[index1]
        temp2 = self.array[index2]
        self.array[index1] = temp2
        self.array[index2] = temp1

        tempIndex1 = self.index[temp1.vertex]
        tempIndex2 = self.index[temp2.vertex]
        self.index[temp1.vertex] = tempIndex2
        self.index[temp2.vertex] = tempIndex1
 

    def __repr__(self):
        """ Return a string representation of the heap. """
        output = ""
        for i in range(1, self.elements+1):
            item = self.array[i]
            output = output + str(item) + "\n"
        return output
            
