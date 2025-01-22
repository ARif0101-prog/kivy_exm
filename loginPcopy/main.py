# import kivy module
import kivy

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# BoxLayout arranges children
# in a vertical or horizontal box.
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.screenmanager import ScreenManager, Screen

# class in which we are defining action on click
class RootWidget(BoxLayout):
	# def textInput(self, widget):
	# 	self.txt = widget.text

	def btn_clk(self, txt):
		# self.lbl.color = '#ffffA'
		# self.lbl.font_size = '50sp'
        #self.lbl.color = 
		
		return print(txt)


# creating action class and calling
# Rootwidget by returning it
class layoutloginApp(App):

	def build(self):
		return RootWidget()

# creating the myApp root for ActionApp() class
myApp = layoutloginApp()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
myApp.run()
