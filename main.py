import requests
import flet as ft
import deepl
from requests import RequestException, options


def get_categories():
    try:
        response = requests.get("https://v2.jokeapi.dev/categories")
        data = response.json()
        categories = data.get("categories", [])
        return categories
    except RequestException:
        print("Hata oluştu")
        return []

def get_blackflags():
    try:
        response = requests.get("https://v2.jokeapi.dev/flags")
        data = response.json()
        blackflags = data.get("flags", [])
        return blackflags
    except RequestException:
        print("Hata oluştu")
        return []


def main(page: ft.Page):

    # Page Properties
    page.title = ""
    page.window.height = 720
    page.window.width = 1160
    page.window.min_height = 720
    page.window.min_width = 1160
    page.window.max_height = 720
    page.window.max_width = 1160

    page.window.alignment = ft.alignment.center
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = True

    def generate(e):
        selected_categories = categories_combobox.value
        selected_blackflags = blackflags_combobox.value

        selected_type = types_combobox.value
        selected_language = ["English","Turkish"][language_list.selected_index]

        auth_key = "562c3841-0617-447a-94ea-d066420c62ce:fx"
        deepl_client = deepl.DeepLClient(auth_key)

        url =(f"https://v2.jokeapi.dev/joke/{selected_categories}?blacklistFlags={selected_blackflags}&type={selected_type}")
        response = requests.get(url)
        data = response.json()

        print("API cevabı:", data)
        print("İstek Atılan:", url)


        if data.get("error", False):
            joke_label.value = "Hata oluştu"
            joke_label2.value = ""
            page.update()
            return

        if selected_language == "Turkish":
            if selected_type == "single":
                result = deepl_client.translate_text(data["joke"], target_lang="TR")
                joke_label.value = result
                joke_label2.value = ""
                page.update()
            elif selected_type == "twopart":
                translated_setup = deepl_client.translate_text(data["setup"], target_lang="TR")
                translated_delivery = deepl_client.translate_text(data["delivery"], target_lang="TR")
                joke_label.value = translated_setup
                joke_label2.value = translated_delivery
                page.update()
        elif selected_language == "English":
            if selected_type == "single":
                joke_label.value = data["joke"]
                joke_label2.value = ""
                page.update()
            elif selected_type == "twopart":
                joke_label.value = data["setup"]
                joke_label2.value = data["delivery"]
                page.update()

    def change_theme(e):
        selected_index = int(e.data)
        if selected_index == 0:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    def change_lang(e):
        selected_index = int(e.data)
        if selected_index == 0:
            categories_label.value = "Categories"
            blackflags_label.value = "Blackflags"
            types_label.value = "Types"

            btn.content.controls[2].value= "Generate A Joke"
            btn.content.spacing = 14

            language_list.controls[0].value = "English"
            language_list.controls[1].value = "Turkish"

            theme_mode.controls[0].value = "Light Mode"
            theme_mode.controls[1].value = "Dark Mode"


            categories_combobox.options = [ft.dropdown.Option(text=c, key=c) for c in categories]
            blackflags_combobox.options = [ft.dropdown.Option(text=b, key=b) for b in blackflags]
            types_combobox.options = [ft.dropdown.Option(text=t, key=t) for t in ["single", "twopart"]]

        else:
            categories_label.value = "Kategoriler"
            blackflags_label.value = "Yasaklı Konular"
            types_label.value = "Şaka Tipi"

            btn.content.controls[2].value= "Şaka Yap"
            btn.content.spacing = 25

            language_list.controls[0].value = "İngilizce"
            language_list.controls[1].value = "Türkçe"

            theme_mode.controls[0].value = "Aydınlık Mod"
            theme_mode.controls[1].value = "Karanlık Mod"

            categories_combobox.options = [
                ft.dropdown.Option(text=category_map.get(c, c), key=c) for c in categories
            ]
            blackflags_combobox.options = [
                ft.dropdown.Option(text=blackflags_map.get(c, c), key=c) for c in blackflags
            ]
            types_combobox.options = [
                ft.dropdown.Option(text=types_map.get(c, c), key=c) for c in ["single", "twopart"]
            ]

        theme_mode.update()
        btn.content.update()
        page.update()



    btn = ft.ElevatedButton(content=ft.Row(
            [
                ft.Icon(ft.Icons.ADD_ROUNDED, size=20),
                ft.Container(width=10),
                ft.Text("Generate A Joke")
            ],
        alignment=ft.MainAxisAlignment.START,
        spacing=14
        ),
        width= 225,
        height=40,
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
        on_click=generate
    )


    category_map = {
        "Any": "Herhangi",
        "Misc": "Çeşitli",
        "Programming": "Yazılım",
        "Dark": "Kara Mizah",
        "Pun": "Kelime Oyunu",
        "Spooky": "Korkutucu",
        "Christmas": "Noel"

    }

    blackflags_map = {
        "nsfw": "Müstehcen",
        "religious": "Dini",
        "political": "Politik",
        "racist": "Irkçı",
        "sexist": "Cinsiyetçi",
        "explicit": "Açık içerik"
    }

    types_map ={
        "single": "Tek Cümle",
        "twopart": "Soru-Cevap"
    }
    # Text
    joke_label = ft.Text("")
    joke_label2 = ft.Text("")
    categories_label = ft.Text("Categories")
    blackflags_label = ft.Text("Blackflags")
    types_label = ft.Text("Types")

    # Page List
    categories_combobox = ft.Dropdown(
        border_radius=10,
        editable=False,
        hint_text="Category",
        width=180,
        border_width=0.5,
    )

    blackflags_combobox = ft.Dropdown(
        border_radius=10,
        editable=False,
        hint_text="Blackflags",
        width=180,
        border_width=0.5,
    )

    types_combobox = ft.Dropdown(
        border_radius=10,
        editable=False,
        hint_text="Types",
        width=180,
        border_width=0.5,
    )

    language_list = ft.CupertinoSlidingSegmentedButton(
            selected_index=0,
            thumb_color=ft.Colors.BLUE_400,
            on_change=lambda e: change_lang(e),
            padding=ft.padding.symmetric(0, 10),
            controls=[
                ft.Text("English"),
                ft.Text("Turkish"),
            ],
        )

    theme_mode = ft.CupertinoSlidingSegmentedButton(
            selected_index=0,
            thumb_color=ft.Colors.BLUE_400,
            on_change=lambda e: change_theme(e),
            padding=ft.padding.symmetric(0, 10),
            controls=[
                ft.Text("Light Mode"),
                ft.Text("Dark Mode"),
            ],
        )


    # Pages
    page.add(
        ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            [
                                ft.WindowDragArea(
                                    ft.Container(padding=10),
                                    expand=True
                                ),
                                ft.IconButton(
                                    ft.Icons.CLOSE_SHARP,
                                    on_click=lambda _: page.window.close(),
                                )
                            ]
                        ),
                        ft.Row([categories_label], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([ft.Container(content=categories_combobox, margin=5)],
                               alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([blackflags_label], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([ft.Container(content=blackflags_combobox, margin=5)],
                               alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([types_label], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([ft.Container(content=types_combobox, margin=5)], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([ft.Container(content=btn, margin=20)], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([joke_label], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([joke_label2], alignment=ft.MainAxisAlignment.CENTER),
                    ],
                    expand=True
                    ),

                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(content=language_list, expand=True, alignment=ft.alignment.bottom_left),
                            ft.Container(content=theme_mode, expand=True, alignment=ft.alignment.bottom_right),
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.END,
                    ),
                    height=60
                )
            ],
            expand=True
        )
    )

    categories = get_categories()
    if categories:
        categories_combobox.options = [ft.dropdown.Option(text=c) for c in categories]
        categories_combobox.value = categories[0]
        categories_combobox.update()

    blackflags = get_blackflags()
    if blackflags:
        blackflags_combobox.options = [ft.dropdown.Option(text=b) for b in blackflags]
        blackflags_combobox.value = blackflags[0]
        blackflags_combobox.update()

    types_combobox.options = [
        ft.dropdown.Option("single", "single"),
        ft.dropdown.Option("twopart", "twopart")
    ]
    types_combobox.value = "single"


    page.update()

ft.app(main)