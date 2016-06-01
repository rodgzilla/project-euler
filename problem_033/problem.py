from fractions import Fraction

res = []
for denom in range(10, 100):
    for nom in range(10, denom):
        s_denom, s_nom = str(denom), str(nom)
        frac = Fraction(nom, denom)
        for i in range(len(s_denom)):
            new_denom = s_denom[:i] + s_denom[i+1:]
            new_nom = ''.join([c for c in s_nom if c != s_denom[i]])
            if new_nom != '' and new_denom!= '' and int(new_denom) != 0 and s_denom[-1] != '0' and Fraction(int(new_nom), int(new_denom)) == frac:
                res.append((nom, denom))

final_num, final_denum = 1, 1
for num, denum in res:
    final_num *= num
    final_denum *= denum

print(Fraction(final_num, final_denum).denominator)
            
    
            
