demo_str= 'Helloworld'
demo_str1 = "Haroon Baig"
demo_str2 = """Hi Im going to Mysore 
Tomorrow morning"""
demo_str3 = '''The place is famous for
1. Hertiage
2. Cleanliness
'''

x = "9845"

print(demo_str1)
print(len(demo_str1))
print("2nd letter",demo_str1[1]) #indexing
print("last letter",demo_str1[-1])#indexing
print(demo_str1*2) #repeatation
print(demo_str2 + demo_str3) #concatenation
print("first 4 letters from the string",demo_str1[:4])
print("reverese the string",demo_str1[::-1])#reversing
print("count number of o from the string",demo_str1.count('l'))#counting
print(demo_str1.upper(), demo_str1.lower())#uppercase & lower case
print(demo_str.isalpha()) #alphacheck
print("find the position of ll from the string : ", demo_str.find("ll"))#finding
