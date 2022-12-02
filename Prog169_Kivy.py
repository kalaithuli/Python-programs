from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.add_widget(Image(source="kk.jpg"))
        #self.greeting = Label(text="whats your name?")
        #self.window.add_widget(self.greeting)
        return self.window
if __name__ =="__main__":
    SayHello().run()
