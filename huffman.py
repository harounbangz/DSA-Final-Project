"""
Huffman Coding Implementation

Data Structures and Algorithms Project

This program:
- Creates a Huffman Tree
- Generates Huffman Codes
- Calculates encoded length
"""

import heapq



class Node:

    def __init__(self, frequency, symbol=None, left=None, right=None):

        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right


    # Required for priority queue comparison
    def __lt__(self, other):

        return self.frequency < other.frequency



def generate_codes(node, current_code="", codes={}):

    if node is None:
        return


    # Leaf node
    if node.symbol is not None:

        codes[node.symbol] = current_code

        return


    generate_codes(
        node.left,
        current_code + "0",
        codes
    )


    generate_codes(
        node.right,
        current_code + "1",
        codes
    )



# Symbol frequencies

frequencies = {

    "a": 2,
    "b": 4,
    "c": 8,
    "d": 16,
    "e": 16

}



# Create priority queue

heap = []


for symbol, frequency in frequencies.items():

    node = Node(
        frequency,
        symbol
    )

    heapq.heappush(
        heap,
        node
    )



# Build Huffman Tree

while len(heap) > 1:


    left = heapq.heappop(heap)

    right = heapq.heappop(heap)


    merged = Node(

        left.frequency + right.frequency,

        left=left,

        right=right

    )


    heapq.heappush(
        heap,
        merged
    )



# Root of Huffman Tree

root = heap[0]



# Generate Codes

codes = {}

generate_codes(
    root,
    "",
    codes
)



print("===== Huffman Coding =====")


print("\nGenerated Huffman Codes:\n")


for symbol, code in codes.items():

    print(
        symbol,
        ":",
        code
    )



# Calculate total encoded length

total_bits = 0


for symbol, frequency in frequencies.items():

    total_bits += (
        frequency *
        len(codes[symbol])
    )



print(
    "\nTotal Encoded Length:",
    total_bits,
    "bits"
)