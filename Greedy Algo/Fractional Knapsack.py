
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        
        # code here
         # Calculate value per unit weight for each item
        value_per_unit_weight = [(item.value / item.weight, item.weight) for item in arr]

        # Sort items based on value per unit weight in non-increasing order
        value_per_unit_weight.sort(reverse=True)

        # Initialize total value of knapsack
        total_value = 0

        # Iterate through sorted items
        for value_per_unit, weight in value_per_unit_weight:
            # If knapsack can hold entire item, add its value to total value and reduce capacity
            if W >= weight:
                total_value += value_per_unit * weight
                W -= weight
            else:
                # Otherwise, add a fraction of the item to the knapsack and break loop
                total_value += value_per_unit * W
                break

        return total_value