from breach_range import get_breach_range
from constants import SOC_UPPER as upperLimit,SOC_LOWER as lowerLimit, MESSAGES

def check_chargerate(CR):
	
	breach_range_value = get_breach_range(CR,upperLimit,lowerLimit)
	message = MESSAGES[breach_range_value]
	print(message)
	return !(breach_range_value == 1 or breach_range_value == 5)
