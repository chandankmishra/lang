from marketorestpython.client import MarketoClient
munchkin_id = "473-EOD-147"  # fill in Munchkin ID, typical format 000-AAA-000
client_id = "cc3b4926-4e51-4948-b7d3-3b9e49fd82bb"  # enter Client ID from Admin > LaunchPoint > View Details
client_secret = "1DY40K34m3RM0sHJ8qNFfcO9mMYsXSm9"  # enter Client ID and Secret from Admin > LaunchPoint > View Details
mc = MarketoClient(munchkin_id, client_id, client_secret)

# #Get Multiple Leads by List Id #2681
leads1 = mc.execute(method='get_multiple_leads_by_list_id', listId='2681',
                    fields=['email', 'firstName', 'lastName', 'company', 'postalCode'], batchSize=None)

# Write leads into a file
import pickle
with open('outfile.txt', 'wb') as fp:
    pickle.dump(leads1, fp)

# with open('outfile.txt', 'rb') as fp:
#     leads = pickle.load(fp)


# #Get Multiple Leads by List Id Yield (Generator)
# for leads in mc.execute(method='get_multiple_leads_by_list_id_yield', listId='676',
#                 fields=['email','firstName','lastName'], batchSize=None):
#     print(len(leads)) vv vvvvvvvv
