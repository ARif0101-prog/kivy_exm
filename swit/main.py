from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class Myrootwidget(BoxLayout):
    pass

class lytApp(App):
    def build(self):
        return  Myrootwidget()

if __name__ == '__main__':
    lytApp().run()