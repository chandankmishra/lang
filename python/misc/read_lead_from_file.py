import pickle
with open('outfile.txt', 'rb') as fp:
    leads = pickle.load(fp)

print (len(leads), type(leads))
error, total = 0, 0
for lead in leads:
    total += 1
    try:
        print (lead)
    except:
        error += 1
        pass

print ("total", total, "error", error)
