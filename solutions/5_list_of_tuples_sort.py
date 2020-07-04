"""
5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
"""

my_details = ('Anjal', 'Bam', 21)

people = [my_details,]


friend_detail1 = ('Harish', 'Chand', 21)
friend_detail2 = ('Rajesh', 'Gautam', 20)
friend_detail3 = ('Amit', 'Buyo', 20)
people.append(friend_detail1)
people.append(friend_detail2)
people.append(friend_detail3)

people.sort()
# print(people)
people.sort(key=lambda detail: detail[2])
print(people)
