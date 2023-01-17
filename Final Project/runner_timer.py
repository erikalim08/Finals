print("Poppleton Park Run")
print("------------------")
print("Start: ")
print("Press END to stop")
num_runners=[]
time_taken=[]
runner_data = []

while True:
    try:
        data= input('>')
        if data=='END' :
            break
        if data=='::':
            print("ERROR!")
            continue
        runner= data.split('::')[0]
        time= data.split('::')[1]
        runner_data.append(data)
        num_runners.append(runner)
        time_taken.append(time)
        datas = [num_runners,time_taken]
    except:
        print("Error! Carry on!")
        continue
time_taken = [int(i) for i in time_taken]
average= (sum(time_taken)/len(num_runners))
minute= int(average//60)
second= int(average%60)

min_time= int(min(time_taken))
max_time= int(max(time_taken))
runners = [[int(i) for i in x.split('::')] for x in runner_data]
print("Number of runners: ", len(num_runners))
print("Average time: ","{} minutes {} seconds".format(minute,second))
print("Fastest time: ","{} minutes {} seconds".format(max_time//60,max_time%60))
print("Slowest time: ","{} minutes {} seconds".format(min_time//60,min_time%60))

fastest_runner = min(runners, key=lambda item: item[1]) 
print("Best Runner: ", fastest_runner[0])