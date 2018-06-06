"""
Implement a UNIX TAIL command
"""
def tail(file_name, n):
    f = open(file_name, 'rb')
    f.seek(0, 2)
    file_size = f.tell()
    newline_cnt = 0
    print ("file size: ", file_size, " # of line:", n)

    last_n_lines = ""
    for i in range(1,file_size):
       f.seek(-i, 2)
       c = f.read(1).decode('utf-8')
       if c == '\n': newline_cnt += 1
       if (newline_cnt >= n): break
       last_n_lines += c
    f.close()
    return last_n_lines[::-1]

print (tail("epi_7_13_tail.py", 10))
