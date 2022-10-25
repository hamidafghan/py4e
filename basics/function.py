# Define a function to say hey.
# def say_hey(name):
#     print("Hey", name)
#     print("How are you?")


# # use the say_hey function
# say_hey("hamid")

# define the full_name function
# def full_name(name, last_name):
#     print(name, last_name)


# # Call/invoke the full_name function
# full_name("Hamid", "Afghan")

# define the next step function
def next_step(current):
    # check if there is next step (1 - 5)
    if current > 0 and current < 5:
        return current + 1
    else:
        return None


# Get the current step from user
try:
    current_step = int(input("Current Step: "))

    # Call the next_step function
    print("The next step is", next_step(current_step))
except:
    print("Error, the number is not valid")
