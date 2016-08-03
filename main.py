
from firebase import firebase
from firebase_token_generator import create_token
from pprint import pprint

import sys
import fontv
import ldp




"""
#Creates the Token necesarry for Authorization
# "private_key" in the credentials JSON
private_key = 'YOUR PRIVATE KEY HERE' # "client_email" in the credentials JSON
service_account_email = "YOUR EMAIL FROM SERVICE ACCOUNT"
auth_payload = {"auth_data": "foo", "other_auth_data": "bar"}
token = create_token(service_account_email, private_key, "user1", auth_payload)

#Access the firebase database
# FIREBASE -> PYTHON
fbs = firebase.FirebaseApplication('PROJECT URL', None)


authentication = firebase.FirebaseAuthentication('SECRET', 'EMAIL', extra={'id': 123})
fbs.authentication = authentication
print authentication.extra

#AUTHENTICATIONS
user = authentication.get_user()
user.firebase_auth_token = token
#print user.firebase_auth_token
"""

global cancel
global count
count = 0
cancel = False
#reg_users = fbs.get('/Users', None)
reg_users = [1,2,3,4,5]
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


    #
    # function to shift left all the vaules of the matrix array
    # this allows us to put new data in the first column
    #
    def shiftmatrix():
        for row in range(8):
            for col in range(79, 0, -1):
                matrix[row][col] = matrix[row][col - 1]
    # end def

    # function to read the matrix array and output the values to the display device
    #
    def showmatrix():
        ldp.displayoff()
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
    #
    # assign the command line args for the text and colour
    #

    textinput = str("{:,}".format(count*1000))
    # textinput=str(sys.argv[1])
    colour = 1

    # append extra characters to text input to allow for wrap-around
    textinput += '  ::  '

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
    #
    # Continually output to the display until Ctrl-C
    #
    check = 0
    while cancel == False:
        try:
            """
            response = fbs.get('/Users', None)
            if len(response) != count:
                count = len(response)
                cancel = True
                print(count)
            """
            if check > 10:
                #fbs.get_async('/Users', None, callback=log_user)
                log_user([1,2,3,4,5])
                check = 0
            # loop around each column in the dotarray
            for col in range(len(dotarray[0])):
                for row in range(8):
                    # copy the current dotarray column values to the first column in the matrix
                    matrix[row][0] = (dotarray[row][col])
                # now that we have updated the matrix lets show it
                showmatrix()
                # shift the matrix left ready for the next column
                shiftmatrix()
            check += 1
        except KeyboardInterrupt:
            ldp.clear()
            print
            print "Finished"

