#Author: Leon Abraham T. Apit

#This function will calculate the median of given list of numbers
#Function receive list as a parameter & returns single value

def median(list):

    #Checking for empty list

    if len(list) == 0:

        return 0

   

    list.sort() #Arranging list of elements

   

    midIndex = int(len(list) / 2)   #Determining middle element

   

    if len(list) % 2 == 1:

        #return median when number of elements in list is odd

        return list[midIndex]      

    else:

      #return median when number of elements in list is even

        return (list[midIndex] + list[midIndex - 1]) / 2

#This function will calculate the mean of given list of numbers

#Function receive list as a parameter & returns single value

def mean(list):

    #Checking for empty list

    if len(list) == 0:

        return 0

    total = 0

    for number in list:

        total += number

    return total / len(list)    #returns calculated mean

#This function will calculate the mode of given list of numbers

#Function receive list as a parameter & returns single value

def mode(list):

    if len(list) == 0:

        return 0

    numberDictionary = {}       #Creating dictionary

    for digit in list:

        number = numberDictionary.get(digit, None)

        if number == None:

            numberDictionary[digit] = 1

        else:

            numberDictionary[digit] = number + 1

    #Getting the maximum value from list

    maxValue = max(numberDictionary.values())

    modeList = []

    for key in numberDictionary:

        #Determing elements which has the maximum value

        if numberDictionary[key] == maxValue:

            modeList.append(key)        #adding elements into list whose value is maximum

    return modeList         #returns mode list

def main():

    #Creating list

    list = [5, 5, 3, 2, 8, 1, 4]

   

    print("List:", list)    #Printing list of elements

   

    #Printing mode of given list by calling function & passed list as a parameter

    print ("Mode: ", mode(list))

    #Printing median of given list by calling function & passed list as a parameter

    print ("Median :", median(list))

    #Printing mean of given list by calling function & passed list as a parameter

    print ("Mean: ", mean(list))

main()