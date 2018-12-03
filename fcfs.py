
burst = []
arrival=[]
index=[]
file = open("input.txt", "r")
for i in file:
 a=i.split()
 index.append(int(a[0]))
 arrival.append(int(a[1]))
 burst.append(int(a[2])) 
finishtime=arrival[0]
starttime=arrival[0]
waitingtime=0
turnaround=0
wsum=0.0
tsum=0.0
size=len(arrival)
print("waiting time is ")
for i in range (size):	
 finishtime=finishtime+burst[i]
 waitingtime=starttime-arrival[i]
 print(waitingtime ,"\n")
 wsum=wsum+waitingtime
 turnaround=finishtime-arrival[i]
 tsum=tsum+turnaround
 starttime=starttime+burst[i]
print("average waiting time is ",wsum/size)
print("average turnaround time is ",tsum/size)
