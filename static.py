
from firebase import firebase
from firebase_token_generator import create_token
from pprint import pprint

import sys
import fontv
import ldp



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

global cancel
global count
count = 0
cancel = False
reg_users = fbs.get('/Users', None)
pprint(reg_users)

for counter in reg_users:
    global count
    count += 1


def log_user(response):
    global count
    global cancel
    if len(response) != count:
        count = len(response)
        cancel = True
        print(count)


"""this is the tickers stuff"""
while True:
    cancel = False
    # the matrix is a representation of the led's that are lit on the 80x8 display
    #
    matrix = [[0 for i in xrange(80)] for i in xrange(8)]

    # function to read the matrix array and output the values to the display device
    #
    def showmatrix():
        for row in reversed(range(8)):
            for col in reversed(range(80)):
                ldp.colourshift(matrix[row][col])
            ldp.showrow(row)
    # end def

    #
    # Main
    #
    # initialise the display
    #
    ldp.init()
    displaywidth = 80
    totalwidth = 0
    #
    # assign the command line args for the text and colour
    #

    textinput = str(count)
    colour = 1


    # save the ascii values of the input characters into the inputarray
    # the font module uses the ascii value to index the font array
    inputarray = []
    for char in textinput:
        inputarray.append(ord(char))

    # dotarray is  8 X n
    # n is determined by the number of characters multiplyed by 8
    # n will be len(dotarray[0]) after filling dotarray from characters
    # in the inputarray
    #
    dotarray = [[] for i in xrange(8)]
    #
    # fill the dot array with the colour digits
    # this is the dot pattern that we want to show
    #
    for row in range(8):
        for ascii in inputarray:
            # get the width of the character from the first element of the font variable
            width = fontv.array[ascii][0]
            binary = '{0:{fill}{align}{width}{base}}'.format(fontv.array[ascii][row + 1], base='b', fill='0', align='>',
                                                             width=width)
            for digit in range(width):
                if binary[digit] == '0':
                    dotarray[row].append(0)
                else:
                    dotarray[row].append(colour)

    totalwidth = len(dotarray[0])
    if totalwidth > displaywidth:
        print 'Message is Larger than the Display'
        sys.exit()

    offset = int((displaywidth - totalwidth) / 2)

    # Fill the matrix initially with offset spaces to centre align the message
    #
    for col in range(offset):
        for row in range(8):
            matrix[row][col] = 0
    # now fill the rest of the matrix with the dotarray
    for col in range(totalwidth):
        for row in range(8):
            # copy the current dotarray column values to the first column in the matrix
            matrix[row][offset + col] = (dotarray[row][col])
    #
    # Continually output to the display until Ctrl-C
    #
    check = 0
    while cancel == False:
        try:
            if check > 100:
                fbs.get_async('/Users', None, callback=log_user)
                check = 0;
            check += 1
            showmatrix()

        except KeyboardInterrupt:
            ldp.clear()
            print
            print "Finished"

