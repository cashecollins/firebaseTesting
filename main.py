
from firebase import firebase
from firebase_token_generator import create_token
from pprint import pprint


""" Creates the Token necesarry for Authorization """
# "private_key" in the credentials JSON
private_key = '-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCPxdH3NfDAY/aV\n14gZIBLv1fZfz/WfFnRUSxCSgVR6lp0t1+oOk70GDn0JoHZIp15a6Ht5JBSG8LRa\nQNvBeC7CbBFyeGGLBqW1oUqcf9wLmh7pWFNvzNGjwIQfp71QKm5lzVV1UWBZBUKL\n/josBB1yydAMSF9vBN7abOiFvm6S3uVx4rKy4Dkw2p6+YnXclkB7a3GjSLGJiEZV\nCjSlQdO5iCmkRZV1Reztv1aSJFRneL2Ufdy61RgWm7fiHij2ySdOs91C2S0Dwarg\nxWf/oM8dG3atc/t+erURVvOVNRu4QH2JFA7cy4BBJKoINxmH5AANVZNFDXQN5YSE\nudiUDanhAgMBAAECggEAWB1fj+lpQiCB8lgEO5HiyUcTFqm32ebDKR5Qa9oD0pYY\ngw4/juuQ//NFQu8rT1/0fjbZ5ebtBb7kaiQyCyMDVXkyQDvzXGeYi/bsaXobfKja\npRzTFkQrf/bvgw8lAcrfmlj8NUjIigalQHNxZ6Sl/8IcVkrM4pfTlX8GC2IpFq3F\n9nOkg2N3UV/Da75CppLjcYpz2DrhFrJ9KHLmLc9VYnE4PncrqxT425RUwjLQq4UE\nVNLdOcOeNEoODEJJnZV4hwpDjbfCIfhWpOX0bTQ7JF/66nLnMkrmeSdV10AfK1bY\nI+juh7VTD5xSBBZWXTFQAYM1OnqpXf08539R8GQVmQKBgQDJUT9S/uVltHplB2ly\ne+OSDZzJpteUZMB/1tIR8pO+XAAQK8MWpTjl4KF9ApRR5TbyK0evp65nR+1XHKVL\nHc6h2RKo1JPp3f19Cv1x4vb7xYWV/N8kMU8tVDXcXeGsUrv+g4zloCWKTRo7EWsr\nsII7TZ3IbP0JTKQ/gIlHZENt9wKBgQC20ynwVnrdwTDJ1iq5cHGOaxE5uCapkYQN\nCtHFt1K0YwjXQGaXUuIOtW85pSIjE1VwVX86uRMjBZ6YTvkT5WZswJpk4fEu8fJE\nxaBv2iUTNsevZN1jFBnExYSgXwVHrhYy52MSPK/84bokUH7lPXMy7fgsWTsvPAs9\n35DcwNoQ5wKBgQC75xvF6ahPv56mAb8IXl5QimgXR6TcGxYZvHaizdncyZ49ebtD\nvb9XwMy6E9hAgENC0ea9KzN7rwT2VARsEkw1gJkMAC53EP5y4fkhfYiuAvTmw/m6\nnFOcqYcEQpRK9YYGzt6JzWp8pe6fx2hShRNpKs7kreWX8nMz2lNH0WumjQKBgGAF\ntnBBq5SO5EYOEzCEa1AG0exD2SKUiAullBnJOEn//eO4MmnmIU7iYkGfhrdvbx9p\n+EHqdK+fQvXx/IZDpTEXU8AKn3ctojYWqjY1F+XojqaDTne8VfBwYUEtxwMn3wbr\nWrB4aWJjWDW8hXl3derY69C3KQuc+LaNlnMrYx0fAoGAVaFu4ODKIjGUOyJq3Cby\nIGht8suKIPw7UtO1vBG/UkSMAyCDIBNoGtJPp9oeu6g9DwWGbDA+rHh5o58l1Zod\nUSBR2Mqu68+Ihuj31KGzdDGTtTwFef3yOlBe7l7uKC4J2omTET/DSyJzRkVhfdHO\nnHWe69Hdh9YwV4sgcvlQ41g=\n-----END PRIVATE KEY-----\n'
# "client_email" in the credentials JSON
service_account_email = "counter@project--4674828252354873374.iam.gserviceaccount.com"
auth_payload = {"auth_data": "foo", "other_auth_data": "bar"}
token = create_token(service_account_email, private_key, "user1", auth_payload)

"""Access the firebase database"""
# FIREBASE -> PYTHON
fbs = firebase.FirebaseApplication('https://project-4674828252354873374.firebaseio.com/', None)


authentication = firebase.FirebaseAuthentication('nU9t12pCYNaGUIP7EKbEy21b0xDkKmYoB8VE1vs5', 'cashe@vssl.com', extra={'id': 123})
fbs.authentication = authentication
print authentication.extra

#AUTHENTICATIONS
user = authentication.get_user()
user.firebase_auth_token = token
#print user.firebase_auth_token

previous_count = 0
while True:
    reg_users = fbs.get('/Users', None)
    #pprint(reg_users)

    count = 0
    for i in reg_users:
        count += 1;

    if count == previous_count:
        x = 0
    else:
        print count
        previous_count = count

