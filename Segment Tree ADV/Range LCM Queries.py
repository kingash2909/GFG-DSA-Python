
#Function to find LCM of given range.
def getLCM(arr,n,st,li,rv):
    
    return frg(st,0,n-1,li,rv,0)
 
#recursive function to get LCM of given range of array indexes.      
def frg(st,ss,se,qs,qe,si):
    
    #if segment of this node is outside the given range, we return 1.
    if ss>qe or se<qs:
        return 1
    
    #if segment of this node is part of given range then we return st[si].
    if ss>=qs and se<=qe:
        return st[si]
    
    #if a part of this segment overlaps with the given range, we call
    #the function recursively for the children nodes.    
    mid=ss+(se-ss)//2
    a=frg(st,ss,mid,qs,qe,si*2+1)
    b=frg(st,mid+1,se,qs,qe,si*2+2)
    
    n=lcm(a,b)
    return n
 
#Function to update a value in input array and segment tree.   
def updateValue(arr,n,st,li,rv):
    
    #updating the value of nodes in segment tree.
    uv(st,li,rv,0,n-1,0)

#recursive function to update nodes which have given index in their range.    
def uv(st,li,rv,ss,se,si):
    
    #base cases
    if ss>li or se<li:
        return
    if ss==se:
        st[si]=rv
        return
    
    
    #if the input index is in range of this node then we update
    #the value of the node and its children.
    mid=ss+(se-ss)//2
    uv(st,li,rv,ss,mid,si*2+1)
    uv(st,li,rv,mid+1,se,si*2+2)
    
    st[si]=lcm(st[si*2+1],st[si*2+2])
