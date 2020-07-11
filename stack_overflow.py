str_escaped = u'"A\u2167B"'
str_unicode = '"Война́ и миръ"'

arr_all_strings = [str_escaped, str_unicode]

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_escaped_unicode(str):
    #how do I determine if this is escaped unicode?
    if is_ascii(str): # escaped unicode is ascii
        return True
    return False

for str in arr_all_strings:
    if is_escaped_unicode(str):
        #str = str.decode("unicode-escape")
        print("Here")
        print(str)