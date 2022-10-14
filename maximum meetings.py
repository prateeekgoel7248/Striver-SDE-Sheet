def maximumMeetings(start, end):
    intervals=[[start[i],end[i],i+1] for i in range(len(start))]
    intervals = sorted(intervals,key=lambda x:x[1])
    res=[intervals[0][2]]
    prev=0
    for cur in range(1,len(intervals)):
        if intervals[cur][0]>intervals[prev][1]:
            prev=cur
            res.append(intervals[cur][2])
    return res