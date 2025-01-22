from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class  MyrootWidget(BoxLayout):
    def checkbox_checked (self, instance, value):
        # if value == True :
        #     self.ids.lbl1.text = "tercentang"
        # else :
        #     self.ids.lbl1.text = "tidak tercentang"
        if self.ids.ckbx1.active == True and self.ids.ckbx2.active == True:
            self.ids.lbl1.text = "perjelas kelamin anda"
        # if self.ids.ckbx1.active == True and self.ids.ckbx2.active == False :
        #     self.ids.lbl1.text = "kelamin anda laki laki"
        else :
            self.ids.lbl1.text = "tidak tercentang"



        


class lay_tApp(App):
    def build(self):
        return MyrootWidget()

if __name__ == "__main__":
    lay_tApp().run()