def count_and_say(n):
    res = "1"
    for _ in range(n - 1):
        n = len(res)
        result = []
        count = 0
        for i in range(n):
            if i == 0 or res[i] == res[i - 1]:
                count += 1
            else:
                result.append(str(count) + res[i - 1])
                count = 1
        result.append(str(count) + res[n - 1])
        res = ''.join(result)
    return res


def testcase(actual, expected):
    if actual != expected:
        print (f"FAILED: expected {expected}, got {actual}")
    else:
        print ("SUCCESS")


if __name__ == "__main__":
    testcase(count_and_say(1), "1")
    testcase(count_and_say(2), "11")
    testcase(count_and_say(3), "21")
    testcase(count_and_say(4), "1211")
    testcase(count_and_say(5), "111221")
