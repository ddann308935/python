# Choose between pizza size: S M L or X
# Display prices for each size

user_size = input("Please choose from following for the size of pizza: S, M, L, or X: ")

pizza_size = ['S', 'M', 'L', 'X']
price = ["$6.99", "$8.99", "$12.50", "$15.00"]

if user_size in pizza_size and pizza_size != 0:
    index = pizza_size.index(user_size)
    print(f"The {user_size} size pizza is {price[index]}")
else:
    print("Error. Please try again.")
        




    
    
    
    
    
    
    

        



