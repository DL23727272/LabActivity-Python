from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
Screen:

    ScrollView:

        MDList:

            OneLineAvatarListItem:
                text: "Github"
                on_release: print('github gods')

                IconLeftWidget:
                    icon: "github"
'''

class IconApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

IconApp().run()
