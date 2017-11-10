def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    vmov = 0
    hmov = 0
    for chr in moves:
        if chr is 'L':
            hmov = hmov - 1
        elif chr is 'R':
            hmov = hmov + 1
        elif chr is 'U':
            vmov = vmov - 1
        elif chr is 'D':
            vmov = vmov + 1
        else:
            return False
        print (vmov, hmov, (vmov + hmov))
    return True if hmov is 0 and vmov is 0 else False


print ("true") if judgeCircle("LDRRLRUULR") else print("false")

# judgeCircle("LLUD")
