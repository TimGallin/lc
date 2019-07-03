'''
Facebook interview question
How many ways to decode this message?
The message is a string consisted of numbers.These numbers are mapped to legiters.
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

def num_of_way_bottom_to_top(data):
    #add some pre-check here(if char c <1 || c>26 then return 0)

    length = len(data)
    memo = [0]*( length + 1)

    index = 0

    for index in range(length) :
        if int(data[index : index + 2]) > 26 :
            break

    check_index = index
    for check_index in range(length) :
        v = int(data[check_index]) 
        if  v < 1 :
            return 0
    
    memo[index + 1] = 1
    memo[index] = 1

    index -= 1

    while index >=0 :
        v=0
        if int(data[index : index + 2]) <= 26 : 
            v = memo[index +1] + memo[index +2]
        else:
            v =memo[index + 1]
        memo[index] = v
        index -= 1

    return memo[0]


if __name__ == "__main__":
    print(num_of_way_bottom_to_top('1212121211122231'))
    print(num_of_way_bottom_to_top('1212121211122221112121212121212121212121212121212'))
    print(num_of_ways('123456789'))
    print(num_of_ways('2345'))
    print(num_of_ways('345'))
    print(num_of_ways('30'))
    print(num_of_ways('123'))
    print(num_of_ways('1'))

    print('bottom_to_top')

    print(num_of_way_bottom_to_top('1212121211122221112121212121212121212121212121212'))
    print(num_of_way_bottom_to_top('123456789'))
    print(num_of_way_bottom_to_top('2345'))
    print(num_of_way_bottom_to_top('345'))
    print(num_of_way_bottom_to_top('30'))
    print(num_of_way_bottom_to_top('123'))
    print(num_of_way_bottom_to_top('1'))
