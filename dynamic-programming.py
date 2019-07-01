'''
Facebook interview question
How many ways to decode this message?
The message is a string consist of numbers.These numbers are mapped to legiter.
''->''
1->a 
...
z->26
For example:
Input: 12

12->1 2 ->ab
or
12->l
Output:2
'''

#data : input string
#k: decode from the index of (data.length - k)
def decode(data, k, memo) :
    if k == 0:
        #if k == 0,the data is a empty str.
        return 1

    s = len(data) - k
    #if the first character is '0',then this message cannot be decoded.
    if data[s] == '0': 
        return 0
    
    if memo[k] != -1:
        return memo[k]

    result = decode(data, k-1,memo)

    if k>=2 and int(data[s:s+2]) <= 26 :
        result += decode(data,k-2,memo)

    memo[k]=result  

    return result

def num_of_ways(data) :
    memo = [-1]*(len(data) + 1)

    return decode(data, len(data), memo)


if __name__ == "__main__":
    print(num_of_ways('12345'))
    print(num_of_ways('2345'))
    print(num_of_ways('345'))
    print(num_of_ways('30'))
    print(num_of_ways('123'))
    print(num_of_ways('12'))
