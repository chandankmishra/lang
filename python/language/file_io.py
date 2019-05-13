'''
file = open("testfile.txt", "w+")
file.write("Hello World\n")
file.write("This is our new text file\n")
file.write("and this is another line.\n")
file.write("Why? Because we can.\n")
file.close()

file = open("testfile.txt", "r")
print(file.read())
print(file.name)
file.close()
'''

# context manager
with open("testfile.txt", "r") as f:
    pass

# 1 read the full content of the file
with open("testfile.txt", "r") as f:
    content = f.read()
    print (content)

# 2 read the file line by line
with open("testfile.txt", "r") as f:
    for line in f:
        print (line, end='')

# 3 f.readlines reads the full file and returns an array of all lines
with open("testfile.txt", "r") as f:
    print (f.readlines())
    f.seek(0)

# 4 f.readline will read one line
with open("testfile.txt", "r") as f:
    content = f.readline()
    while len(content) > 0:
        print (content)
        print (f.readline())


# 5 read the file data by size
with open("testfile.txt", "r") as f:
    size = 10
    f_content = f.read(size)
    print (f_content)
    while len(f_content) > 0:
        f_content = f.read(size)
        print (f_content, end='')

# 6 f.seek and f.tell
with open("testfile.txt", "r") as f:
    f_content = f.read(size)
    print (f_content)
    print (f.tell())
    f.seek(0)
    f_content = f.read(size)
    print (f_content)

# 7 seek can reset the position for writing
with open("test.txt", "w+") as f:
    f.write('Testing123\n')
    f.seek(0)
    f.write('Testing\n')

# 8 test write
with open("test.txt", "w+") as f:
    f.write('Testing file write\n')

# 9 copy the content from one file to other line by line
with open("test.txt", 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# 10 copy the content from one file to other chunk by chunk
with open("test.txt", 'r') as rf:
    with open('test_copy2.txt', 'w') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

# 11 to read and write the image file open the file in the binary format
# append b in the 'r' 'w' to 'rb', 'wb'
