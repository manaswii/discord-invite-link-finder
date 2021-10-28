import asyncio
import csv
import json
import urllib.request

SIZE = 8

def incrementString(str, pos):

    if str[pos] >= 'a' and str[pos] <= 'y':
        str = str[0:pos] + chr(ord(str[pos]) + 1) + str[pos + 1:]

    elif str[pos] == 'z':
        str = str[0:pos] + 'A' + str[pos + 1:]

    elif str[pos] >= 'A' and str[pos] <= 'Y':
        str = str[0:pos] + chr(ord(str[pos]) + 1) + str[pos + 1:]

    elif str[pos] == 'Z':
        str = str[0:pos] + '0' + str[pos + 1:]

    elif str[pos] >= '0' and str[pos] <= '8':
        str = str[0:pos] + chr(ord(str[pos]) + 1) + str[pos + 1:]

    elif str[pos] == '9':
        str = str[0:pos] + 'a' + str[pos + 1:]
        str = incrementString(str, pos - 1)

    return str


def finishedCheck(inputString):
    if inputString == "99999999":
        return True
    return False


def checkValidity(str):
    try:
        url = f'https://discord.com/api/v6/invites/{str}?with_counts=true'
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers = {'User-Agent': user_agent, }
        request = urllib.request.Request(url, None, headers)  # The assembled request
        response = urllib.request.urlopen(request)
        data = response.read()  # The data u need
        mydata = json.loads(data.decode('utf-8'))
        with open('foundValidLinks.csv', 'a') as csv_file1:
            fieldNames = ['name', 'approximate_member_count', 'invite_link']
            csv_writer1 = csv.DictWriter(csv_file1, fieldnames=fieldNames)
            print("found")
            csv_writer1.writerow({'name' : mydata['guild']['name'], 'approximate_member_count' : mydata['approximate_member_count'], 'invite_link' : str })
    except:
        print("not_found")
        return


def generateStrings(inputString):

    try:
        while finishedCheck(inputString) == False:
            # print(inputString)
            checkValidity(inputString)
            asyncio.sleep(0.1)
            inputString = incrementString(inputString, SIZE - 1)
        print("all values are checked")
    except KeyboardInterrupt:
        print("exiting")
        with open('starting.csv', 'w') as csv_file:
            fieldNames = ['stringCombination']
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldNames)
            csv_writer.writeheader()
            csv_writer.writerow({'stringCombination': inputString})
            pass


def main():

    with open('starting.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        starter = next(csv_reader)['stringCombination']
    generateStrings(starter)


main()
