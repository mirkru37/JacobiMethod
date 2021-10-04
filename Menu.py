import Input


def get_menu_option(message=""):
    if message:
        print(message)
    return input("-->").strip()


def invalid_option(*_):
    print("Invalid choice!!")
    raise ValueError("Invalid menu option")


def menu(template, data=None, greet_message='', message_for_get=''):
    if greet_message:
        print(greet_message)
    for key in template:
        print(f"{key}: {template[key][0]}")
    option = get_menu_option(message_for_get)
    try:
        return template.get(option, [None, invalid_option])[1](data)
    except ValueError:
        return menu(template, data, greet_message, message_for_get)


def close(*_):
    exit()


input_matrix = {
    "1": ("Input", Input.matrix),
    "2": ("Exit", close)
}