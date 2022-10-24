import math

##Oppgave 1##
''' Hvis du  blir tilbudt 300 krone for å vaske et hus, ville du gjort det
da? hva om du ble tilbudt dette i 2 månader, hvor betalingen ville økes 15%
hver dag. Det vil si kr300 første dag, 345 andre dag, kr396.75 neste dag, osv.  '''
amount = 300
for i in range(60):
    amount = amount * 1.15
print("Etter 2 måneder du vil bli tilbudt " + str(round(amount, 2)) + "kr") 
  ### your task##
'''Lag en funksjon som regner ut total lønn etter 2 måneder, og lønn for 
dag 15, 30, 45 og 50. Bruk print() for å vise disse verdiene i terminalen'''
basesalary = 4500
print("Du starter med " + str(basesalary) + "kr")
print("Lønn var " + str(basesalary * 2) + "kr etter 2 måneder")
salaryperday = basesalary / 30
print("Etter 15 dager du vil har" + str(salaryperday * 15))
print("Etter 30 dager du vil har" + str(salaryperday * 30))
print("Etter 45 dager du vil har" + str(salaryperday * 45))
print("Etter 50 dager du vil har" + str(salaryperday * 50))

##Oppgave 2##
''' Opprett en funksjon som kan tegne følgende figur i terminalen:
*
**
***
****
*****
******
*******
********
*********
**********
***********
          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********
 **********
***********
'''
def DrawShape():
  startstring1 = "*"
  for i in range(10):
    print(startstring1)
    startstring1 = startstring1 + "*"
  startstring2 = "         *"
  asterisks = 1
  spaces = 9
  for i in range(10):
    print(startstring2)
    startstring2 = ""
    asterisks += 1
    spaces -= 1
    for i in range(spaces):
      startstring2 = startstring2 + " "
    for i in range(asterisks):
      startstring2 = startstring2 + "*" 

DrawShape()

##Oppgave 3##
''' Opprett en funksjon som kan printe alle primtall i variabel prime_numbers '''
prime_numbers = [1, 5, 6, 7, 10, 11, 19, 23, 25, 26, 31, 26, 37, 40, 43, 67, 73, 99, 101]
for i in range(len(prime_numbers)):
  print(prime_numbers[i])
#E