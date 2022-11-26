import statistics

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

#find the min and max
minAge = min(ages)
maxAge = max(ages)
print("The minimum age is: ", minAge)
print("The maximum age is: ", maxAge)

# Add the min age and the max age again to the list
ages.append(minAge)
ages.append(maxAge)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
medianAge = statistics.median(ages)
print("The median age is :", medianAge)

#average age
average = sum(ages) / len(ages)
print("The average age is: ", average)

# Find the range of the ages (max minus min)
range = maxAge - minAge
print("The range of the ages is: ", range)

# Compare the value of (min - average) and (max - average), use abs() method
valueA = abs(minAge - average)
valueB = abs(maxAge - average)

if(valueA > valueB):
    print("Min - Average is greater")
else: print("Max - Average is greater")



