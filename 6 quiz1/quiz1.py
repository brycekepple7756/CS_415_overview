#
#Bryce Kepple
#Quiz 1
#

#setting all the variables that will be used later
three_ds=75.94
Wii_U=13.56
Wii=101.63
DS=154.02
Game_Boy_Advance=81.51
Game_Boy=118.69
GameCube=21.74
Nintendo_64=32.93
SNES=49.10
NES=61.91

#gathering the users input
Switch=float(input("how many units (in millions) has the Switch sold? "))


#multiplying  the string "-" 29 times so it prints out 29 dashes
print("-"*29)
#using the format code <20s to make the text left oriented in a 20 space column and then making right oriented text in a 8 space column
print(f"{'Nintendo Console' : <20s}{'|'}{'Sales' : >8s}")
print("-"*29)

# also using the format code to print left generated code in a 20 space column then printing the float number only to the first decimal point
print(f"{'Switch' : <20s}{'|   '}{Switch : .1f}")
print(f"{'3DS' : <20s}{'|    '}{three_ds : .1f}")
print(f"{'Wii U' : <20s}{'|    '}{Wii_U : .1f}")
print(f"{'Wii' : <20s}{'|   '}{Wii : .1f}")
print(f"{'DS' : <20s}{'|   '}{DS : .1f}")
print(f"{'Game Boy Advance' : <20s}{'|    '}{Game_Boy_Advance : .1f}")
print(f"{'Game Boy' : <20s}{'|   '}{Game_Boy : .1f}")
print(f"{'GameCube' : <20s}{'|    '}{GameCube : .1f}")
print(f"{'Nintendo 64' : <20s}{'|    '}{Nintendo_64 : .1f}")
print(f"{'Super NES' : <20s}{'|    '}{SNES : .1f}")
print(f"{'NES' : <20s}{'|    '}{NES : .1f}")
