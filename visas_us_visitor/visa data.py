import urllib.request


codes = dict()
with open('codes') as in_f:
    for line in in_f:
        line = line.strip()
        code, city = line.split(',')
        codes[code] = city

answers = dict()
counter = 0

# Interview Required Students/Exchange Visitors (F, M, J) 	45 Calendar Days
# Interview Required Petition-Based Temporary Workers (H, L, O, P, Q) 	45 Calendar Days
# Interview Required Crew and Transit (C, D, C1/D) 	45 Calendar Days
# [0] Interview Required Visitors (B1/B2) 	160 Calendar Days
# Interview Waiver Students/Exchange Visitors (F, M, J) 	10 Calendar Days
# Interview Waiver Petition-Based Temporary Workers (H, L, O, P, Q) 	10 Calendar Days
# Interview Waiver Crew and Transit (C, D, C1/D) 	10 Calendar Days
# Interview Waiver Visitors (B1/B2)

for code in codes.keys():
    url = f'https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid={code}&aid' \
          f'=VisaWaitTimesHomePage '
    s = urllib.request.urlopen(url).read().decode('utf-8').strip()
    try:
        time_days = int(s.split('|')[0].split()[0])
    except ValueError:
        time_days = 999
    except Exception:
        print(f'error with code number {code}, string {s}')
    answers[codes[code]] = time_days
    counter += 1
    if counter % 5 == 0:
        print(f'{counter} requests processed')

out = ''
for name in sorted(answers, key=lambda x: answers[x]):
    out += f'{name}\t{answers[name]}\n'

with open('answer.txt', 'w') as out_file:
    out_file.write(out)
