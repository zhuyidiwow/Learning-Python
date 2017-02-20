import random

def monte_carlo(no_of_days):
	sum_demand = 0
	demand_today = 0
	
	i = 0

	while i < no_of_days:
		rand = random.random()

		if rand > 0.85:
			demand_today = 600
		elif rand > 0.65:
			demand_today = 500
		elif rand > 0.35:
			demand_today = 400
		elif rand > 0.15:
			demand_today = 300
		elif rand > 0.05:
			demand_today = 200
		else:
			demand_today = 100

		sum_demand = sum_demand + demand_today
		i = i + 1;
	print "Sum demand:", sum_demand
	print "Mean demand:", sum_demand / i + 1


no_of_days = int(raw_input("Enter days: "))
monte_carlo(no_of_days)