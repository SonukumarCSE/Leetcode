class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        m_interval = []
        intervals.sort()
        first = intervals[0][0]
        second = intervals[0][1]
        for i in range(1,len(intervals)):
            if second >= intervals[i][0]:
                second = max(intervals[i][1],second)
            else:
                m_interval.append([first,second])
                first = intervals[i][0]
                second = intervals[i][1]
        m_interval.append([first,second])
        return m_interval