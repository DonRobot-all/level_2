# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_2
#     ................
#     case шаблон_N:
#         действие_N
#     case _:
#         действие_по_умолчанию


day = "Monday"
match day:
    case "Sunday"    : print("Take it easy")
    case "Monday"    : print("Go to work")
    case "Tuesday"   : print("Work + Hobbies")
    case "Wednesday" : print("Meetings")
    case "Thursday"  : print("Presentations")
    case "Friday"    : print("Interviews and party")
    case "Saturday"  : print("Time to do sports")


# Шаблон захвата (capture)
def greet(name=None):
    match name:
        # Check if name == None
        case None:
            print("Hello there")
        # Store name into some_name if it is not None
        case some_name:
            print(f"Hello {some_name}")
greet()       # Prints "Hello there"
greet("Jack") # Prints "Hello Jack"

# Шаблон подстановки (wildcard)
coinflip = 4
match coinflip:
    case 1:
        print("Heads")
    case 0:
        print("Tails")
    case _:
        print("Must be 0 or 1.")

location = (0, 0)
match location:
    case (_,):
        print("1D location found")
    case (_, _):
        print("2D location found")
    case (_, _, _):
        print(("3D location found"))


directions = ["North", "East", "South", "West"]
# Grab the values from a list and store them into variables
n, e, s, w = directions
print(n) # prints North
print(e) # prints East
print(s) # prints South
print(w) # prints West

location = (1, 3)
match location:
    case x, :
        print(f"1D location found: ({x})")
    case x, y:
        print(f"2D location found: ({x}, {y})")
    case x, y, z:
        print((f"3D location found: ({x}, {y}, {z})"))

def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "english":
            print("Hello")
        case "german":
            print("Hallo")
        case _:
            print("Undefined")
 
 
print_hello("english")      # Hello
print_hello("spanish")      # Undefined


def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "american english" | "british english" | "english":
            print("Hello")
        case _:
            print("Undefined")
 
 
print_hello("english")              # Hello
print_hello("american english")     # Hello
print_hello("spanish")              # Undefined