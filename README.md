# dice
Simple dice-rolling utility. Goal of the project would be to provide a numerical result and provide additional info using flags.

Use:

dice.py [-rmdog] [<Amount of dice>d<Die maximum value>]

Examples:

dice.py -r
dice.py --median 20d6
dice.py -m 4d20
dice.py

Flags:

-r or --results: Prints the results of each die tallied.
-m or --mean: Prints the mathematical mean from the dice rolled.
-d or --median: Prints the mathematical median from the dice rolled.
-o or --mode: Prints the mathematical mode from the dice rolled.
-g or --range: Prints the mathematical range from the dice rolled.
No flags: Only print the sum of the dice rolled.
