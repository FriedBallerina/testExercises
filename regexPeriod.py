regex_pattern = r".{3}(\..{3}){3}"   # Do not delete 'r'.

import re
import sys

test_string = '123.456.abc.def'

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())