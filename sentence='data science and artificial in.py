sentence='data science and artificial inteliigence'
unique=set(sentence)
vowels='aeiouAEIOU'
sets=set()
for i in unique:
    if i in vowels:
        sets.add(i)
print(sets)