# There is a dangerous criminal 🥷 being escorted by a group of police 👮👮👮 to another prison.
# He is escorted in a specific coach of a train  (a confidential matter), thinking that 
# his criminal members might plot his escape.
# Unfortunately the criminal members come to know the specific coach the criminal would 
# be placed, and this comes to the knowledge of the Head of the Police.
# He, in the last moment, decides to change the order of the coaches manually.
# The coaches are in an order that only adjacent coaches can be swapped.
# NOTE: Your task is to find the minimum number of such swaps needed 
#       to bring the coaches into a desired order (i.e. the order the Head wishes it to be)
# INPUT: N integer -- read as `int`
#        S arr [] -- 20 40 50 60 80 -- read as `str` in a single line, not as `int`
#        X arr [] -- 50 40 60 80 20 -- read as `str` in a single line, not as `int`
# S represents the first order, X represents the order to which coaches are to be changed
# OUTPUT: `int` -- minimum number of moves needed to change S to X

# function min_mov()
def min_mov(n,s:list,x:list):
    x_dict={}
    for i in range(n):
        x_dict[x[i]]=i
    for i in range(n):
        s[i]=x_dict[s[i]]
    return merge_sort(n,s)

# function merge_sort()
def merge_sort(n:int,s:list):
    i,j=0,1
    mode=1
    moves=0
    while(s!=list(range(n))):
        if(s[i]>s[j]):
            s[i],s[j]=s[j],s[i]
            moves+=1
        i+=2
        j+=2
        if(j>=n):
            if(mode==1):
                i,j=1,2
                mode=2
            elif(mode==2):
                i,j=0,1
                mode=1
    return moves

# Function to safely convert comma-separated string to list of integers
def parse_int_list(input_str):
    try:
        # Remove extra spaces, split by comma, and convert to integers
        numbers = list(map(int, input_str.strip().split(' ')))
        return numbers
    except ValueError:
        # Handle case where conversion to int fails
        print("Error: Please enter only integers separated by commas.")
        return None


# main program
N=int(input())
S = input()
S = parse_int_list(S)
X = input()
X = parse_int_list(X)
min_=min_mov(N,S,X)
print(min_)
