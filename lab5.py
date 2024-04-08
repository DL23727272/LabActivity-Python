from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable


class Table(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        layout = AnchorLayout()

        column_data = [
            ("No.", dp(30)),
            ("Status", dp(30)),
            ("Network Provider", dp(40), self.sort_on_col_3),
        ]

        row_data = [
            (
                "1",
                ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                "Globe",
            ),
            (
                "2",
                (
                    "checkbox-marked-circle",
                    [39 / 256, 174 / 256, 96 / 256, 1], 
                    "Online"
                ),
                "Dito",
            ),
        ]

        data_tables = MDDataTable(
            size_hint=(0.7, 0.5),
            column_data=column_data,
            row_data=row_data,
        )

        layout.add_widget(data_tables)
        return layout

    def sort_on_col_3(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][2]  #to access the two dimensional array (columnf and row data)
            )
        )

Table().run()
