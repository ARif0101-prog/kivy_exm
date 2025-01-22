# import kivy module
import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.widget import Widget
from kivy.core.window import Window
Window.size = (700, 150)
class MyrootWidget(BoxLayout):

	def val_in(self):
		self.ids.lbl2.text= str(self.ids.txtin.text)+", hehe"
		
class layouthintApp(App):

	def build(self):
		return MyrootWidget()

myApp = layouthintApp()

if __name__ == '__main__':
    myApp.run()