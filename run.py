from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.close_login_modal()
        bot.change_currency(currency="USD")
        place = input("Where do you want to go?\n").strip()
        bot.select_place_to_go(place)
        check_in = input("Please enter the check in date(YYYY-MM-DD): ").strip()
        check_out = input("Please enter the check out date(YYYY-MM-DD): ").strip()
        bot.select_dates(check_in_date=check_in, check_out_date=check_out)
        no_adult = int(input("Number of adult: "))
        no_child = int(input("Number of children: "))
        no_room = int(input("Number of room: "))
        bot.select_room_capacity(adult=no_adult, children=no_child, room=no_room)
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh()
        print()
        print()
        bot.report_results()
except Exception as ex:
    if 'in PATH' in str(ex):
        print("There is a problem running this program from cli.")
    else:
        raise