'''write a program to calculate batter strike rate from user given runs and balls '''

runs = int(input("Enter runs scored: "))
balls = int(input("Enter balls faced: "))

strike_rate = (runs / balls) * 100

print("Batting Strike Rate:", strike_rate)