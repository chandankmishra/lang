Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.

Fixed number of VMs = v
Number of test cases = n

10 8 6 4

10  8
4   6 
-----


testList = [[test1, time1], [test2, time2]....]
def runTests(testList, vmList):
 	testdone = False
	descresing = 1
	while True:
		if descresing:
			testList.sort(lambda x: x[1])
		else:
			testList.sort(lambda x: -x[1])
		nvm = len(vmList)
		for index in range(nvm):
			if len(testList) == 0:
				testdone = True
				break
			test_name, test_time = testList.pop(0)
			# check if the VM is alive or not
			runTest(vmList[index], test_name)
		if testdone is True:
			break	
		descresing ^= 1

def runTest(targetVM, test): ...

