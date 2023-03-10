from constants import WARNING_THRESHOLD
def get_breach_range(value, ulimit,llimit):
	warning_limit = (WARNING_THRESHOLD/100)*ulimit
	if value < llimit:
		return 1
	elif value > ulimit:
		return 5
	else:
		return get_valid_range(value,ulimit,llimit)
	
def get_valid_range(value,ulimit,llimit):
	warning_limit = (WARNING_THRESHOLD/100)*ulimit
	if value <= llimit+warning_limit:
		return 2
	elif value <= (llimit-warning_limit):
		return 4
	else:
		return 3
