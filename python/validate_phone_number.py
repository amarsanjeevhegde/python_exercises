# Program to convert input to
# phonenumber format
  
import phonenumbers
  
# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx
phoneNumber = phonenumbers.parse("+919876543210")
phoneNumber1= phonenumbers.parse("+971553545682")
  
# This will print the phone number and 
# it's basic details.
print(phoneNumber)
print(phoneNumber1)
