
#from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class RootWidget(BoxLayout):
    pass

class ifaceApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
	ifaceApp().run()
    