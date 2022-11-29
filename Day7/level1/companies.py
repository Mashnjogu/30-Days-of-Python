it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
kenya_it_companies = {"Chamasoft", "Twiga", "NCBA"}

print("The length of the IT Companies is ", len(it_companies))
#add Twitter
it_companies.add("Twitter")
print(it_companies)
#add multiple it_companies
it_companies.update(kenya_it_companies)
print(it_companies)
#remove one of the companies from the set
it_companies.remove("Twitter")
print(it_companies)
#What is the difference between remove and discard
#Remove() is used to remove an item from the set and if the item is not found it raises errors
#However, discard() does not raise any errors