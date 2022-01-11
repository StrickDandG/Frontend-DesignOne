from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer,MDNavigationLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem,IconLeftWidget
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.button import MDFillRoundFlatButton,MDRoundFlatIconButton


from kivy.animation import Animation
from kivy.graphics import Ellipse
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.uix.image import Image

'''
    Date: 9-01-2022
    TODO:
        1. Add Genres to Game Navigation Drawer
        2. Try to Complete the Login Screen
        3. Brainstorm for more Ideas
'''


class ImmersiveGaming(MDApp):

    def build(self):

    # === Variables === #
        self.clock=Clock
        self.loggedin=False

    # === Window and App Configuration === #
        self.title="Immersive Gaming"
        self.theme_cls.theme_style="Light"
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

        self.loginscreen=MDScreen(name="LoginScreen")
        self.accountscreen=MDScreen(name="AccountScreen")

        self.splashscreen.add_widget(self.bootlogo)

        # === Adding Screens to Screen Manager === #
        self.screenmanager.add_widget(self.splashscreen)
        self.screenmanager.add_widget(self.homescreen)
        self.screenmanager.add_widget(self.gamescreen)
        self.screenmanager.add_widget(self.serverscreen)
        self.screenmanager.add_widget(self.settingscreen)
        self.screenmanager.add_widget(self.loginscreen)
        self.screenmanager.add_widget(self.accountscreen)

        self.navigation_layout.add_widget(self.screenmanager)

    # === ToolBar === #
        self.hometoolbar=MDToolbar(title="Home",pos_hint={"top":1})
        self.hometoolbar.left_action_items=[['menu',self.open_navigation_drawer]]
        self.hometoolbar.right_action_items=[["account",self.goto_account_or_login]]

        self.gametoolbar=MDToolbar(title="Games",pos_hint={"top":1})
        self.gametoolbar.left_action_items=[['menu',self.open_navigation_drawer]]
        self.gametoolbar.right_action_items=[['account',self.goto_account_or_login],['filter',self.open_game_genre]]


        self.servertoolbar=MDToolbar(title="Server",pos_hint={"top":1})
        self.servertoolbar.left_action_items=[['menu',self.open_navigation_drawer]]
        self.servertoolbar.right_action_items=[['account',self.goto_account_or_login]]


        self.settingstoolbar=MDToolbar(title="Settings",pos_hint={"top":1})
        self.settingstoolbar.left_action_items=[['menu',self.open_navigation_drawer]]

        self.logintoolbar=MDToolbar(title="Login",pos_hint={"top":1})
        self.logintoolbar.left_action_items=[["chevron-left",self.goto_homescreen]]

        self.accounttoolbar=MDToolbar(title="My Account",pos_hint={"top":1})
        self.accounttoolbar.left_action_items=[["chevron-left",self.account_to_homescreen],['menu',self.open_navigation_drawer]]


    # === Navigation Pannel === #

        self.navigation_bar=MDNavigationDrawer(orientation='vertical')
        self.navigation_layout.add_widget(self.navigation_bar)

        self.navigation_boxlayout=MDBoxLayout(spacing='8dp',padding='8dp',orientation='vertical')
        self.navigation_bar.add_widget(self.navigation_boxlayout)

        self.scrollview=ScrollView()
        self.navigation_bar.add_widget(self.scrollview)

        self.pagename_label=MDLabel(font_style="H5",halign="center")
        self.navigation_boxlayout.add_widget(self.pagename_label)

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

    # === Game Genre Panel === #

        self.gamegenre_bar=MDNavigationDrawer(orientation="vertical")

        self.gamegenre_boxlayout=MDBoxLayout(spacing='8dp',padding='8dp',orientation='vertical')
        self.gamegenre_bar.add_widget(self.gamegenre_boxlayout)

        self.gamebarscrollview=ScrollView()
        self.gamegenre_bar.add_widget(self.gamebarscrollview)

        self.genre_label=MDLabel(text="Genre and Categories",font_style="H5",halign="center")
        self.gamegenre_boxlayout.add_widget(self.genre_label)

        self.navigation_layout.add_widget(self.gamegenre_bar)

    # === Login Card === #
        self.login_card=MDCard(elevation=20,size_hint=(None,None),size=(500,500),pos_hint={"center_x":0.5,"center_y":0.45})

        self.login_boxlayout=MDBoxLayout(orientation="vertical",spacing=10,padding=10)

        self.login_label=MDLabel(text="Login",font_style="H2",halign="center",pos_hint={"center_x":0.5},font_size=15)
        self.login_boxlayout.add_widget(self.login_label)

        self.username_textfield=MDTextFieldRect(hint_text="Enter Your Username",size_hint=(0.8,0.2),pos_hint={"center_x":0.5},font_size=20)
        self.login_boxlayout.add_widget(self.username_textfield)

        self.password_textfield=MDTextFieldRect(hint_text="Enter Your Password",size_hint=(0.8,0.2),pos_hint={"center_x":0.5},font_size=20,password=True)
        self.login_boxlayout.add_widget(self.password_textfield)

        self.login_buttons_boxlayout=MDBoxLayout(orientation='vertical',spacing=10,padding=10)

        self.login_button=MDFillRoundFlatButton(text="Login",size_hint=(0.6,None),pos_hint={"center_x":0.5})
        self.login_buttons_boxlayout.add_widget(self.login_button)

        self.singup_button=MDFillRoundFlatButton(text="Sign Up",size_hint=(0.6,None),pos_hint={"center_x":0.5})
        self.login_buttons_boxlayout.add_widget(self.singup_button)

        self.clear_button=MDFillRoundFlatButton(text="Clear",size_hint=(0.6,None),pos_hint={"center_x":0.5})
        self.login_buttons_boxlayout.add_widget(self.clear_button)

        self.login_boxlayout.add_widget(self.login_buttons_boxlayout)

        self.login_card.add_widget(self.login_boxlayout)
        

    # ===Screen Contents === #
        # === Home Screen Content === #
        self.homescreen.add_widget(self.hometoolbar)

        # === Game Screen Content === #
        self.gamescreen.add_widget(self.gametoolbar)

        # === Server Screen Content === #
        self.serverscreen.add_widget(self.servertoolbar)

        # === Settings Screen Content === #
        self.settingscreen.add_widget(self.settingstoolbar)

        # === Login Screen Content === #
        self.loginscreen.add_widget(self.logintoolbar)
        self.loginscreen.add_widget(self.login_card)

        # === Account Screen Content === #
        self.accountscreen.add_widget(self.accounttoolbar)

    # === Return Screen and Clock for Boot Screen Transition === #

        self.clock.schedule_once(self.stop_splash,timeout=5)

        return self.navigation_layout


    # Used to transition from spash screen to Home Screen
    def stop_splash(self,*args):
        self.screenmanager.current="HomeScreen"
        self.pagename_label.text="Home"


    # Used to open Navigation Bar when the menu is click or it is dragged
    def open_navigation_drawer(self,*args):
        self.navigation_bar.set_state("open")


    # A Function that is used to goto home screen from the navigation bar
    def goto_homescreen(self,*args):
        self.screenmanager.current="HomeScreen"
        self.screenmanager.transition.direction="left"
        self.pagename_label.text="Home"
        self.navigation_bar.set_state("close")


    # A Function that is used to goto game screen from the navigation bar
    def goto_gamescreen(self,*args):
        self.screenmanager.current="GameScreen"
        self.screenmanager.transition.direction="left"
        self.pagename_label.text="Games"
        self.navigation_bar.set_state("close")


   # A Function that is used to goto server screen from the navigation bar    
    def goto_serverscreen(self,*args):
        self.screenmanager.current="ServerScreen"
        self.screenmanager.transition.direction="left"
        self.pagename_label.text="Servers"
        self.navigation_bar.set_state("close")


    # A Function that is used to goto home screen from the navigation bar
    def goto_settingscreen(self,*args):
        self.screenmanager.current="SettingsScreen"
        self.screenmanager.transition.direction="left"
        self.pagename_label.text="Settings"
        self.navigation_bar.set_state("close")


    # A Function that is used to goto account screen or login screen if user is not logged in
    def goto_account_or_login(self,*args):
        if self.loggedin==False:
            self.screenmanager.current="LoginScreen"
            self.screenmanager.transition.direction="left"
            self.loggedin=True

        else:
            self.screenmanager.current="AccountScreen"
            self.screenmanager.transition.direction="left"


    # A Function that opens the games genre
    def open_game_genre(self,*args):
        self.gamegenre_bar.set_state("open")

    
    # A Function that is used to transition from account screen to home screen.
    def account_to_homescreen(self,*args):
        self.screenmanager.current="HomeScreen"
        self.screenmanager.transition.direction="right"
        
        

if __name__ == "__main__":
    app=ImmersiveGaming()
    app.run()