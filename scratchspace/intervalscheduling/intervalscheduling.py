
# (start time, finish time)
intervals = [(0, 7), (1,4), (3, 5), (3,8), (4,7), (5,9), (6,10), (7,8), (8,11)]



def earliestFinishTimeFirst(intervals):
    # sort finish time in ascending order (earliest to latest)
    intervals.sort(key = lambda x : x[1])

    schedule = []
    for slot in intervals:
        if schedule == []:
            schedule.append(slot)
        else:
            # check if slot starts after last finish time
            if slot[0] >= schedule[-1][1]:
                schedule.append(slot)
    print(schedule)

if __name__ == "__main__":
    earliestFinishTimeFirst(intervals)
