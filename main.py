import json
import tkinter
from tkinter import ttk
from tkinter import messagebox
from wand.image import Image as wandImage
# import wand
from PIL import ImageTk
from PIL import Image as PILimage
# import PIL
import shutil
import os
from pathlib import Path
import sys

# NOTE-TO-SELF
# one reason why the "update image" is so confusing, is becoz. once we change change/edit an image,
# the "handle" of that image is no longer valid, and on top of that, updating inside function means making sure PhotoImage is in the scope always. And using wand instead of PIL works for us. Not sure if its, a problem with our knowledge


lastUsed_data = []

# folderState = True

# def doFoldersExist():
#     if not Path("./input").is_dir() or not Path("./temp").is_dir() or not Path("./input/__tree.jpg").is_file():
        # folderState = False
        # messagebox.showinfo(message=f"The folder ./input does not exist")
        # messagebox.showinfo(message=f"The folder ./temp does not exist")




def folder_required(func):
    """
    A simple decorator that prints messages before and after
    the decorated function is called.
    """
    def wrapper(*args, **kwargs):
        if not Path("./input").is_dir() or not Path("./temp").is_dir() or not Path("./input/__tree.jpg").is_file():
            errorMessage = "Make sure ./input, ./temp and ./input/_tree.jpg exist"
            messagebox.showinfo(message=f"App disabled becoz: {errorMessage}")
            window.destroy()
            sys.exit(0)
        return func(*args, **kwargs)
        print("asd")
    return wrapper


# Vfilename="derevia-tree.jpg"


mainLabelWindowX = 500
mainLabelWindowY = 500
activeEffectDisplay = "highlights"

window = tkinter.Tk()
Vscale_high1_val = tkinter.IntVar()
Vscale_high1_val.set(0)
Vscale_high2_val = tkinter.IntVar()
Vscale_high2_val.set(0)
Vscale_br_val = tkinter.IntVar()
Vscale_br_val.set(0)
Vscale_ctr_val = tkinter.IntVar()
Vscale_ctr_val.set(0)
Vscale_mod1_val = tkinter.IntVar()
Vscale_mod1_val.set(0)
Vscale_sat_val = tkinter.IntVar()
Vscale_sat_val.set(0)
Vscale_warmth_val = tkinter.IntVar()
Vscale_warmth_val.set(0)



@folder_required
def initMainImageLabel():    
    global mainLabelWindowX, mainLabelWindowY
    shutil.copyfile(    
        r'./input/__tree.jpg',
        r'./temp/current.jpg'
    )
    Vimage = PILimage.open(r"./temp/current.jpg")
    Vimage.thumbnail((500,500))
    VmainImage = ImageTk.PhotoImage(Vimage)
    return VmainImage

@folder_required
def getListPics():
    return os.listdir("./input")
    
# def reduceLeft(self, left=0):
#     self.crop(
#         left=left
#     )

    
def Vc_toRatio(l_cs, sum):
    return l_cs/sum

    
def wandImage_getWidth(p_img):
    img = wandImage(filename=r'./input/'+Vfilename)
    return img.width




def Vresize(self,p_width):
    self.resize(p_width,
                  int(p_width/self.width*self.height)
                  )






def neutralizeEffectDisplayed():
    global activeEffectDisplay
    frameEffect_high.grid_forget()
    frameEffect_br.grid_forget()
    frameEffect_ctr.grid_forget()
    frameEffect_mod.grid_forget()
    frameEffect_sat.grid_forget()
    frameEffect_warmth.grid_forget()
    activeEffectDisplay = ""

        


# def leftSide(Vfilename):
#     global VmainImage,Vimage
#     try:
#         Vleft = Vscale.get()
#         Vimage.reduceLeft(left=Vleft)
#         Vimage.save(filename=r"./temp/current.jpg")
#         # ===== endleftcrop
        
#         messagebox.showinfo(message=f"Slide value: {Vleft}")
#         Vimage = wandImage(filename=r"./temp/current.jpg")
#         blob = Vimage.make_blob(format="jpg")
#         VmainImage = ImageTk.PhotoImage(data=blob)
#         # ===== endgloballyupdatevar


#     except Exception as e:
#         messagebox.showwarning(message=f"Error: {e}")


def on_effectList_select(event):
    global activeEffectDisplay, VeffectChosen
    try:
        
        VShow_effect(VeffectChosen.get())
        print(activeEffectDisplay)
        # shutil.copyfile(
        #     os.path.join('input/', VpicChosen.get()),
        #     r'./temp/current.jpg'
        # )
        # filename = "./config/last-used.json"
        # with open(filename, 'w') as file:
        #     json.dump([], file, indent=4) # indent=4 for pretty-printing with 4 spaces
        # VupdateImageLabel()
        
    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")

def on_picList_select(event):
    global VpicChosen
    try:

        shutil.copyfile(
            os.path.join('input/', VpicChosen.get()),
            r'./temp/current.jpg'
        )
        filename = "./config/last-used.json"
        with open(filename, 'w') as file:
            json.dump([], file, indent=4) # indent=4 for pretty-printing with 4 spaces
        VupdateImageLabel()
    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")



def VappendJson():
    global lastUsed_data

    filename = "./config/last-used.json"
    try:
        with open(filename, 'w') as file:
            json.dump(lastUsed_data, file, indent=4) # indent=4 for pretty-printing with 4 spaces
        
    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")


def Vbrightness_event():
    global VlabelImage, VmainImage, lastUsed_data
    try:
        Vimage = wandImage(filename=r"./temp/current.jpg")
        l_br = Vscale_br_val.get() # l_br is local brightness
        Vimage.brightness_contrast(brightness=l_br, contrast=0)
        Vimage.save(filename=r"./temp/current.jpg")
        print(l_br)
        # ===== endleftcrop
        
        Vimage = PILimage.open(r"./temp/current.jpg")
        Vimage.thumbnail((500,500))
        VmainImage = ImageTk.PhotoImage(Vimage)
        # ===== endgloballyupdatevar

        lastUsed_data.append({"effect": "brightness", "value1": l_br})
        VappendJson()
        # endappendjson        

        VlabelImage.config(image=VmainImage)
        # ===== endupdateimagelabel

    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")
        print(e)
        
def Vcontrast_event():
    global VlabelImage, VmainImage, lastUsed_data
    try:
        Vimage = wandImage(filename=r"./temp/current.jpg")
        l_ctr = Vscale_ctr_val.get() # l_ctr is local contrast
        Vimage.brightness_contrast(brightness=0, contrast=l_ctr)
        Vimage.save(filename=r"./temp/current.jpg")
        print(l_ctr)
        # ===== endleftcrop
        
        Vimage = PILimage.open(r"./temp/current.jpg")
        Vimage.thumbnail((500,500))
        VmainImage = ImageTk.PhotoImage(Vimage)
        # ===== endgloballyupdatevar

        lastUsed_data.append({"effect": "contrast", "value1": l_ctr})
        VappendJson()
        # endappendjson        

        VlabelImage.config(image=VmainImage)
        # ===== endupdateimagelabel

    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")
        print(e)

        
def Vmodulate_event():
    global VlabelImage, VmainImage, lastUsed_data
    try:
        Vimage = wandImage(filename=r"./temp/current.jpg")
        l_mod1 = Vscale_mod1_val.get() # l_mod1 is local br
        Vimage.modulate(brightness=l_mod1)
        Vimage.save(filename=r"./temp/current.jpg")
        print(l_mod1)

        # ===== endmodulate
        
        Vimage = PILimage.open(r"./temp/current.jpg")
        Vimage.thumbnail((500,500))
        VmainImage = ImageTk.PhotoImage(Vimage)
        # ===== endgloballyupdatevar

        lastUsed_data.append({"effect": "exposure", "value1": l_mod1})
        VappendJson()
        # endappendjson        

        VlabelImage.config(image=VmainImage)
        # ===== endupdateimagelabel

    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")
        print(e)

        
def Vsaturation_event():
    global VlabelImage, VmainImage, lastUsed_data
    try:
        Vimage = wandImage(filename=r"./temp/current.jpg")
        l_sat = Vscale_sat_val.get() # l_mod1 is local br
        Vimage.modulate(saturation=l_sat)
        Vimage.save(filename=r"./temp/current.jpg")
        print(l_sat)

        # ===== endsaturation
        
        Vimage = PILimage.open(r"./temp/current.jpg")
        Vimage.thumbnail((500,500))
        VmainImage = ImageTk.PhotoImage(Vimage)
        # ===== endgloballyupdatevar

        lastUsed_data.append({"effect": "saturation", "value1": l_sat})
        VappendJson()
        # endappendjson        

        VlabelImage.config(image=VmainImage)
        # ===== endupdateimagelabel

    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")
        print(e)


# DONT DELETE: https://docs.wand-py.org/en/0.6.12/guide/fx.html#colorize
def Vwarmth_event():
    global VlabelImage, VmainImage, lastUsed_data
    try:
        Vimage = wandImage(filename=r"./temp/current.jpg")
        l_warmth = Vscale_warmth_val.get() # l_mod1 is local br

        if l_warmth > 50:
            l_color = "orange"
            l_val = (l_warmth - 50) * 2
        else:
            l_color = "blue"
            l_val = (50 - l_warmth) * 2
        #endgetcolor        


        if l_color == "orange":
            Vimage.colorize(color=l_color, alpha=f"rgb(5%, 5%, {l_val}%)")
        else:
            Vimage.colorize(color=l_color, alpha=f"rgb({l_val}%, 5%, 5%)")
        Vimage.save(filename=r"./temp/current.jpg")
        print(l_warmth)

        # ===== endsaturation
        
        Vimage = PILimage.open(r"./temp/current.jpg")
        Vimage.thumbnail((500,500))
        VmainImage = ImageTk.PhotoImage(Vimage)
        # ===== endgloballyupdatevar

        lastUsed_data.append({"effect": "warmth", "value1": l_warmth})
        VappendJson()
        # endappendjson        

        VlabelImage.config(image=VmainImage)
        # ===== endupdateimagelabel

    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")
        print(e)

        
        
def Vhighlight__Button():
    global VlabelImage, VmainImage, lastUsed_data
    try:
        Vimage = wandImage(filename=r"./temp/current.jpg")
        l_cs1 = Vscale_high1_val.get() # l_cs1 is local contrast stretch
        print(l_cs1)
        ratio1=Vc_toRatio(l_cs1, 100)
        l_cs2 = Vscale_high2_val.get() # l_cs2 is local contrast stretch
        print(l_cs2)
        ratio2=Vc_toRatio((100-l_cs2), 100)
        Vimage.contrast_stretch(ratio1, ratio2)
        # TEST: Vimage.contrast_stretch(20,20)
        Vimage.save(filename=r"./temp/current.jpg")
        # ===== endleftcrop
        
        Vimage = PILimage.open(r"./temp/current.jpg")
        Vimage.thumbnail((500,500))
        # blob = Vimage.make_blob(format="jpg")
        # if Photoimage below is imported globally, it will not work, PhotoImage object needs to redefined inside scope, otherwise it doesnt track image changes, weird.
        VmainImage = ImageTk.PhotoImage(Vimage)
        # ===== endgloballyupdatevar


        lastUsed_data.append({"effect": "highlight", "value1": l_cs1, "value2": l_cs2})
        VappendJson()
        # endappendjson


        VlabelImage.config(image=VmainImage)
        # ===== endupdateimagelabel

    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")
        print(e)

def VsaveJson():
    global lastUsed_data

    filename = "./config/last-used.json"
    try:
        with open(filename, 'w') as file:
            json.dump(lastUsed_data, file, indent=4) # indent=4 for pretty-printing with 4 spaces
        messagebox.showinfo(message=f"Successfull export: {filename}")
        
    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")

    


        
def VShow_effect(l_effectChosen):
    global activeEffectDisplay
    neutralizeEffectDisplayed()
    activeEffectDisplay = l_effectChosen
    if activeEffectDisplay == "brightness":
        frameEffect_br.grid(row=1,column=1)
    elif activeEffectDisplay == "highlights":
        frameEffect_high.grid(row=1,column=1)
    elif activeEffectDisplay == "contrast":
        frameEffect_ctr.grid(row=1,column=1)
    elif activeEffectDisplay == "exposure":
        frameEffect_mod.grid(row=1,column=1)
    elif activeEffectDisplay == "saturation":
        frameEffect_sat.grid(row=1,column=1)
    elif activeEffectDisplay == "warmth":
        frameEffect_warmth.grid(row=1,column=1)

        
#delete
def VupdateImageLabel():
    global VmainImage, VlabelImage

    try:
        Vimage = PILimage.open(r"./temp/current.jpg")
        Vimage.thumbnail((500,500))
        VmainImage = ImageTk.PhotoImage(Vimage)
        VlabelImage.config(image=VmainImage)

    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")


def setSizePosition(window):
    x = 500
    y = 50
    width = 1000
    height = 800
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.geometry(f"+{x}+{y}")
    
# def setSize(window):
#     x = 500
#     y = 500
#     window.geometry(f"+{x}+{y}")
        



frame_mc = tkinter.Frame(window) # frame main control
frame_mc.grid(row=0,column=0,padx=10,pady=10)
# endframemaincontrol

# VShow_cs_button = tkinter.Button(frame_mc, text='Show effect', command=lambda:VShow_cs())
# VShow_cs_button.pack(padx=10, pady=10)


VeffectChosen = tkinter.StringVar()
VeffectList =ttk.Combobox(frame_mc, width = 27, textvariable = VeffectChosen)
VeffectList['values'] = ["brightness", "highlights", "contrast", "exposure", "saturation", "warmth"]
VeffectList.bind("<<ComboboxSelected>>", on_effectList_select)
VeffectList.pack()


VpicChosen = tkinter.StringVar()
VpicList = ttk.Combobox(frame_mc, width = 27, textvariable = VpicChosen)
VpicList['values'] = getListPics()
VpicList.bind("<<ComboboxSelected>>", on_picList_select)
VpicList.pack()


VmainImage = initMainImageLabel()
VlabelImage = tkinter.Label(window, image=VmainImage, width=mainLabelWindowX, height=mainLabelWindowY)
VlabelImage.grid(row=0,column=1,padx=10,pady=10)
#endmainimagelabel

Vlabel2 = tkinter.Label(window, text="Some image details").grid(row=0, column=2)


# w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
# w.pack()



# VButton_leftSide = tkinter.Button(window, text='Crop', command=lambda:leftSide(Vfilename)).grid(row=1, column=0)


frameEffect_high = tkinter.Frame(window) 
frameEffect_high.grid(row=1,column=1, padx=10, pady=10, rowspan=10)
Vlabel_high1 = tkinter.Label(frameEffect_high,  text=f"white values (start at 0)")
Vlabel_high1.pack(padx=10,pady=(10,0))
Vscale_high1 = tkinter.Scale(frameEffect_high, from_=0, to=100, orient='horizontal', variable=Vscale_high1_val)
Vscale_high1.pack(padx=10,pady=(0,10))
Vlabel_high2 = tkinter.Label(frameEffect_high,  text=f"black values (start at 100)")
Vlabel_high2.pack(padx=10,pady=(10,0))
Vscale_high2 = tkinter.Scale(frameEffect_high, from_=0, to=100, orient='horizontal', variable=Vscale_high2_val)
Vscale_high2.set(100)
Vscale_high2.pack(padx=10,pady=(0,10))
tkinter.Button(frameEffect_high, text='Highlight', command=lambda:Vhighlight__Button()).pack(padx=10,pady=10)
frameEffect_high.grid_forget()
# frameEffect_high is frame effect contrast stretch
#endhighlight
                                                                                                          
                                                                                                          

frameEffect_br = tkinter.Frame(window) # frameEffect_br is frame effect brightness
frameEffect_br.grid(row=1,column=1,rowspan=10)
Vlabel_br = tkinter.Label(frameEffect_br, text=f"brightness value")
Vlabel_br.pack(padx=10,pady=(10,0))
Vscale_br = tkinter.Scale(frameEffect_br, from_=-100, to=100, orient='horizontal', variable=Vscale_br_val)
Vscale_br.pack(padx=10,pady=(0,10))
tkinter.Button(frameEffect_br, text='Brightness', command=lambda:Vbrightness_event()).pack(padx=10,pady=10)
frameEffect_br.grid_forget()
# frameEffect_br is frame brightness
#endbrightness


frameEffect_ctr = tkinter.Frame(window) # frameEffect_ctr is frame effect brightness
frameEffect_ctr.grid(row=1,column=1,rowspan=10)
Vlabel_ctr = tkinter.Label(frameEffect_ctr, text=f"contrast value")
Vlabel_ctr.pack(padx=10,pady=(10,0))
Vscale_ctr = tkinter.Scale(frameEffect_ctr, from_=-100, to=100, orient='horizontal', variable=Vscale_ctr_val)
Vscale_ctr.pack(padx=10,pady=(0,10))
tkinter.Button(frameEffect_ctr, text='Contrast', command=lambda:Vcontrast_event()).pack(padx=10,pady=10)
frameEffect_ctr.grid_forget()
# frameEffect_ctr is frame contrast
#endcontrast


frameEffect_mod = tkinter.Frame(window) # frameEffect_mod is frame effect modulate
frameEffect_mod.grid(row=1,column=1,rowspan=10)
Vlabel_mod1 = tkinter.Label(frameEffect_mod, text=f"exposure")
Vlabel_mod1.pack(padx=10,pady=(10,0))
Vscale_mod1 = tkinter.Scale(frameEffect_mod, from_=0, to=200, orient='horizontal', variable=Vscale_mod1_val)
Vscale_mod1.set(100)
Vscale_mod1.pack(padx=10,pady=(0,10))
tkinter.Button(frameEffect_mod, text='Exposure', command=lambda:Vmodulate_event()).pack(padx=10,pady=10)
frameEffect_mod.grid_forget()
# frameEffect_mod is frame modulate
#endmodulate


frameEffect_sat = tkinter.Frame(window) # frameEffect_sat is frame saturation
frameEffect_sat.grid(row=1,column=1,rowspan=10)
Vlabel_sat = tkinter.Label(frameEffect_sat, text=f"saturation")
Vlabel_sat.pack(padx=10,pady=(10,0))
Vscale_sat = tkinter.Scale(frameEffect_sat, from_=0, to=200, orient='horizontal', variable=Vscale_sat_val)
Vscale_sat.set(100)
Vscale_sat.pack(padx=10,pady=(0,10))
tkinter.Button(frameEffect_sat, text='Exposure', command=lambda:Vsaturation_event()).pack(padx=10,pady=10)
frameEffect_sat.grid_forget()
# frameEffect_sat is frame contrast
#endsaturation


frameEffect_warmth = tkinter.Frame(window) # frameEffect_warmth is frame warmth
frameEffect_warmth.grid(row=1,column=1,rowspan=10)
Vlabel_warmth = tkinter.Label(frameEffect_warmth, text=f"warmth (below 50 is colder)")
Vlabel_warmth.pack(padx=10,pady=(10,0))
Vscale_warmth = tkinter.Scale(frameEffect_warmth, from_=0, to=100, orient='horizontal', variable=Vscale_warmth_val)
Vscale_warmth.set(50)
Vscale_warmth.pack(padx=10,pady=(0,10))
tkinter.Button(frameEffect_warmth, text='Exposure', command=lambda:Vwarmth_event()).pack(padx=10,pady=10)
frameEffect_warmth.grid_forget()
# frameEffect_warmth is frame contrast
#endwarmth



frameEffect_neMainControls = tkinter.Frame(window) # neMainControls is no effect main controls
frameEffect_neMainControls.grid(row=1,column=2)

#delete
VupdateImageLabel_button = tkinter.Button(frameEffect_neMainControls, text='View', command=lambda:VupdateImageLabel())
VupdateImageLabel_button.pack(padx=10,pady=10)


VsaveJson_button = tkinter.Button(frameEffect_neMainControls, text='Export to JSON', command=lambda:VsaveJson())
VsaveJson_button.pack(padx=10,pady=10)








# window.geometry(f"+{x}+{y}")
# setPosition(window)
setSizePosition(window)
tkinter.mainloop()



