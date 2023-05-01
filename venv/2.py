from keyboards.inline.choice_but_start_test import towers



from s3 import a

MyList = towers()
MyFile=open('output.txt', 'w')
for element in MyList:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()