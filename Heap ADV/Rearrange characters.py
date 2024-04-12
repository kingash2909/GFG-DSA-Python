from collections import *
import heapq
class Solution :
      def rearrangeString(self, str):
        #code here
        count = Counter(str)
        maxheap = [[-cut,char]for char,cut in count.items()]
        heapq.heapify(maxheap)
        prev = None
        res = ''
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            cnt, cha = heapq.heappop(maxheap)
            res+=cha
            cnt+=1
            if prev :
                heapq.heappush(maxheap,prev)
                prev = None
            if cnt != 0:
                prev = [cnt,cha]
        return res
