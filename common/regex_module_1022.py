import re
import logging as log

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s -  %(levelname)s - %(message)s'
    )


def isEmail(addr):
    tst = re.compile(r'\w[a-z0-9_.]*\w@(\w{2,})(\.\w{2,})+', re.IGNORECASE)
    res = tst.fullmatch(addr)
    if res == None:
        return False
    else:
        return True

def isPhone(num):
    tst = re.compile(r'(\d{3}|\(\d{3}\))[ -.]?\d{3}[ -.]?\d{4}')
    res = tst.fullmatch(num)
    if res == None:
        return False
    else:
        return True


def run_email_unit_tests():
    all_addresses_dict = {
        'paul@yorkfamily.com': True,
        'paul.york@augusta.edu': True,
        'pyork1@augusta.edu': True,
        'ptyork@cc.gatech.edu': True,
        'ptyork@marchfirst.co.uk': True,
        'PAUL.YORk@auGUsta.edu': True,
        'paul@yorkfamily_com': False,
        'a@b.c': False,
        'j,,@@': False,
        'j..@..com': False,
        'I am not an email': False,
        'paul york@augusta university.edu': False,
        'paul@yorkfamily,.com': False,
        'paul,york@augusta.edu': False,
        ',@@_._': False,
        '.paul@yorkfmaily.com': False,
        'paul.@augusta.edu': False
    }

    for addr in all_addresses_dict:
        expected_res = all_addresses_dict[addr]
        res = isEmail(addr)
        log.debug(f'TESTING {addr}, EXPECTING {expected_res}, GOT {res}')
        assert res == expected_res

if __name__ == "__main__":
    run_email_unit_tests()
