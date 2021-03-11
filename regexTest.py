import re

# string = "Congress/NNP july/NN"
# pattern = re.compile(r'(.*)/(.*)')

# matches = pattern.finditer(string)

# trainDict={}

# for match in matches:
#     #print(match.group(1))
#     #print(match.group(2))

#     if match:
#             key = match.group(1)
#             value = match.group(2)
#             trainDict[key]=value

#     print(trainDict)


pattern = r"(.*)/(.*)"
stringPar = "old/JJ ,/, will/MD join/VB "
res = stringPar.split()

trainDict={}

for i in res:
    match = re.search(pattern,i)
    if match:
        key = match.group(1)
        value = match.group(2)
        trainDict[key]=value
print(trainDict)



# matches=re.finditer(pattern,res)

# for matchNum, match in enumerate(matches, start=1):
#     if match:
#         key = match.group(1)
#         value = match.group(2)
#         trainDict[key]=value

# print(trainDict)

