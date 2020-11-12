

# NamedTuple


from typing import NamedTuple


class MenuConfig(NamedTuple):


    title: str
    body: str
    button_text: str
    cancellable: bool = False


data = MenuConfig(title='china', body=None, button_text= None, cancellable=False)
print(data)
print(data.title)



