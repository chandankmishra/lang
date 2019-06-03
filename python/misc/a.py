text = "aadya is a good girl"
i, n = 0, len(text)

start, end = -1, -1
for i in range(n):
    if (i == 0 or text[i-1] == ' ') and text[i] != ' ':
        start = i
    if (i == n-1 or text[i+1] == ' ') and text[i] != ' ':
        end = i
    if start != -1 and end != -1:
        print (text[start:end+1])
        start, end = -1, -1
 
