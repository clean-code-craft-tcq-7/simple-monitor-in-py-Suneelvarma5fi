from check_temperature import check_temperature
from check_soc import check_soc
from check_chargerate import check_chargerate

def battery_is_ok(temp,soc,chargerate,tunit):
	return all(check_temperature(temp,tunit),check_soc(soc),check_chargerate(chargerate))
