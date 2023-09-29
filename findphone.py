import phonenumbers
from phonenumbers import geocoder
# install the phonenumbers library
# pip phonenumbers

first_num = phonenumbers.parse("+") #input your Phone number inclued your country code

print(geocoder.description_for_number(first_num, "en"))
