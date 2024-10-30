weight = 41.5

#Ground shipping

cost = 0

if weight <= 2:
  cost = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
  cost  = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  cost = weight * 4.00 + 20
elif weight > 10:
  cost = weight * 4.75 + 20 

print("Ground Shipping $: ", cost)
#Ground premium shipping

cost_premium = 125.00

print("Ground Premium Shipping $: ", cost_premium)

#Drone shipping

if weight <= 2:
  cost = weight * 4.50
elif weight > 2 and weight <= 6:
  cost = weight * 9.00
elif weight > 6 and weight <= 10:
  cost = weight * 12.00
elif weight > 10:
  cost = weight * 14.25

print("Drone Shipping $:", cost)