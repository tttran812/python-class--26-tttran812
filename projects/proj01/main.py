# Starting file for PROJECT 1
# Include your course number, student first and last name, and date in the comment header
# CS 31 - 72473, Trang Tran, October 24, 2026

#Beyond the Map Travel Consulting
#Sales Program Prototype

print("********************************************")
print("Welcome to Beyond the Map Travel Consulting!")
print("********************************************")

first_name = input("Enter your first name: ")
print(f"Hello, {first_name}!")

learn_more = input("Would you like to learn more about our services? (y/n):")

if learn_more.lower() == "y":
    print("""
    Welcome to Beyond the Map Travel Consulting!
    
    Dreaming of your next adventure but not sure
    where to start? We are here to help!
    
    Our Personalized Travel Itinerary service
    takes the stress out of planning your trip.
    We create customized travel schedules with 
    sighseeing recommendations, fun activities,
    and restaurant suggestions to help you make
    most of your vacation.
    
    Whether you dream of relaxing on a tropical
    beach, exploring a new city, or discovering
    beautiful national parks, we help turn your
    travel dreams into unforgettable memories!
    
    Let us help you plan your next adventure!
    """)
    
    purchase = input("Would you like to purchase a travel itinerary? (y/n): ")

    if purchase.lower() == "y":

        #Collect customer information
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        email = input("Please enter your email address: ")
        phone = input("Please enter your phone number: ")

        #Calculate purchase cost
        price = 179.00

        print(f"\nOur Personalized Travel Itinerary costs ${price:.2f}.")
        quantity = int(
            input("How many travel itineraries would you like to purchase? "))

        subtotal = quantity * price
        tax = subtotal * 0.10
        total = subtotal + tax

        # Display receipt
        print("\n========================================")
        print("    BEYOND THE MAP TRAVEL CONSULTING")
        print("           SALES RECEIPT")
        print("========================================")
        print(f"Customer: {first_name} {last_name}")
        print(f"Email:    {email}")
        print(f"Phone:    {phone}")
        print("----------------------------------------")
        print("Product: Personalized Travel Itinerary")
        print(f"Quantity: {quantity}")
        print(f"Price per itinerary: ${price:.2f}")
        print("----------------------------------------")
        print(f"Subtotal:         ${subtotal:.2f}")
        print(f"Sales Tax (10%):  ${tax:.2f}")
        print(f"TOTAL DUE:        ${total:.2f}")
        print("========================================")
        print("Thank you for choosing Beyond the Map!")
        print("Your next adventure awaits!")
        print("Have a wonderful day!")

    else:
        print("\nThank you for considering Beyond the Map!")
        print("We hope to help you plan your next adventure.")
        print("Have a wonderful day!")

else:
    print("\nThank you for visiting Beyond the Map Travel Consulting!")
    print("We hope you have a wonderful day!")








