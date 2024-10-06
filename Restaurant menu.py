# Functions
def order_processor(order_list_facture, bill, category_order, user_order):
    """in tabe darkhast moshtari ra daryaft va pardazesh mikonad """
    user_order = input(
        f"\nIf you don't want to chose order, please type (skip).\nIf you wanna see menu again, please type (menu).\n"
        f"If you wanna see your facture, please type (facture).\nIf you wanna quit, please type (quit).\n\n"
        f"Please choose your order with number between 1-{len(orders_menu[category_order])}: "
    )

    if user_order.isdecimal():
        user_order = int(user_order)
    elif user_order.isalpha():
        user_order = user_order.casefold()
        user_order = user_order.capitalize()

    if type(user_order) == int:
        single_order = user_order
        order_list_facture, bill = facture_maker(order_list_facture, bill, category_order, single_order)
    elif user_order.isalpha() == False:
        for single_order in user_order:
            if single_order.isdecimal():
                single_order = int(single_order)
                order_list_facture, bill = facture_maker(order_list_facture, bill, category_order, single_order)
            else:
                continue
    elif user_order == "menu":
        # Menu
        print(
            "Menu is: \n--Food--           --Drink--\n1-Big mac (25$)    1-Cola - (2$)\n2-Hot dog (30$)    "
            "2-Water - (1.5$)\n3-Pizza (50$)      3-Coffee - (2.5$)\n4-Burger (15$)     4-McDonald's Drink - (5$)\n"
            "5-Bandary (9$)      5-Tea (2.5$)")
    elif user_order == "Skip":
        print("You skip it.")
    elif user_order == "Facture":
        print(f"Your facture\n*Your orders: {order_list_facture}\n*Your bill: {round(bill)}$")
    elif user_order == "Quit":
        print(f"Your facture\n*Your orders: {order_list_facture}\n*Your bill: {round(bill)}$\nHope to meet again. :)")
        quit()
    else:
        print("Wrong answer")

    return order_list_facture, bill


def facture_maker(order_list_facture, bill, category_order, single_order):
    """ezafeh kardan sefaresh moshtary dar facture"""
    if single_order in range(1, len(orders_menu[category_order]) + 1):
        order_name = f"\n   +{orders_menu[category_order][single_order - 1]}"
        order_price = orders_price[category_order][single_order - 1]
        order_list_facture += order_name
        bill += order_price
        print(f"*You chose: {order_name}")
    else:
        print(f"{single_order} is not in menu")

    return order_list_facture, bill


# Program
orders_menu, orders_price = ([
                                 # Orders menu
                                 ["Big mac - (25$)", "Hot dog - (30$)", "Pizza - (50$)", "Burger - (15$)",
                                  "Bandary (9$)"],
                                 ["Cola - (2$)", "Water - (1.5$)", "Coffee - (2.5$)", "McDonald's Drink - (5$)"]],
                             # Orders price
                             [[25, 30, 50, 15], [2, 1.5, 2.5, 5]])

# Menu
user_order, order_list_facture, bill = "", "", 0.0

print(
    "Menu is: \n--Food--           --Drink--\n1-Big mac (25$)    1-Cola - (2$)\n2-Hot dog (30$)    "
    "2-Water - (1.5$)\n3-Pizza (50$)      3-Coffee - (2.5$)\n4-Burger (15$)     4-McDonald's Drink - (5$)\n"
    "5-Bandary (9$)      5-Tea (2.5$)")

while user_order != "Quit":
    # Food order
    order_list_facture, bill = order_processor(order_list_facture, bill, 0, "")

    # Drink order
    order_list_facture, bill = order_processor(order_list_facture, bill, 1, "")
