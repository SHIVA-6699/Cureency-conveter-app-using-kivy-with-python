
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.app import App
from kivy.core.window import Window
Builder.load_string('''
            

<MygridLayout>

    BoxLayout:
        size:root.width,root.height
        spacing:50
        padding:50
        orientation:'vertical'
        
        Label:
            text:"RUPEES"
            
           
            background_color:(1,1,1,1)
            background_normal:''
            color:(1,1,1,1)
            size_hint:(.5, .5)
            pos_hint:{'center_x': .5, 'center_y': .5}
            font_size:34
        TextInput:
            multiline:True
            id:c
            font_size:34
            size_hint:(1,1)
        Label:
            text:"DOLARS"
            font_size:30
        TextInput:
            multiline:True
            id:d
            font_size:34
            size_hint:(1,1)
        GridLayout:
            cols:2
            Label:
                text:"INR"
            CheckBox:
                
                on_active:root.press1(self,self.active)
            Label:
                text:"USD"
            CheckBox:
               
                on_active:root.press2(self,self.active)
                
 
            
            

                

''')
class Mygridlayout(Widget):

    
        def press2(self,instance,value):
           
           
            a=self.ids.c.text
            b=eval(a)
            
            if(value==True):
                e=b/82.52
                
                self.ids.d.text=f'{e}$'
                
                
            else:
              self.ids.c.text=""
              self.ids.d.text=""
                
                
                
        
                
        def press1(self,instance,value):

            a=self.ids.d.text
            b=eval(a)
            
            if(value==True):
                e=b*82.52
                
                self.ids.c.text=f'{e}₹'
                
                
            else:
                self.ids.c.text=""
                self.ids.d.text=""
                
               
                
class Myapp(App):

    def build(self):
        return  Mygridlayout()
if __name__=='__main__':
    Myapp().run()
