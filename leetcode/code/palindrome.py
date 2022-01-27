
# collections.Counter()
# A counter is a container that stores elements as dictionary keys, 
# and their counts are stored as dictionary values.

from collections import Counter

def constructable(string, k):
    
    # get termination case knocked out from the get go
    if k > len(string):
        return False
    
    h = Counter(string)
    print(h)
    
    odd_count = 0
    for value in h.values():
        print(value)
        if value % 2:
            odd_count += 1
            
    if odd_count > k:
        return False
    else:
        return True


'''
The solution is based on the understanding that a 
string can be a palindrome only if it has at most 1 character whose frequency is odd. 

So if the number of characters having an odd frequency is greater than the number of palindromes 
we need to form, then naturally it's impossible to do so.
'''

if __name__ == "__main__":
    
    # Input: s = "annabelle", k = 2
    
    string = "annabelle"
    k = 2
    
    output = constructable(string, k)
    print(output)
    
    
    