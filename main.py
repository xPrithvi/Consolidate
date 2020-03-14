"""Dependencies."""
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
import ConsolidateWallpaper

class ConsolidateApp(MDApp):
    """KivyMD framework is inherited by our Application class."""

    def build(self):
        """The application layout is loaded from the main.kv file."""
        return Builder.load_file("main.kv")

    def openScreen(self, itemdrawer):
        self.openScreenName(itemdrawer.target)
        self.root.ids.nav_drawer.set_state("close")

    def openScreenName(self, screenName):
        self.root.ids.screen_manager.current = screenName

    def on_start(self):
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(target="HomeScreen", text="Home",
                       icon="home-circle-outline",
                       on_release=self.openScreen))
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(target="MoodScreen", text="Mood Tracker",
                       icon="sticker-emoji",
                       on_release=self.openScreen))
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(target="SleepScreen", text="Sleep Tracker",
                       icon="bell-ring",
                       on_release=self.openScreen))
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(target="JournalScreen", text="My Journal",
                       icon="notebook",
                       on_release=self.openScreen))
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(target="PersonalityScreen", text="My Personality",
                       icon="weather-sunny",
                       on_release=self.openScreen))
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(target="TestsScreen", text="Depression & Anxiety",
                       icon="weather-lightning-rainy",
                       on_release=self.openScreen))
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(target="InfoScreen", text="Info",
                       icon="information",
                       on_release=self.openScreen))
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(target="SettingsScreen", text="Settings",
                       icon="settings-outline",
                       on_release=self.openScreen))

class ContentNavigationDrawer(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    target = StringProperty()

class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when the menu item is clicked."""

        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

"Algorithm execution."
if __name__ == "__main__":
    ConsolidateWallpaper.Wallpaper().select_wallpaper()
    ConsolidateApp().run()
