
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        # Combine the start and end times into tuples
        meetings = [(start[i], end[i]) for i in range(n)]
        
        # Sort the meetings by their end times
        meetings.sort(key=lambda x: x[1])
        
        # Initialize variables to keep track of the current meeting and count
        current_end = -1
        count = 0
        
        # Iterate through the sorted meetings
        for meeting in meetings:
            # If the start time of the current meeting is greater than or equal to
            # the end time of the previous meeting, schedule this meeting
            if meeting[0] > current_end:
                count += 1
                current_end = meeting[1]
        
        return count
