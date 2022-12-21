
# Ground Shipping


def cost_ground(weight):

    cost = 0
    flat_charge = 20
    if weight <= 2:
        cost += weight*1.50
    elif weight <= 6:
        cost += weight*3.00
    elif weight <= 10:
        cost += weight*4.00
    else:
        cost += weight*4.75
    cost += flat_charge
    return "Here is your total with Ground Shipping: ₺" + str(cost)

# Ground Shipping Premium


cost_ground_premium = 125.00

# Drone Shipping


def cost_drone(weight):
    cost = 0
    if weight <= 2:
        cost += weight*4.5
    elif weight <= 6:
        cost += weight*9
    elif weight <= 10:
        cost += weight*12
    else:
        cost += weight*14.25
    return "Here is your total with Drone Shipping: ₺" + str(cost)


# Information needed

weight_told = int(input("What's the weight?"))
typeof_transport = input("What type of transport do you need?")

if typeof_transport == "G":
    print(cost_ground(weight_told))
elif typeof_transport == "GP":
    print("Here is your total with Ground Shipping Premium ₺" + str(cost_ground_premium))
elif typeof_transport == "Drone":
    print(cost_drone(weight_told))
