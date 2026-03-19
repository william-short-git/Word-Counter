#Plan:
# user inputs a file name
# program returns the number of words in the file

print("Enter your file name: ")
filename = input()

with open(filename, 'r') as f:
    data = f.read()
    words = data.split()
    print(len(words))
    f.close()