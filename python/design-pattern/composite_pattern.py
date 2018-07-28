"""
What is this pattern about?
The composite pattern describes a group of objects that is treated the
same way as a single instance of the same type of object. The intent of
a composite is to "compose" objects into tree structures to represent
part-whole hierarchies. Implementing the composite pattern lets clients
treat individual objects and compositions uniformly.
"""


class MenuComponent():
    def __init__(self, text):
        self.text = text

    def render(self, prefix):
        print("{} {}".format(prefix, self.text))


class Menu(MenuComponent):
    def __init__(self, text):
        self.components = []
        super().__init__(text)

    def render(self, prefix):
        super().render(prefix)
        prefix += "  "
        for component in self.components:
            component.render(prefix)

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)


class MenuItem(MenuComponent):
    def __init__(self, text):
        super().__init__(text)

    def render(self, prefix):
        super().render(prefix)

# Client
if __name__ == '__main__':
    menuitem1 = MenuItem("New File")
    menuitem2 = MenuItem("Open")
    menuitem3 = MenuItem("Save")
    menuitem4 = MenuItem("Exit")
    menuitem5 = MenuItem("Copy")
    menuitem6 = MenuItem("Paste")

    component1 = Menu("File")
    component2 = Menu("Edit")

    component1.add(menuitem1)
    component1.add(menuitem2)
    component1.add(menuitem3)
    component1.add(menuitem4)
    component2.add(menuitem5)
    component2.add(menuitem6)

    menu = Menu("Menu Bar")

    menu.add(component1)
    menu.add(component2)

    menu.render("")
