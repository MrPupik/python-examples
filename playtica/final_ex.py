def show_menu(dc: dict, title: str, show_values=False):
    print(title)
    for i, k in enumerate(dc):
        if show_values:
            row = f"{k} - {dc[k]}"
        else:
            row = f"{k}"
        print(f"    {i+1}. {row}")
    print(f"    {i+2}. exit")


my_dict = {
    'phones': {
        'galaxy': 4300,
    },
    'computers': {
        'lenovi': 3500,
    },
    'accesorries':
    {
        'sunglasses': 440,
    }
}


show_menu(my_dict, "choose category:")
