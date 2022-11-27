first_tuple = ()
brother = ('John', 'Doe')
sisters = ('Jane', 'Doe')
siblings = brother + sisters
print(siblings)
len(siblings)
family_members = list(siblings)
family_members.append("Mother Doe")
family_members.append("Father Doe")
fam = tuple(family_members)
print(fam)
#unpack siblings from tuple
del fam
