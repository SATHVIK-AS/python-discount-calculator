# Ask for Coustomer name
customer_name = input("Customer Name      :")

#Ask for Item price 
item_price = int(input("Item Price      :"))

#Ask for Quantity
quantity = int(input("Quantity      :"))

#calculating  total 
total = item_price * quantity

#Calculating Discount Amount

# Conditions for Discount
if total >= 5000 :
  #calculating Discount
  Discount_amount = total * 20 / 100 
  #calculating Final Amount
  Final_amount = total - Discount_amount 

  print("Discount =",Discount_amount)

  print("Final Amount =",Final_amount)

elif total >= 3000 :
  #calculating Discount
  Discount_amount = total * 15/ 100 
  #calculating Final Amount
  Final_amount = total - Discount_amount 

  print("Discount =",Discount_amount)

  print("Final Amount =",Final_amount)

elif total >= 1000 :
  #calculating Discount Amount
  Discount_amount = total * 10 / 100 
  #calculating Final Amount
  Final_amount = total - Discount_amount 

  print("Discount =",Discount_amount)

  print("Final Amount =",Final_amount)

else :
  print("Discount = No discount")

                  
