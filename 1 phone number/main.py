
import phonenumbers
from test import number 
#print(number)

#Find country from mobile num
from phonenumbers import geocoder
ch_number=phonenumbers.parse(number,"CH")
#print(ch_number)
print(geocoder.description_for_number(ch_number,"en"))

#Find service provider d
from phonenumbers import carrier
service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))
