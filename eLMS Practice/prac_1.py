run = int(input("Runs: "))
over_bowled = int(input("Over bowled: "))
target = int(input("Target: "))
run_remain = target - run
over_remain = 20 - over_bowled
runrate = run / over_bowled
estimated_run = float(runrate) * float(over_remain)
if estimated_run > run_remain:
    print("Might win")
else:
    print("Might lose")
