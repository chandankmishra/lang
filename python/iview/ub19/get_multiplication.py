# Enter your code here. Read input from STDIN. Print output to STDOUT


# N {digits} * M {digits}= 
# N "12345" M "425"

'''
  425 (M)
12345
------

'''
def get_multiplication(N, M):
    nlen, mlen = len(N), len(M)
    if nlen == 0 or mlen == 0:
        return "0"
    
    res = [0] * (nlen+mlen)
    
    carry = 0
    for i in range(nlen - 1, -1, -1):
        for j in range(mlen - 1, -1, -1):
            prod = res[i+j+1] + carry + int(N[i]) * int(M[j])
            digit = prod % 10
            carry = prod // 10
            res[i+j+1] = digit
            
        if carry:
            prod = res[i+j] + carry
            res[i+j] = prod % 10
            carry = prod // 10
 
    if carry:
        prod = res[i+j] + carry
        res[i+j] = prod % 10
        carry = prod // 10
    res = list(map(str, res))

    ret = ''.join(res).lstrip("0")
    return "0" if len(ret) == 0 else ret
    

def testcases(input, output):
    output = str(output)
    if input != output:
        raise ValueError()


print (get_multiplication("99", "99"), 99 * 99)
print (get_multiplication("0", "123"), 0 * 123)
print (get_multiplication("42", "123"), 42 * 123)
print (get_multiplication("123", "42"), 123 * 42)
print (get_multiplication("12345", "425"), 12345 * 425)
#  42
# 123

# 126
# 84
'''
try:
    testcases(get_multiplication("12345", "425"), 12345 * 425)
    print("TEST PASSED")
except:
    print ("TEST FAILED") 
'''
# print(get_multiplication("12", "2") == 12 * 2) # 24


'''
try:
    testcases(get_multiplication("12", "2"), 12 * 2)
    print("TEST PASSED")
except:
    print ("TEST FAILED")
    
try:
    testcases(get_multiplication("12", "2"), 25)
    print("TEST PASSED")
except:
    print ("TEST FAILED")
'''
    
    
    
            
    
    
    
    
        
    
