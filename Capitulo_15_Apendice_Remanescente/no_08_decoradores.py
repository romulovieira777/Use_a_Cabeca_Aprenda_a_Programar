def paragraph(func):
    def add_markup():
        return '<p>' + func() + '</p>'
    return add_markup


@paragraph
def get_text():
    return 'hello head firsr reader!'


print(get_text())
