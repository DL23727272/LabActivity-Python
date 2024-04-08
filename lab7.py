from kivy.lang import Builder

from kivymd.app import MDApp

class Nav(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('lab7.kv')

Nav().run()