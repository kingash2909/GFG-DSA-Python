
'''
class node:
    def __init__(self):
        self.sm=None
        self.prefixsm=None
        self.suffixsm=None
        self.maxsm=None
        
'''
def updateu(tree,arr,index,low,high,idx,value):
    if low==high:
        tree[index].sm = value
        tree[index].prefixsm = value
        tree[index].suffixsm = value
        tree[index].maxsm = value
    else:
        mid = (low + high) // 2
        if idx <= mid:
            updateu(tree,arr, 2 * index + 1, low, mid, idx, value)
        else:
            updateu(tree,arr, 2 * index + 2, mid + 1, high, idx, value)
       
       
        tree[index].sm = tree[2 * index + 1].sm + tree[2 * index + 2].sm
        tree[index].prefixsm = max(tree[2 * index + 1].prefixsm, tree[2 * index + 1].sm + tree[2 * index + 2].prefixsm)
        tree[index].suffixsm = max(tree[2 * index + 2].suffixsm, tree[2 * index + 2].sm + tree[2 * index + 1].suffixsm)
        tree[index].maxsm = max(tree[index].prefixsm, max(tree[index].suffixsm, max(tree[2 * index + 1].maxsm, max(tree[2 * index + 2].maxsm, tree[2 * index + 1].suffixsm + tree[2 * index + 2].prefixsm))))

def queryu(tree,arr,index,low,high,l,r):
    result=node()
    if (r < low or high < l):
        return result
    if (l <= low and high <= r):
        return tree[index]
        
    mid = (low + high) // 2
    if (l > mid):
        return queryu(tree,arr, 2 * index + 2, mid + 1, high, l, r)
    if (r <= mid):
        return queryu(tree,arr, 2 * index + 1, low, mid, l, r)
    left = queryu(tree,arr, 2 * index + 1, low, mid, l, r)
    right = queryu(tree,arr, 2 * index + 2, mid + 1, high, l, r)
    result.sm = left.sm + right.sm
    result.prefixsm = max(left.prefixsm, left.sm + right.prefixsm)
    result.suffixsm = max(right.suffixsm, right.sm + left.suffixsm)
    result.maxsm = max(result.prefixsm,max(result.suffixsm,max(left.maxsm,max(right.maxsm,left.suffixsm + right.prefixsm))))
    return result

def update(tree,arr,arrSize,index,value):
    arr[index-1]=value
    updateu(tree,arr, 0, 0, arrSize-1, index-1, value)
    
def query(tree,arr,n,l,r):
    
    return queryu(tree,arr, 0, 0, n-1, l-1, r-1).maxsm
