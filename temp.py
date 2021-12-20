import argparse

parser = argparse.ArgumentParser(description="This program prints recipes \
consisting of the ingredients you provide.")

# if an argument has a dash - or a double dash -- prefix, it'll be treated as optional.

parser.add_argument("-i1", "--ingredient_1")  # optional argument
                                              # or
parser.add_argument("ingredient_1")           # positional argument

                                                    # the parameter “action” is responsible for what should be done
parser.add_argument("--salt", action="store_true")  # with a command-line argument. By default, it just stores the
                                                    # value passed to the argument, though it's not the only option.

parser.add_argument("--pepper", default=False)  # This time the argument isn't used as a flag any more, so,
                                                # if you'd like to change the value, you will have to define it in
                                                # the command line explicitly: --pepper "True".

args = parser.parse_args() #The parse_args() method is used for reading argument strings from the command line

print(args.ingredient_2)  # onion
# (the value was chosen by a user from the given options)
print(args.ingredient_3)  # None
# (the value wasn't provided by a user)

#############################################################################################


parser = argparse.ArgumentParser(description="This program prints recipes \
consisting of the ingredients you provide.")

parser.add_argument("-i1", "--ingredient_1", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i2", "--ingredient_2", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i3", "--ingredient_3", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i4", "--ingredient_4", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i5", "--ingredient_5", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")

parser.add_argument("--salt", action="store_true",
                    help="Specify if you'd like to use salt in your recipe.")
parser.add_argument("--pepper", default="False",
                    help="Change to 'True' if you'd like to use pepper in your recipe.")

args = parser.parse_args()

ingredients = [args.ingredient_1, args.ingredient_2, args.ingredient_3,
               args.ingredient_4, args.ingredient_5]
if args.salt:
    ingredients.append("salt")
if args.pepper == "True":
    ingredients.append("pepper")

print(f"The ingredients you provided are: {ingredients}")


def find_a_recipe(ingredients):
    ...
    # processes the input and returns a recipe depending on the provided ingredients


# In this topic, we briefly familiarized ourselves with Python argparse module. There are three main steps to get the
# job done: first, create the ArgumentParser object; then, add arguments with add_argument() method; finally,
# parse them with the parse_args() method and use them in your program. Since what we discussed here is more of a
# review than a full description, it's definitely worth reading the argparse section in the official docs for more
# details, especially to learn about different parameter options you can use in your program.