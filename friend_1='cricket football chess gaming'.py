friend_1='cricket football chess gaming'
friend_2='gaming coding badminton cricket'
friends_1=friend_1.split()
friends_2=friend_2.split()
unique1=set(friends_1)
unique2=set(friends_2)
print(unique1-unique2)