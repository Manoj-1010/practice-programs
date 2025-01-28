'''
A washing machine works on the principle of Fuzzy System, the weight of clothes put 
inside it for washing is uncertain but based on weight measured by sensors and the water 
level chosen, it decides total time needed. 
For low level water, the time estimate is 25 minutes, where approximately weight is 
between 2000 grams or any nonzero positive number below that.
For medium level water, the time estimate is 35 minutes, where approximately weight is 
between 2001 grams and 4000 grams.
For high level water, the time estimate is 45 minutes, where approximately weight is 
above 4000 grams. Assume the capacity of machine is maximum 7000 grams. 
When the weight is zero, time needed is 
0
minutes. 
If the weight exceeds maximum weight limit, then, print “OVERLOADED”, and for all 
negative weights, the output is “INVALID INPUT”.

Sample Input-1: 2000, L
Sample Output-1: Time Estimated: 25 minutes

Input should be in the form of integer value. 
Output must have the following format: 
    Time Estimated: NN Minutes
'''

def time_estimator(load, water_level):
    # Checking for valid loads by eliminating negative weights, and weights more than 7000, and handling zero load condition
    if load == 0: return "Time Estimated: 0 minutes"
    elif load < 0: return "INVALID INPUT"
    elif load > 7000: return "OVERLOADED"
    else:
        # Based on the water level and load conditions, the respective estimated times are displayed
        if (water_level == 'L') and (load <= 2000): return "Time Estimated: 25 minutes"
        elif (water_level == 'M') and (load <= 4000): return "Time Estimated: 35 minutes"
        else: return "Time Estimated: 45 minutes"

if __name__ == "__main__":
    load, water_level = input().split()
    load = int(load)

    print(time_estimator(load, water_level))
