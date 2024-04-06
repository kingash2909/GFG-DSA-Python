
class Solution:
    def compareCLL(self,head1,head2):
        #code here
         # Function to count the number of nodes in a circular linked list
        def countNodes(head):
            if not head:
                return 0
            count = 1
            current = head.next
            while current != head:
                count += 1
                current = current.next
            return count

        # Count the number of nodes in both lists
        n1 = countNodes(head1)
        n2 = countNodes(head2)

        # If the number of nodes is different, return False
        if n1 != n2:
            return False

        # Traverse both lists simultaneously
        current1 = head1
        current2 = head2
        while True:
            # If data of current nodes are different, return False
            if current1.data != current2.data:
                return False

            # Move to the next nodes
            current1 = current1.next
            current2 = current2.next

            # If both nodes reach the heads again, break the loop
            if current1 == head1 and current2 == head2:
                break

        # If loop completes without returning False, return True
        return True