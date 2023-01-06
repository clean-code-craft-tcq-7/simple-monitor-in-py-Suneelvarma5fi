from check_soc import check_soc
if __name__ == '__main__':
  assert(check_soc(0.1) is True)
  assert(check_soc(0.3) is True)
  assert(check_soc(0.9) is False)
  assert(check_soc(0.8) is True)
  assert(check_soc(0) is True)
  assert(check_soc(-0.3) is False)
  