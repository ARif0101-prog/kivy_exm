from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App

class myrootwidget(RelativeLayout):
    pass

class btnlayoutApp(App):
    def build(self):
        return myrootwidget()

if __name__ == '__main__':
	btnlayoutApp().run()