try:
    file=open("sample.txt","r")
    reading_file=file.read()
    file.close()
    print("Line1:This is a sample text file.")
    print("Line2:It contains multiple lines.")

except FileNotFoundError:
     print("Error:The file 'sample.txt' was not found.")

finally:
       print("Thank You")