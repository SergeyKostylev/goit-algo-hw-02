import re


def check(string_to_check: str):
    string_to_check = re.sub(r'[^\[\]\(\)\{\}]', '', string_to_check)

    while True:
        previous_len = len(string_to_check)
        if previous_len == 0:
            return True

        string_to_check = re.sub(r'\(\)|\[\]|\{\}', '', string_to_check)
        if len(string_to_check) == previous_len:
            return False


string_list = [
    '{2}([()sdf(fds)])[]dasd',
    '{2}([(])[]dasd',
    '( ){[ 1 ]( 1 + 3 )( ){ }}',
    '( 23 ( 2 - 3);',
    '( 11 }',
]

for item in string_list:
    res = 'Симетрично' if check(item) else 'Несиметрично'
    print(f'{item}: {res}')
