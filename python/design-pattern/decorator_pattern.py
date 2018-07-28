class WindowInterface(object):
    def build(self):
        pass


class AbstractWindowDecorator(WindowInterface):
    """
    Maintain a reference to a Window object and define an interface that
    comforms to Window's interface.
    """

    def __init__(self, window):
        self._window = window

    def build(self):
        pass


class Window(WindowInterface):
    def build(self):
        print('Building window')


class BorderDecorator(AbstractWindowDecorator):
    def add_border(self):
        print('Adding border')

    def build(self):
        self.add_border()
        self._window.build()


class VerticalSBDecorator(AbstractWindowDecorator):
    def add_vertical_scroll_bar(self):
        print('Adding vertical scroll bar.')

    def build(self):
        self.add_vertical_scroll_bar()
        self._window.build()


class HorizontalSBDecorator(AbstractWindowDecorator):
    def add_horizontal_scroll_bar(self):
        print('Adding horizontal scroll bar.')

    def build(self):
        self.add_horizontal_scroll_bar()
        self._window.build()


if __name__ == '__main__':
    w = Window()
    w.build()
    print ("=" * 50)
    wb = BorderDecorator(w)
    wb.build()
    print ("=" * 50)
    wh = HorizontalSBDecorator(w)
    wh.build()
    print ("=" * 50)
    wv = VerticalSBDecorator(w)
    wv.build()
    print ("=" * 50)
    whv = VerticalSBDecorator(wh)
    whv.build()
    print ("=" * 50)
    allw = BorderDecorator(whv)
    allw.build()
