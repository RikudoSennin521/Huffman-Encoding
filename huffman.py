#Code by Rohan Kumar 
#Date: 30.06.22

from collections import defaultdict
import heapq


#Test Cases incase of no input.
#s = 'qwertyuiopasdfghjklzxcv'
#f = [4, 4, 17, 28, 38, 41, 41, 48, 55, 56, 57, 66, 69, 71, 71, 72, 74, 75, 75, 77, 92, 96, 98]


#string containing characters appearing in text
s = ''

#list containing the corresponding characters' frequency
f = []

#taking input from input.txt
file = open('input.txt', 'r')
text = file.read()

#tracking frequency of characters 
dict = defaultdict(int)


for i in range(len(text)):
    dict[text[i]] += 1

for x in sorted(dict):
    s += x
    f.append(dict[x])


#this dictionary stores the huffman codes for the characters
h_code = defaultdict(str)

#Huffman Tree Node
class Node:
    def __init__(self,freq,symbol):
        self.freq = freq
        self.symbol = symbol
        self.left = None
        self.right = None
        self.huff = ''
    
    def __lt__(self,other):
        return self.freq < other.freq

#Prints the codes of the characters
def printnodes(node,val):
    newval = val + (node.huff)

    if node.left:
        printnodes(node.left,newval)
    if node.right:
        printnodes(node.right,newval)
    
    if not node.left and not node.right:
        #adding the codes to the huffman code dictionary before printing
        h_code[node.symbol] = newval
        print(node.symbol,': ',newval)



#Min Heap using heapq 
heap = []
for i in range(len(s)):
    newnode = Node(f[i],s[i])
    heapq.heappush(heap,newnode)





while(len(heap) > 1):
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)

    newnode = Node(n1.freq + n2.freq, n1.symbol + n2.symbol)
    if n1.freq <= n2.freq:
        newnode.left = n1
        n1.huff = '0'
        newnode.right = n2
        n2.huff = '1'
    else:
        newnode.left = n2
        n2.huff = '0'
        newnode.right = n1
        n1.huff = '1'
    heapq.heappush(heap,newnode)

print('The Huffman Codes are: ')
printnodes(heap[0],'')

encoded_string = ''
for i in range(len(text)):
    encoded_string += h_code[text[i]]

print('Encoded version of input text is :',encoded_string)




