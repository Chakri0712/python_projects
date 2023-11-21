from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def search_image(self):
        query = self.manager.current_screen.ids.user_query.text
        try:
            page = wikipedia.page(query, auto_suggest=False)
            option = page.links[0]
            page = wikipedia.page(option, auto_suggest=False)

            link = page.images[0]
            req = requests.get(link)
            with open('photos/image.jpg', 'wb') as file:
                file.write(req.content)
            self.manager.current_screen.ids.img.source = 'photos/image.jpg'
        except wikipedia.exceptions.HTTPTimeoutError:
            print("Wikipedia request timed out. Please try again later.")
        except wikipedia.exceptions.PageError:
            print(f"No Wikipedia page found for {query}.")


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
