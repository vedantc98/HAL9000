#Making a sample request to Product Advertisement API to retrieve item prices

import urllib
import requests
import string
#import hashlib
import hmac
import time
import datetime
import base64

def formatTime():
	temp = datetime.datetime.now()

	return datetime.datetime.isoformat(temp)

def get_signature(key, message):
	sign = hmac.new(key, message, hashlib.sha256).digest()
	return sign

test = """GET
webservices.amazon.co.uk
/onca/xml
AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Actor=Johnny%20Depp&AssociateTag=mytag-20&Operation=ItemSearch&Operation=ItemSearch&ResponseGroup=ItemAttributes%2COffers%2CImages%2CReviews%2CVariations&SearchIndex=DVD&Service=AWSECommerceService&Sort=salesrank&Timestamp=2014-08-18T17%3A34%3A34.000Z&Version=2013-08-01"""
testKey = "1234567890"


secretKey = "tAW3Nz0G4mHHxdXSYOsrVFESiyPm8ugDWSo40eD2"
accessKeyID = "AKIAJNUVYTV7KYDQLSZA"
associateTag = "hal900007-21"
baseSearchQuery = "https://webservices.amazon.in/onca/xml?"
Service = "AWSECommerceService"
Operation = "ItemSearch"
searchIndex = "FashionMen"
sortCriteria = "price"
query = "lacoste polo"
timestamp = formatTime()
HTTPverb = "GET"
HTTPRequestURI = "/onca/xml"
hostHeader = "webservices.amazon.com"
ResponseGroup = "ItemAttributes"

uncodedQuery = {
	"Service" : Service,
	"Operation" : Operation,
	"AWSAccessKeyId" : accessKeyID,
	"associateTag" : associateTag,
	"SearchIndex" : searchIndex,
	"Sort" : "price",
	"Keywords" : query,
	"Timestamp" : timestamp,
	"ResponseGroup" : ResponseGroup
}

encodedQuery = urllib.urlencode(uncodedQuery)
encodedQuery = baseSearchQuery + encodedQuery

canonicalizedQueryString = encodedQuery.replace("+", "%20").replace("*", "%2A").replace("%7E", "~")
stringToSign = HTTPverb + "\n" + hostHeader + "\n" + HTTPRequestURI + "\n" + canonicalizedQueryString

signature = get_signature(secretKey, canonicalizedQueryString)
signature = base64.b64encode(signature)

#print signature.replace("+", "%2B").replace("=", "%3D").replace("/", "%2F")
uncodedQuery['Signature'] = signature
payload = urllib.urlencode(uncodedQuery).replace("+", "%20").replace("*", "%2A").replace("%7E", "~")
payload = baseSearchQuery + payload
#payload = canonicalizedQueryString + "&Signature=" + signature.replace("+", "%2B").replace("=", "%3D").replace("/", "%2F")

print payload

response = requests.get(payload);

print response.text
