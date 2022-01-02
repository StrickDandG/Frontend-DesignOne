from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer,MDNavigationLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem,IconLeftWidget




from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView


class ImmersiveGaming(MDApp):

    def build(self):

    # === Variables === #
        self.navigation_open=0

        self.title="Immersive Gaming"
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette="DeepPurple"

        self.navigation_layout=MDNavigationLayout()

        # Adding Scroll View


    # === Screens and Screen Manager === #
        self.screenmanager=ScreenManager()

        self.homescreen=MDScreen(name="HomeScreen")
        self.gamescreen=MDScreen(name="GameScreen")
        self.serverscreen=MDScreen(name="ServerScreen")
        self.settingscreen=MDScreen(name="SettingsScreen")


        # === Home Screen Content === #
        # self.homescreen.add_widget(self.toolbar)
        # === Game Screen Content === #
        # === Server Screen Content === #
        # === Settings Screen Content === #

        # === Adding Screens to Screen Manager === #
        self.screenmanager.add_widget(self.homescreen)
        self.screenmanager.add_widget(self.gamescreen)
        self.screenmanager.add_widget(self.serverscreen)
        self.screenmanager.add_widget(self.settingscreen)

        self.navigation_layout.add_widget(self.screenmanager)





    # === ToolBar === #
        self.toolbar=MDToolbar(title="Home",pos_hint={"top":1})
        self.toolbar.left_action_items=[['menu',self.open_navigation_drawer]]
        self.navigation_layout.add_widget(self.toolbar)

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

        return self.navigation_layout

        
    def open_navigation_drawer(self,*args):
        self.navigation_bar.set_state("open")

    def goto_homescreen(self,*args):
        self.screenmanager.current="HomeScreen"
        self.toolbar.title="Home"
        self.navigation_bar.set_state("close")

    def goto_gamescreen(self,*args):
        self.screenmanager.current="GameScreen"
        self.toolbar.title="Games"
        self.navigation_bar.set_state("close")

    def goto_serverscreen(self,*args):
        self.screenmanager.current="ServerScreen"
        self.toolbar.title="Servers"
        self.navigation_bar.set_state("close")

    def goto_settingscreen(self,*args):
        self.screenmanager.current="SettingsScreen"
        self.toolbar.title="Settings"
        self.navigation_bar.set_state("close")

        
        



if __name__ == "__main__":
    app=ImmersiveGaming()
    app.run()