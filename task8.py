file=open('output.txt','w')
file.write('hello, python!'"\n")
file.close()

file=open('output.txt','r')
reading_file=file.read()
print("Enter text to write to the file:",reading_file)
file.close()

file=open('output.txt','a')
appending_file=file.write('learning file handling in python.'"\n")
file.close()

file=open('output.txt','r')
reading_file=file.read()
print("Enter additional text to append:",reading_file)
file.close()