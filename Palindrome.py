def convert_to_lower(s):
    s= s.lower().replace(" ","")
    reversed_s = s[::-1]
    if reversed_s == s:
        return True
    else:return False

st= "Hello World"

print(convert_to_lower(st))



