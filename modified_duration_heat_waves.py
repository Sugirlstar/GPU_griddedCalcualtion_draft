import numpy as np

#input: 
# pos_hw - the positions of HW days
# min_duration - a numeric number
def duration_heatwaves(pos_hw, min_duration):

    pos_hw_arr = np.array(pos_hw)
    pos_hw.insert(0,pos_hw[0]-21) #to keep the first diff>20

    d = np.diff(pos_hw)

    startD = np.where(d !=  1)[0]
    endD = np.append((startD-1)[1:],len(pos_hw)-2)
    durD = endD-startD+1

    # Condition1: the interval > 20days
    condition1 = np.where(d[d!=1]>20)
    # Condition2: last for at least min_duration days
    condition2 = np.where(durD>=min_duration)
    finalIndex = np.intersect1d(condition1,condition2)

    pos_day1_hw = pos_hw_arr[startD[finalIndex]]
    duration_hw = durD[finalIndex]

    return duration_hw, pos_day1_hw


# An example to test the function ------------

x = [2,3,4,5,6,7, 28,29,30,31,32, 34,35,36, 50,51,52,53,54, 90,91,92,93,94,95,96, 99]
# for a min_duration=5, the results should be:
# duration_hw: 6, 5, 7
# pos_day1_hw: 2, 28, 90

print(duration_heatwaves(x,5))
