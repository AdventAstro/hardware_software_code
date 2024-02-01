def menu_display():
    menu_dict = {
        '1': 'decimal_to_binary',
        '2': 'binary_to_decimal',
        'X': 'exit_program'
    }
    return menu_dict

def main():
    sel, choice = execute_display(menu_display())
    print("You selected {} and want to convert {}".format(sel, choice))

if __name__ == "__main__":
    main()
