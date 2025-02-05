from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

KV = '''
MDScrollView:

    MDList:
        id: container
'''


class List(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(5):
            self.root.ids.container.add_widget(
                OneLineListItem(text=f"Item {i}")
            )

List().run()