#checks if a site if running or not 
#import urllib
#use urllib.request to get the data from the url
#write function that takes url and returns response

import urllib.request as urllib

def main(url):
    print("Checking connectivity...")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully.")
    print("The response code was:", response.getcode()) #200 means it was successful

print("This is a site connectivity checker program.")
input_url = input("Input the URL of the site: ")

main(input_url)