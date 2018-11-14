for _ in range(1,10**6):
 if any(_%k<1for k in[3,5,7])and str(_)[0]==str(_)[-1]:print(_)