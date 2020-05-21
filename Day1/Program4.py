#Take 2 inputs, CostPrice,SellingPrice of a product for user and return following:
#1.profit from sell
#2.what should be the selling price if we increased th profit by 5% 

costprice=int(input("Enter the cost price of the product: "))
sellingprice=int(input("Enter the sell price of the product: "))
profit=sellingprice - costprice 
incrasedsellingprice=1.05* profit + costprice
print("Profit from this sell :-", profit)
print("Selling price should be increase for profit of 5% :-",incrasedsellingprice)
