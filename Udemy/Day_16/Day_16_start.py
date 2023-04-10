# import turtle
import prettytable

#
# timmy = turtle.Turtle()
# my_screen = turtle.Screen()
#
# timmy.shape('turtle')
# print(my_screen.canvheight)
# timmy.forward(200)
# my_screen.exitonclick()
#
table = prettytable.PrettyTable()

table.add_column("pokemon name", ["Pikachu", "Squitle"], "c")
table.add_column("Type", ["Elec", "Water"])

table.align = "l"
print(table)
