# Open the file document 
document = open("document.txt")

# Read each line the file content
count = 0
for _ in document:
    count = count + 1

print("Line count: ", count)

# Read the whole document 
w_document = document.read()

# Count the letters
print(len(w_document))

# The very 20 start of string
print(w_document[:4]+ " xxxx "*3)   