from STACK import stack

def int2bin(num):
    s = stack()
    while num > 0:
        s.push(num%2)
        num = num//2
    bin = ""
    while not s.is_empty():
        bin+= str(s.pop())
    return bin
    
    
        
print(int2bin(11261126112611262611))