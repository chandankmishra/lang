class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def canAttendMeetings(intervals):
    """
    :type intervals: List[Interval]
    :rtype: bool
    """
    ilst = []
    for i in intervals:
        for s, e in ilst:
            print (s, e)
            if i.end > s and i.start < e:
                return False
        ilst.append((i.start, i.end))
    return True


lst = []
lst.append(Interval(0, 30))
lst.append(Interval(5, 10))
lst.append(Interval(10, 20))

print(canAttendMeetings(lst))
