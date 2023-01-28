# Python has the module called statistics and we can use this module to do all
# the statistical calculations. However, to learn how to make function and reuse function
# let us try to develop a program, which calculates the measure of central tendency of a sample
# (mean, median, mode) and measure of variability (range, variance, standard deviation).
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample.
# You can create a class called Statistics and create all the functions that do statistical calculations as
# methods for the Statistics class. Check the output below.
import collections
from statistics import median, mean

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
class Statistics:
    def __init__(self, ages):
        self.ages = ages

    def mean(self):
        return mean(self.ages)

    def median(self):
        return median(self.ages)

    def mode(self):
        data = collections.Counter(self.ages)
        data_list = dict(data)
        max_value = max(list(data_list.values()))
        print("The maximum value is: ", max_value)
        mode_value = [num for num, freq in data_list.items() if freq == max_value]
        if(len(mode_value) == len(self.ages)):
            print("No mode in the list")
        else:
            print("The mode of the list is: " + ','.join(map(str, mode_value)))
        return mode_value

data  = Statistics(ages)
print(data.mean())
print()
print(data.mode())
