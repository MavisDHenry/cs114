print('how much change would you like?')
change = int(input())
coins_in_quarters = change // 25
change_left_quarters = change - (coins_in_quarters * 25)
coins_in_dimes = change_left_quarters // 10
change_left_dimes = change_left_quarters - (coins_in_dimes * 10)
coins_in_nickles = change_left_dimes // 5
change_left_nickles = change_left_dimes - (coins_in_nickles * 5)
coins_in_pennies = change_left_nickles // 1
change_left_pennies = change_left_nickles - (coins_in_pennies * 1)
total_coins = ('quarters ' + str(coins_in_quarters) + " dimes " +
               str(coins_in_dimes) + ' nickles ' + str(coins_in_nickles) +
               ' pennies ' + str(coins_in_pennies) + '.')
print(total_coins)