from check_date import ch_date as chd
from sys import argv

my_date = ['30.02.2020', '28.02.211020', '29.02.2020', '31.112.2020', '31.12.2023']

for i in my_date:
    print(i, chd(i), end=' | ')

term_date = str(argv[-1])
print(f'Terminal date: {term_date} {chd(term_date)}')