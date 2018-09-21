# Python script by Suprith Gangawar for Humanitec assignment, test case 2.

# Importing requests module in python. It is be used for API testing in python scripts.
import requests

URI = "https://jsonplaceholder.typicode.com/"


# Making a get request on the given site to later capture the response.
response = requests.get(URI + "users")
print("Response Code is: {}".format(response.status_code))

# Check if status code is OK or not and print likewise.
if 'assert response.status_code == 200':
    pass
else:
    print "Response is not 200. Request not successful"
#print("Response Time: {}".format(response.elapsed.total_seconds()))

# Verify if response time is less than 200 ms or not and print likewise.
var1 = response.elapsed.total_seconds()
if var1 <= 0.200:
    print "Response time is less than 200 ms"
else:
    print "Response time is more than 200 ms"

# Import json data into a variable and check for companies names ending with 'Group'
json_content = response.json()
for i in json_content:
    name = i['company']['name']
    if name.endswith("Group"):
        print("Company Name: {}".format(name))
