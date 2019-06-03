from marketorestpython.client import MarketoClient
munchkin_id = "473-EOD-147"  # fill in Munchkin ID, typical format 000-AAA-000
client_id = "cc3b4926-4e51-4948-b7d3-3b9e49fd82bb"  # enter Client ID from Admin > LaunchPoint > View Details
client_secret = "1DY40K34m3RM0sHJ8qNFfcO9mMYsXSm9"  # enter Client ID and Secret from Admin > LaunchPoint > View Details
mc = MarketoClient(munchkin_id, client_id, client_secret)

# Get Lead by Id
lead = mc.execute(method='get_lead_by_id', id=1258528, fields=['firstName', 'middleName', 'lastName', 'department'])
print (lead)
lead = mc.execute(method='get_lead_by_id', id=1258528)
print (lead)
