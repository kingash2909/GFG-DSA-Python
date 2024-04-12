import heapq


class Solution:
    def kthLargest(self, k, arr, n):
        # code here 
        result = []
        # Initialize a min-heap to store the K largest elements.
        min_heap = []
        
        for num in arr:
            # If the heap has less than K elements, just push the current element.
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                # If the current element is greater than the root of the heap, replace the root with the current element.
                if num > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
            # If the heap has less than K elements, append -1 to the result.
            # Otherwise, append the root of the heap.
            result.append(min_heap[0] if len(min_heap) == k else -1)
        
        return result