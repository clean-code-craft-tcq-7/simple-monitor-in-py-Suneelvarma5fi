from constants import WARNING_THRESHOLD
def get_breach_range(value, ulimit,llimit):
	warning_limit = (WARNING_THRESHOLD/100)*ulimit
	if value < llimit:
		return 1
	elif value > ulimit:
		return 5
	elif (value == llimit or value <= llimit+warning_limit):
		return 2
	elif (value == ulimit or value <= llimit-warning_limit):
		return 4
	else:
		return 3
