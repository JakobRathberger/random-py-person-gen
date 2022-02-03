import datetime
import random
import time
from dateutil.relativedelta import relativedelta
import names

PERSON_TYPE = 'D'
AMOUNT = 15
START_ID = 101

start_date = datetime.date(1930, 1, 1)
end_date = datetime.date(2000, 1, 1)

sample_doctor_person = 'sample_doctor_person_data'
sample_doctor_special = 'sample_doctor_special_data'


def get_ssn_digit(dob):
    rand_num = random.randint(100, 999)

    digits = [int(x) for x in str(rand_num)]
    dig_sum = digits[0] * 3
    dig_sum += digits[1] * 7
    dig_sum += digits[2] * 9
    digits = [int(x) for x in str(dob)]
    dig_sum += digits[0] * 5
    dig_sum += digits[1] * 8
    dig_sum += digits[2] * 4
    dig_sum += digits[3] * 2
    dig_sum += digits[4] * 1
    dig_sum += digits[5] * 6

    return dig_sum % 11, rand_num

def get_random_date(start, end):
    time_between_dates = end - start
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start + datetime.timedelta(days=random_number_of_days)


fp_file = 'default_special'
f_file = 'default_person'

if PERSON_TYPE == 'D':
    fp_file = sample_doctor_special
if PERSON_TYPE == 'D':
    f_file = sample_doctor_person

with open(fp_file, 'w') as fp:
    with open(f_file, 'w') as f:

        f.write('insert into person(person_type, dob, firstname, lastname, ssn)\n')
        if PERSON_TYPE == 'D' or PERSON_TYPE == 'N':
            fp.write('insert into medicalstaff(person_id,salary,hiredate)\n')
        elif PERSON_TYPE == 'P':
            fp.write('insert into patient(person_id, weight, height)\n')

        for i in range(AMOUNT):
            random_date = get_random_date(start_date, end_date)

            first_name = names.get_first_name()
            last_name = names.get_last_name()

            year = random_date.strftime('%y')

            dob_str = f'{random_date.day:02d}{random_date.month:02d}{year}'

            digit = 10
            rand_num = 100
            while digit == 10:
                digit, rand_num = get_ssn_digit(dob_str)

            ssn = str(rand_num) + str(digit) + dob_str
            print(i)
            person_val = f'(\'{PERSON_TYPE}\',\'{random_date}\',\'{first_name}\',\'{last_name}\',\'{ssn}\')'
            person_line = f''
            special_val = f'({i+START_ID})'
            if PERSON_TYPE == 'D' or PERSON_TYPE == 'N':
                print(random_date)
                print(random_date + relativedelta(years=20))
                print(datetime.date.today())
                hire_date = get_random_date(random_date + relativedelta(years=20), datetime.date.today())
                print(hire_date)
                salary = round(random.uniform(2000, 4000), 2)
                special_val = f'({i+START_ID},{salary},\'{hire_date}\')'

            special_line = f''
            if i == 0:
                person_line = f'values{person_val},\n'
                special_line = f'values{special_val},\n'

            elif i == AMOUNT - 1:
                person_line = f'{person_val};\n'
                special_line = f'{special_val};\n'

            else:
                person_line = f'{person_val},\n'
                special_line = f'{special_val},\n'

            f.write(person_line)
            fp.write(special_line)


