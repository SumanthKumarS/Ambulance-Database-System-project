import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.picker import MDDatePicker
from kivy.uix.image import Image
kivy.require('1.9.0')
from kivy.uix.image import Image

helpstr = '''
ScreenManager:
    WelcomeScreen:
    UsernameScreen:
    AmbulanceScreen:
    UserLoginScreen:

<WelcomeScreen>:
    name:'welcomescreen'
    Image:
        source:'amb.jpg'
        size_hint: self.image_ratio, 1
        keep_ratio: False
        allow_stretch: True
        canvas.before:
            Color:
                rgb: 1,1,1
            Rectangle:
                size: self.size
                pos: self.pos
    MDLabel:
        text:'Health Help Secure'
        font_style: 'H2'
        halign: 'center'
        pos_hint:{'center_y':0.65}
    MDFloatingActionButton:
        icon:'android'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '60sp'
        pos_hint:{'center_x':0.5,'center_y':0.32}
        on_press:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value:30
        pos_hint:{'center_y':0.02} 

<UsernameScreen>:
    name:'usernamescreen'
    
    MDLabel:
        text:'User Login for Worker and patient'
        font_style: 'H2'
        halign: 'center'
        pos_hint:{'center_y':0.80}
    
    MDLabel:
        text:'Ambulance worker Login'
        font_style: 'H2'
        font_size: '20sp'
        halign: 'center'
        pos_hint:{'center_y':0.26}
    MDFloatingActionButton:
        icon:'android'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '60sp'
        pos_hint:{'center_x':0.5,'center_y':0.16}
        on_press:
            root.manager.current = 'ambulancescreen'
            root.manager.transition.direction = 'left'
    MDLabel:
        text:'User or Patient Login'
        font_style: 'H2'
        font_size: '20sp'
        halign: 'center'
        pos_hint:{'center_y':0.56}
    MDFloatingActionButton:
        icon:'android'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '60sp'
        pos_hint:{'center_x':0.5,'center_y':0.45}
        on_press:
            root.manager.current = 'paitentscreen'
            root.manager.transition.direction = 'left'
    MDFloatingActionButton:
        id : welcome_back
        icon: "arrow-left"
        pos_hint: {'center_x':0.15,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "38sp"
        on_release :
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'right'  
            
<AmbulanceScreen>:
    name:'ambulancescreen'
    MDLabel:
        text:'User Login for Worker and patient'
        font_style: 'H2'
        halign: 'center'
        pos_hint:{'center_y':0.65}
    MDFloatingActionButton:
        id : welcome_back
        icon: "arrow-left"
        pos_hint: {'center_x':0.15,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "38sp"
        on_release :
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'right'

<UserLoginScreen>:
    name:'paitentscreen'
    MDLabel:
        text:'User Login for Worker and patient'
        font_style: 'H2'
        halign: 'center'
        pos_hint:{'center_y':0.65}
    MDFloatingActionButton:
        id : welcome_back
        icon: "arrow-left"
        pos_hint: {'center_x':0.15,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "38sp"
        on_release :
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'right'
        
'''

class WelcomeScreen(Screen):
    pass
class UsernameScreen(Screen):
    pass
class AmbulanceScreen(Screen):
    pass
class UserLoginScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='Welcomescreen'))
sm.add_widget(UsernameScreen(name='Usernamescreen'))
sm.add_widget(AmbulanceScreen(name='Ambscreen'))
sm.add_widget(UserLoginScreen(name='Paitentscreen'))

class NewApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(helpstr)
        return self.strng


NewApp().run()
