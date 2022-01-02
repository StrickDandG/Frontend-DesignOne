from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer,MDNavigationLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem,IconLeftWidget


from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.uix.image import Image


class ImmersiveGaming(MDApp):

    def build(self):

    # === Variables === #
        self.clock=Clock

        self.title="Immersive Gaming"
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="DeepPurple"

        self.navigation_layout=MDNavigationLayout()

        self.bootlogo=Image(source="img\\boot_logo.png",pos_hint={"center_x":.5,"center_y":.5},size_hint=(.5,.5))

    # === Screens and Screen Manager === #
        self.screenmanager=ScreenManager()

        self.splashscreen=MDScreen(name="SplashScreen")
        self.homescreen=MDScreen(name="HomeScreen")
        self.gamescreen=MDScreen(name="GameScreen")
        self.serverscreen=MDScreen(name="ServerScreen")
        self.settingscreen=MDScreen(name="SettingsScreen")

        self.splashscreen.add_widget(self.bootlogo)

        # === Adding Screens to Screen Manager === #
        self.screenmanager.add_widget(self.splashscreen)
        self.screenmanager.add_widget(self.homescreen)
        self.screenmanager.add_widget(self.gamescreen)
        self.screenmanager.add_widget(self.serverscreen)
        self.screenmanager.add_widget(self.settingscreen)

        self.navigation_layout.add_widget(self.screenmanager)





    # === ToolBar === #
        self.hometoolbar=MDToolbar(title="Home",pos_hint={"top":1})
        self.hometoolbar.left_action_items=[['menu',self.open_navigation_drawer]]
        self.gametoolbar=MDToolbar(title="Games",pos_hint={"top":1})
        self.gametoolbar.left_action_items=[['menu',self.open_navigation_drawer]]
        self.servertoolbar=MDToolbar(title="Server",pos_hint={"top":1})
        self.servertoolbar.left_action_items=[['menu',self.open_navigation_drawer]]
        self.settingstoolbar=MDToolbar(title="Settings",pos_hint={"top":1})
        self.settingstoolbar.left_action_items=[['menu',self.open_navigation_drawer]]
        # self.navigation_layout.add_widget(self.toolbar)
        # === Home Screen Content === #
        self.homescreen.add_widget(self.hometoolbar)
        # === Game Screen Content === #
        self.gamescreen.add_widget(self.gametoolbar)
        # === Server Screen Content === #
        self.serverscreen.add_widget(self.servertoolbar)
        # === Settings Screen Content === #
        self.settingscreen.add_widget(self.settingstoolbar)

    # === Navigation Pannel === #

        self.navigation_bar=MDNavigationDrawer(orientation='vertical')
        self.navigation_layout.add_widget(self.navigation_bar)

        self.navigation_boxlayout=MDBoxLayout(spacing='8dp',padding='8dp',orientation='vertical')
        self.navigation_bar.add_widget(self.navigation_boxlayout)

        self.scrollview=ScrollView()
        self.navigation_bar.add_widget(self.scrollview)

        self.home_icon=IconLeftWidget(icon="home",on_release=self.goto_homescreen)
        self.home_tab=OneLineIconListItem(text="Home",text_color=self.theme_cls.primary_color,on_release=self.goto_homescreen)
        
        self.home_tab.add_widget(self.home_icon)
        self.navigation_boxlayout.add_widget(self.home_tab)

        self.game_icon=IconLeftWidget(icon="gamepad",on_release=self.goto_gamescreen)
        self.game_tab=OneLineIconListItem(text="Games",text_color=self.theme_cls.primary_color,on_release=self.goto_gamescreen)
        
        self.game_tab.add_widget(self.game_icon)
        self.navigation_boxlayout.add_widget(self.game_tab)

        self.server_icon=IconLeftWidget(icon="desktop-mac",on_release=self.goto_serverscreen)
        self.server_tab=OneLineIconListItem(text="Servers",text_color=self.theme_cls.primary_color,on_release=self.goto_serverscreen)
        
        self.server_tab.add_widget(self.server_icon)
        self.navigation_boxlayout.add_widget(self.server_tab)

        self.settings_icon=IconLeftWidget(icon="ruler",on_release=self.goto_settingscreen)
        self.settings_tab=OneLineIconListItem(text="Settings",text_color=self.theme_cls.primary_color,on_release=self.goto_settingscreen)
        
        self.settings_tab.add_widget(self.settings_icon)
        self.navigation_boxlayout.add_widget(self.settings_tab)

        self.clock.schedule_once(self.stop_splash,timeout=5)

        return self.navigation_layout

    def stop_splash(self,*args):
        self.screenmanager.current="HomeScreen"

    def open_navigation_drawer(self,*args):
        self.navigation_bar.set_state("open")

    def goto_homescreen(self,*args):
        self.screenmanager.current="HomeScreen"
        self.navigation_bar.set_state("close")

    def goto_gamescreen(self,*args):
        self.screenmanager.current="GameScreen"
        self.navigation_bar.set_state("close")

    def goto_serverscreen(self,*args):
        self.screenmanager.current="ServerScreen"
        self.navigation_bar.set_state("close")

    def goto_settingscreen(self,*args):
        self.screenmanager.current="SettingsScreen"
        self.navigation_bar.set_state("close")

        
        



if __name__ == "__main__":
    app=ImmersiveGaming()
    app.run()