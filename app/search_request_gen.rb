#!/usr/bin/env ruby

require 'time'
require 'uri'
require 'openssl'
require 'base64'

# Your Access Key ID, as taken from the Your Account page
ACCESS_KEY_ID = "AKIAJNUVYTV7KYDQLSZA"

# Your Secret Key corresponding to the above ID, as taken from the Your Account page
SECRET_KEY = "tAW3Nz0G4mHHxdXSYOsrVFESiyPm8ugDWSo40eD2"

# The region you are interested in
ENDPOINT = "webservices.amazon.in"

REQUEST_URI = "/onca/xml"

searchIndex = "All"
#Take search query and index input from python master
searchQuery = ARGV[0]
searchQuery = searchQuery.gsub("+", " ")
searchIndex = ARGV[1]

params = {
  "Service" => "AWSECommerceService",
  "Operation" => "ItemSearch",
  "AWSAccessKeyId" => "AKIAJNUVYTV7KYDQLSZA",
  "AssociateTag" => "hal900007-21",
  "SearchIndex" => searchIndex,
  "Keywords" => searchQuery,
  "ResponseGroup" => "ItemAttributes"
}

# Set current timestamp if not set
params["Timestamp"] = Time.now.gmtime.iso8601 if !params.key?("Timestamp")

# Generate the canonical query
canonical_query_string = params.sort.collect do |key, value|
  [URI.escape(key.to_s, Regexp.new("[^#{URI::PATTERN::UNRESERVED}]")), URI.escape(value.to_s, Regexp.new("[^#{URI::PATTERN::UNRESERVED}]"))].join('=')
end.join('&')

# Generate the string to be signed
string_to_sign = "GET\n#{ENDPOINT}\n#{REQUEST_URI}\n#{canonical_query_string}"

# Generate the signature required by the Product Advertising API
signature = Base64.encode64(OpenSSL::HMAC.digest(OpenSSL::Digest.new('sha256'), SECRET_KEY, string_to_sign)).strip()

# Generate the signed URL
request_url = "http://#{ENDPOINT}#{REQUEST_URI}?#{canonical_query_string}&Signature=#{URI.escape(signature, Regexp.new("[^#{URI::PATTERN::UNRESERVED}]"))}"

puts "#{request_url}"
