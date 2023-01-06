from battery_is_ok import battery_is_ok
if __name__ == '__main__':
  assert(battery_is_ok(43,20,0.1,"C") is True)
  assert(battery_is_ok(0,22,0.8,"C") is True)
  assert(battery_is_ok(111,20,0.1,"F") is True)
  assert(battery_is_ok(120,20,0.1,"F") is True)
  assert(battery_is_ok(30,81,0.1,"C") is False)
  assert(battery_is_ok(35,76,0,"C") is True)
  assert(battery_is_ok(43,24,0.9,"C") is True)