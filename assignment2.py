apples  = 100
net_cost  =7.5
net_invest = apples * net_cost
apples_cost_1 = 10
apples_sold_1 = 20
amount_1 = apples_cost_1 * apples_sold_1
apples_cost_2 = 50
apples_sold_2 = 30
amount_2 = apples_sold_2 * apples_cost_2
total_profit = (amount_1 + amount_2) - net_invest
print("profit from selling apples",total_profit)
print("amount of apples can be purchased", total_profit/net_cost)
