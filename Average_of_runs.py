
#Program to find Average runs scored by a batsman in four days

run1 = int(input('Enter the run scored for the first day'))
run2 = int(input('Enter the run scored for the second day'))
run3 = int(input('Enter the run scored for the third day'))
run4 = int(input('Enter the run scored for the fourth day'))
#computing
Total_runs = run1+run2+run3+run4
Avg_run = Total_runs/4

print('the Average runs scored by a batsman in four days = ', int(Avg_run))
