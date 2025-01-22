from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class Inputwidget(BoxLayout):

	def btn_clk(self, txt):
		return print(txt)
		#self.add_widget(widget)
		# print(self.txt.text())
        #self.lbl.color = 
class layoutloginApp(App):
    #pass
	def build(self):
		return Inputwidget()

if __name__ == '__main__':
	layoutloginApp().run()