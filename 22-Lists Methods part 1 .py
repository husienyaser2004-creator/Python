#---------------------------------
#---- Lists Methods part 1 --------
#---------------------------------

# Append()  :  add element to the end of the list

myFriends = ["Osama" , "Ahmed" , "Sayed"]
myoldFriends = ["Haytham" , "Samah" , "Ali"]
myFriends.append("Ali")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myoldFriends)

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])

# Extend()  :  add element to the end of the list but it adds each element separately
a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["one", "two"]
a.extend(b)
a.extend(c)
print(a)

# Remove()  :  remove element from the list
x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
print(x)
# Sort()  :  sort the list

y = [1, 2, 100, 120, -10, 17, 29]
y = ["A" , "Z" , "c"]
y.sort(reverse=True)
print(y)

# Reverse()  :  reverse the list

z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)

