from STACK import stack

def is_match(top,paren):
    if top =="(" and paren ==")":
        return True
    elif top =='[' and paren ==']':
        return True

    elif top =='{' and paren =='}':
        return True
    else:
        return False

def valid_paren(s1):
    s = stack()
    index = 0
    is_balanced = True
    while( index  < len(s1) and is_balanced):
        paren = s1[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                t = is_match(top,paren)
                if t == False:
                    is_balanced = False
                else:
                    is_balanced = True
                
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


brac= "((()))"
a = valid_paren(brac)
print(a)
     
            








  
