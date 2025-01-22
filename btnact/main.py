# from kivy.app import App
# from kivy.factory import Factory


# class KvDemoApp(App):
#     def build(self):
#         my_widget = Factory.MyWidget()
#         return my_widget


# if __name__ == '__main__':
#     KvDemoApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyWidget (BoxLayout):
    pass
    # def btn_clk(self):
    #     self.label_widget.text="text ganti"

class  KvDemoApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
     KvDemoApp().run()