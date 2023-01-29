#TIME COMPLEXITY ==> O(nlogn) ==> the use of python sort() has a time complexity of O(nlogn) and the the rest of the program has a worst case t.c of O(n).
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i=1
        intervals.sort()
        ans=[intervals[0]]                                    #store the first element of intervals
        while(i < len(intervals)):
            if (intervals[i][0] <= ans[-1][1]):                #compare the the last element of ans and the each iteration of the list intervals
                ans[-1][1]=max(intervals[i][1],ans[-1][1])
                i+=1
            else:
                ans.append(intervals[i])
                i+=1
        return ans
            
