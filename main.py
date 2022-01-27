import datetime
import random
import time

import names

PERSON_TYPE = 'P'
AMOUNT = 100
START_ID = 1

start_date = datetime.date(1920, 1, 1)
end_date = datetime.date(2020, 1, 1)


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


with open('sample_special_data', 'w') as fp:
    with open('sample_person_data', 'w') as f:

        f.write('insert into person(person_type, dob, firstname, lastname, ssn)\n')
        if PERSON_TYPE == 'P':
            fp.write('insert into patient(person_id)\n')

        for i in range(AMOUNT):
            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)

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
            if i == 0:
                f.write(f'values(\'{PERSON_TYPE}\',\'{random_date}\',\'{first_name}\',\'{last_name}\',\'{ssn}\'),\n')
                if PERSON_TYPE == 'P':
                    fp.write(f'values({i+START_ID}),\n')
            elif i == AMOUNT - 1:
                f.write(f'(\'{PERSON_TYPE}\',\'{random_date}\',\'{first_name}\',\'{last_name}\',\'{ssn}\');\n')
                if PERSON_TYPE == 'P':
                    fp.write(f'({i+START_ID});\n')
            else:
                f.write(f'(\'{PERSON_TYPE}\',\'{random_date}\',\'{first_name}\',\'{last_name}\',\'{ssn}\'),\n')
                if PERSON_TYPE == 'P':
                    fp.write(f'({i+START_ID}),\n')

