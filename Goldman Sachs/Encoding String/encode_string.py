#Your task is to complete this function
#Function should return complete string
def encode(arr):
    # Code here
    s=""
    c=1
    for i in range(len(arr)-1):
        
        if arr[i]==arr[i+1]:
            c+=1
            
        else:
            s+=arr[i]+str(c)
            c=1
            
    return s+arr[len(arr)-1]+str(c)        
#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends