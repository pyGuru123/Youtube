# pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

ph = '+919935927853'

obj = phonenumbers.parse(ph,None)

print(obj)
print(phonenumbers.is_valid_number(obj))
print(geocoder.description_for_number(obj,'en'))
print(carrier.name_for_number(obj,'en'))
print(timezone.time_zones_for_number(obj))