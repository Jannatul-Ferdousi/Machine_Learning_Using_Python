# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) : #order should be followed of inedx, a and all
    print("room" + str(index)+ ":"+ str(a))
    #print("room " + str(index + 1) + ": " + str(area))