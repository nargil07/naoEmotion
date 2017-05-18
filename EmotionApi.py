import httplib, urllib, base64
import jsonInterpreter
import PersonClass
headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '281f633d67934f50ae690175f0b271a9',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    f = open('./test/test.jpg', "rb")

    body = f.read()

    f.close()
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    people = jsonInterpreter.addPeople(data)
    print people
    mainPerson = people[0]
    print(mainPerson.getHumor());

    conn.close()
except Exception as e:
    print("[Errno {0}]".format(e))
