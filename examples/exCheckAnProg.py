from verification import check_anfun

dictcppos = {}
cpdictconds = {}
progstru = []
dicttermexpr = {}
dict_var_types_cp = {}
curdir= ""
#program = "frac_fun_term_area"  # Ім'я аналізованої програми
program = "frac"
exdir = "anprograms"  # Ім'я каталогу аналізованих програм
filename = curdir + "\\" + exdir + "\\" + program + ".py"
res = check_anfun(filename, dictcppos, cpdictconds, progstru, dicttermexpr, dict_var_types_cp)
print("res = ", res)
print("dictcppos = ", dictcppos)
