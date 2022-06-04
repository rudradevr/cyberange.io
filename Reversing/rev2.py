s = input('Enter Flag')

o = lambda a : ord(a)

if len(s) == 18:
    if o(s[0]) + o(s[1]) == 203 and o(s[1]) + o(s[2]) == 221 and o(s[2]) + o(s[3]) == 235 and o(s[3]) + o(s[4]) == 152 and o(s[4]) + o(s[5]) == 148 and o(s[5]) + o(s[6]) == 166 and o(s[6]) + o(s[7]) == 146 and o(s[7]) + o(s[8]) == 143 and o(s[8]) + o(s[9]) == 160 and o(s[9]) + o(s[10]) == 163 and o(s[10]) + o(s[11]) == 165 and s[1] == 105 and o(s[11]) + o(s[12]) == 211 and o(s[12]) + o(s[13]) == 213 and o(s[13]) + o(s[14]) == 221 and o(s[14]) + o(s[15]) == 216 and o(s[15]) + o(s[16]) == 221 and o(s[16]) + o(s[17]) == 225:
        print('flag{' + s + '}')
    else:
        print('check again bro')
else:
    print('check again bro')