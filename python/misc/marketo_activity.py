from marketorestpython.client import MarketoClient
munchkin_id = "473-EOD-147"  # fill in Munchkin ID, typical format 000-AAA-000
client_id = "cc3b4926-4e51-4948-b7d3-3b9e49fd82bb"  # enter Client ID from Admin > LaunchPoint > View Details
client_secret = "1DY40K34m3RM0sHJ8qNFfcO9mMYsXSm9"  # enter Client ID and Secret from Admin > LaunchPoint > View Details
mc = MarketoClient(munchkin_id, client_id, client_secret)

activity_list = []
activities = mc.execute(method='get_activity_types')
for idx, activity in enumerate(activities):
    if idx == 9:
        break
    # print (idx + 1, activity['id'])
    activity_list.append(str(activity['id']))
# print (actvity_list)


# activities = mc.execute(method='get_lead_activities', activityTypeIds=['1', '6'], nextPageToken=None,
#                         sinceDatetime='2018-09-26',
#                         # untilDatetime='2018-09-30',
#                         batchSize=None, listId=None, leadIds=[1258528, 1258529, 1258530])

activities = mc.execute(method='get_lead_activities', activityTypeIds=activity_list, nextPageToken=None,
                        sinceDatetime='2018-09-26',
                        # untilDatetime='2018-09-30',
                        batchSize=None, listId=None, leadIds=[1258528, 1258529, 1258530])
print (activities)
for idx, activity in enumerate(activities):
    print (idx + 1, activity)


# for idx in [1257342, 1257343, 1257344, 1257347, 1257353]:
#     lead = mc.execute(method='get_lead_by_id', id=1258528)
#     print (lead)
