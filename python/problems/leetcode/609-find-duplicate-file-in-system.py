
def findDuplicate(paths):
    """
    :type paths: List[str]
    :rtype: List[List[str]]
    """
    fdict = {}
    ret = []
    for path in paths:
        # print (path)
        files = path.split(' ')
        directory = files[0]
        for file in range(1, len(files)):
            fullfile = directory + "/" + files[file]
            fullfile = fullfile[:-1]
            # print (fullfile)
            fname, content = fullfile.split('(')
            if content not in fdict:
                fdict[content] = []
            fdict[content].append(fname)

    for key in fdict:
        if len(fdict[key]) > 1:
            ret.append(fdict[key])
    return (ret)


ilist = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print (findDuplicate(ilist))
