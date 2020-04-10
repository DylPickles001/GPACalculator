#try to include a loop input to redirect to the homepage if misinput
#also include cumulative GPA
print ("Ready to find your G.P.A? ")
print ('Type "cumulative" to find your cumulative GPA.')
asking = input('Do you want to find your weighted or unweighted GPA? ')
if asking == "unweighted":
  ask0 = int(input('How many classes are you taking? '))
  def grades():
    a = int(input('How many As do you have? '))
    b = int(input('How many Bs do you have? '))
    c = int(input('How many Cs do you have? '))
    d = int(input('How many Ds do you have? '))
    gradea = 4*a
    gradeb = 3*b
    gradec = 2*c
    graded = 1*d
    calc = (gradea+gradeb+gradec+graded)/ask0
    print("Your Weighted G.P.A. is:",calc)
  grades()
if asking == "weighted":
  ask0 = int(input('How many classes are you taking? '))
  def wgrades():
    a = int(input('How many As from a regular class do you have? '))
    aw = int(input('How many As from honors or AP classes do you have? '))
    b = int(input('How many Bs from a regular class do you have? '))
    bw = int(input('How many Bs from honors or AP classes do you have? '))
    c = int(input('How many Cs from a regular class do you have? '))
    cw = int(input('How many Cs from honors or AP classes do you have? '))
    d = int(input('How many Ds do you have? '))
    gradea = 4*a
    gradeaw = 5*aw
    gradeb = 3*b
    gradebw = 4*bw
    gradec = 2*c
    gradecw = 3*cw
    graded = 1*d
    calc = (gradea+gradeaw+gradeb+gradebw+gradec+gradecw+graded)/ask0
    print("Your Weighted G.P.A. is:",calc)
  wgrades()
if asking == "cumulative":
  ask0 = input('Do you want to find your weighted or unweighted cumulative GPA? ')
  if ask0 == "weighted":
    classF = int(input('How many classes did you take 9th Grade? '))
    def wgradesF():
       a = int(input('How many As from a regular class do you have? '))
       aw = int(input('How many As from honors or AP classes do you have? '))
       b = int(input('How many Bs from a regular class do you have? '))
       bw = int(input('How many Bs from honors or AP classes do you have? '))
       c = int(input('How many Cs from a regular class do you have? '))
       cw = int(input('How many Cs from honors or AP classes do you have? '))
       d = int(input('How many Ds do you have? '))
       gradea = 4*a
       gradeaw = 5*aw
       gradeb = 3*b
       gradebw = 4*bw
       gradec = 2*c
       gradecw = 3*cw
       graded = 1*d
       calc = (gradea+gradeaw+gradeb+gradebw+gradec+gradecw+graded)/classF
    wgradesF()
  if ask0 == "unweighted":
    classF = int(input('How many classes did you take 9th Grade? Include both semesters. '))
    def gradesF():
       a = int(input('How many As from a regular class do you have? '))
       aw = int(input('How many As from honors or AP classes do you have? '))
       b = int(input('How many Bs from a regular class do you have? '))
       bw = int(input('How many Bs from honors or AP classes do you have? '))
       c = int(input('How many Cs from a regular class do you have? '))
       cw = int(input('How many Cs from honors or AP classes do you have? '))
       d = int(input('How many Ds do you have? '))
       gradea = 4*a
       gradeaw = 5*aw
       gradeb = 3*b
       gradebw = 4*bw
       gradec = 2*c
       gradecw = 3*cw
       graded = 1*d
       calc = (gradea+gradeaw+gradeb+gradebw+gradec+gradecw+graded)/classF
    gradesF()   
