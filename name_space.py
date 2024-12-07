calls = 0
string = ""
list_to_search = []

def count_calls():
    global calls
    calls += 1
    return


def string_info(name):
    info = ()
    info = info + (int(len(name)), name.upper(), name.lower())
    count_calls()
    return info

def is_contains(string, list_to_search):
    string = string.lower()
    for list in list_to_search:
        if string == list.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
