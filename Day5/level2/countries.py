countries = ['China', 'Russia', 'USA', 'Finland','Sweden', 'Norway', 'Denmark']
middleIndex = (len(countries)-1)//2
print(middleIndex)
print(countries[middleIndex])
middleDivisor = len(countries)/2
middleDivisor2 = (len(countries)//2) + 1

if(len(countries)%2 == 0):
    firstHalf = countries[:middleDivisor]
    secondHalf = countries[middleDivisor:]
    print("The first half is: ", firstHalf)
    print("The second half is: ", secondHalf)
elif(len(countries)%2 != 0):
    firstHalf =  countries[:middleDivisor2]
    secondHalf = countries[middleDivisor2:]
    print("The middle country is: ", countries[middleDivisor2])
    print("The first half is: ", firstHalf)
    print("The second half is: ", secondHalf)