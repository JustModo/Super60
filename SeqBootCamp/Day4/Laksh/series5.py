# 6 23 90 267 638 1311 2418 4115
#  17 67
levelOne=6
levelTwo=17
levelThree=50
levelFour=60
levelFive=24 
for _ in range(10):
    print(levelOne, end=" ")
    levelOne+=levelTwo
    levelTwo+=levelThree
    levelThree+=levelFour
    levelFour=levelFour+levelFive
    
