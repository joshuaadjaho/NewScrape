import pandas as pd

#a_file = open("data_description.txt")
#lines_to_read = [x for index, x in enumerate(range(20))]

#for position, line in enumerate(a_file):
#    if position in lines_to_read:
#       print(line)

#a_file.close()

df1 = pd.read_csv('test.csv')
df2 = pd.read_csv('data_description.txt', delimiter='/t', engine ='python')

# THIS IS TO EASILY SELECT DEFINITIONS FOR ACRONYMS AND TRY TO PRINT ALL ITS RELATED INFO.
desired_code = input('Enter house code: ')
next_code = input('Next house code:')

df3 = open('data_description.txt', 'r')

a=1 
b=1
for line in df3:
     if desired_code in line:
         print(line)
         print(a)
     if next_code in line:
         print(line)
         print(b)
         break
     else: 
         a=a+1
         b=b+1


df3.close()