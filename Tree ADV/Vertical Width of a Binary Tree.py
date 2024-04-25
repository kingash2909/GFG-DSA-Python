
#Function to find the vertical width of a Binary Tree.
def solve(root,level,ans):
    if(root):
        if(level not in ans):   ans[level]=level
        solve(root.left,level+1,ans)
        solve(root.right,level-1,ans)
def verticalWidth(root):
    ans={}
    solve(root,0,ans)
    return len(ans)