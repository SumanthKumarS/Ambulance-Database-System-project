import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.picker import MDDatePicker
from kivy.uix.image import Image
kivy.require('1.9.0')
from kivy.uix.image import Image
from helper import code_helper


#Window.size = (600 , 600)

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
        background_color: 1, 1, 0, 1
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
        font_size: "20sp"
        halign: 'center'
        pos_hint:{'center_y':0.8}
    MDFloatingActionButton:
        id : welcome_back
        icon: "arrow-left"
        pos_hint: {'center_x':0.15,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "38sp"
        on_release :
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'right'
    MDTextField:
        id: username_text
        hint_text : 'username'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'account'
        icon_right_color: 0,0.5,0,0.9
        pos_hint: {'center_x':0.5,'center_y':0.6}
        required: True
        size_hint: (0.4,0.1)
        #icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id: password_text
        hint_text : 'password'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        required: True
        size_hint: (0.4,0.1)
        icon_right_color: app.theme_cls.primary_color
        required : True
    
    MDIconButton:
        id : username_check_extra_button
        icon: "reload"
        pos_hint: {'center_x':0.69,'center_y':0.62}
        theme_text_color: "Custom"
        text_color: [0,0,0,0]
        user_font_size: "40sp"
    
    MDRoundFlatButton:
        id: username_check_btn
        text: 'Check'
        pos_hint: {'center_x':0.8,'center_y':0.5}
        font_size: '23sp'
        on_release: 
            app.username_checker()
            app.password_checker()        
        
    MDFloatingActionButton:
        id : username_enter 
        disabled: True
        pos_hint: {'center_x':0.83,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "43sp"
        on_release:
            root.manager.current = 'dobinput'
        
    MDRoundFlatButton:
        id : dob
        text: 'D . O . B'   
        pos_hint: {'center_x':0.5,'center_y':0.4}
        font_size: '30sp'
        on_release : 
            app.show_date_picker()
            
    MDFloatingActionButton:
        icon: "arrow-right"
        disabled: True
        id : dob_enter 
        pos_hint: {'center_x':0.83,'center_y':0.11}
        md_bg_color: app.theme_cls.primary_color
        user_font_size: "43sp"
        on_release:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'
    
    MDIconButton:
        id: secure
        icon : 'pirate'
        pos_hint: {'center_x':0.5,'center_y':0.30}
        user_font_size: "50sp"
        theme_text_color: "Custom"
        text_color: [1,0,0,1]
        
    

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
        #sm.add_widget(self.strng)
        return self.strng


        self.dob_entered = True
        return self.sm

    def username_checker(self):
        username_check_false = True
        username_text_data = self.strng.get_screen('ambulancescreen').ids.username_text.text
        try:
            int(username_text_data)
        except:
            username_check_false = False

        if username_check_false or username_text_data.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry' , on_release=self.close_username_dialog)
            self.username_dialoge = MDDialog(title='Invalid Username' , text='Please Enter a valid Username' ,
                                             size_hint=(0.7 , 0.2) , buttons=[cancel_btn_username_dialogue])
            self.username_dialoge.open()
        else:
            screen_usernamescreen = self.strng.get_screen('ambulancescreen')
            screen_usernamescreen.ids.username_enter.disabled = False
            screen_usernamescreen.ids.username_check_extra_button.icon = 'account-check-outline'
            screen_usernamescreen.ids.username_check_btn.text_color = [1 , 1 , 1 , 0]
            screen_usernamescreen.ids.username_check_btn.md_bg_color = [1 , 1 , 1 , 0]
            screen_usernamescreen.ids.username_check_extra_button.text_color = self.theme_cls.primary_color
            screen_usernamescreen.ids.username_check_extra_button.pos_hint = {'center_x': 0.5, 'center_y': 0.8}
            screen_usernamescreen.ids.username_check_extra_button.user_font_size = '60sp'

    def password_checker(self):
        password_check_false = True
        password_text_data = self.strng.get_screen('ambulancescreen').ids.password_text.text
        try :
            int(password_text_data)
        except :
            password_check_false = False

        if password_check_false or password_text_data.split() == [] :
            cancel_btn_password_dialogue = MDFlatButton(text='Retry' , on_release=self.close_password_dialog)
            self.password_dialoge = MDDialog(title='Invalid Username' , text='Please Enter a valid Username' ,
                                             size_hint=(0.7 , 0.2) , buttons=[cancel_btn_password_dialogue])
            self.password_dialoge.open()
        else :
            screen_passwordscreen = self.strng.get_screen('ambulancescreen')
            screen_passwordscreen.ids.username_enter.disabled = False
            screen_passwordscreen.ids.username_check_extra_button.icon = 'account-check-outline'
            screen_passwordscreen.ids.username_check_btn.text_color = [1 , 1 , 1 , 0]
            screen_passwordscreen.ids.username_check_btn.md_bg_color = [1 , 1 , 1 , 0]
            screen_passwordscreen.ids.username_check_extra_button.text_color = self.theme_cls.primary_color
            screen_passwordscreen.ids.username_check_extra_button.pos_hint = {'center_x' : 0.8 , 'center_y' : 0.5}
            screen_passwordscreen.ids.username_check_extra_button.user_font_size = '60sp'

    def show_date_picker(self):
        date_dialog = MDDatePicker(
            callback=self.get_date,
            year=2000,
            month=1,
            day=1,
        )
        date_dialog.open()

    def get_date(self, date):
        self.dob = date
        dob_input_screen_selector = self.strng.get_screen('ambulancescreen')
        # here i put the next button disbaled as False so user can enter in that window
        dob_input_screen_selector.ids.dob_enter.disabled = False
        dob_input_screen_selector.ids.dob.text = str(self.dob)
        dob_input_screen_selector.ids.secure.text_color = [0 , 1 , 0 , 0.7]



NewApp().run()
