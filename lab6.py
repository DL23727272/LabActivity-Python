from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Toolbar"

    MDLabel:
        text: "Content"
        halign: "center"
'''


class Toolbar(MDApp):
    def build(self):
        return Builder.load_string(KV)


Toolbar().run()