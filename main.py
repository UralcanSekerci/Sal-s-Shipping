# Sal's Shipping

weight = float(input("Weight of the package: "))
flat_charge = 20

# "Ground Shipping"

if weight <= 2:
    cost_ground = 1.50 * weight + flat_charge
elif weight <= 6:
    cost_ground = 3.00 * weight + flat_charge
elif weight <= 10:
    cost_ground = 4.00 * weight + flat_charge
else:
    cost_ground = 4.75 * weight + flat_charge
print("Ground Shipping Costs: ", cost_ground, "Dollars")

# Ground Shipping Premium

cost_ground_premium = 125.00
print("Ground Shipping Premium Costs: ", cost_ground_premium, "Dollars")

# Drone Shipping

if weight <= 2:
    cost_drone = 4.50 * weight
elif weight <= 6:
    cost_drone = 9.00 * weight
elif weight <= 10:
    cost_drone = 12.00 * weight
else:
    cost_drone = 14.25 * weight
print("Drone shipping Costs: ", cost_drone, "Dollars")

cg = 'Ground Shipping', cost_ground
cgp = 'Ground Shipping Premium', cost_ground_premium
cd = 'Drone shipping', cost_drone

minimum_price = (min(cg, cgp, cd))
print("\nCheapest way of Shipping is", minimum_price)
