def make_html(element):
    def wrapper():
        return '<p>' + element() + '<p>'
    return wrapper


@make_html
def get_text(text='I code with PyBites'):
    return text


test = get_text()
print(test)
