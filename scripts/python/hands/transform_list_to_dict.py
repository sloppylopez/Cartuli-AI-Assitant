def list_2_dict(target_list):
    return {item[0]: item[1:] for item in target_list}


if __name__ == "__main__":
    list_2_dict([['19960bfcb5a3998168f27f9f359e06ac12ca0e6fd25fd9eb6af83307088fced1', 'def ', 'ginea_pig.py'],
                 ['6515116c90b1433aef904d909c78833778fe4d46ae0dbb6c2b3a5e14a6a67802', 'def ',
                  'ginea_pig_prime_numbers.py']])
