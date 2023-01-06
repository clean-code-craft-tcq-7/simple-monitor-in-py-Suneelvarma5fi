#converts the temperature from other units to celsius and returns true if valid else invalid

from converter import farhen_to_celsius
from breach_range import get_breach_range
from constants import T_UPPER as upperLimit,T_LOWER as lowerLimit, MESSAGES

def check_temperature(temp,unit):
	
	if unit == "F": temp = farhen_to_celsius(temp)
	breach_range_value = get_breach_range(temp,upperLimit,lowerLimit)
	message = MESSAGES[breach_range_value]
	print(message)
	return not (breach_range_value == 1 or breach_range_value == 5)
