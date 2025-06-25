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

# NOTE-TO-SELF
# one reason why the "update image" is so confusing, is becoz. once we change change/edit an image,
# the "handle" of that image is no longer valid, and on top of that, updating inside function means making sure PhotoImage is in the scope always. And using wand instead of PIL works for us. Not sure if its, a problem with our knowledge


lastUsed_data = []



Vfilename="derevia-tree.jpg"
shutil.copyfile(    
    r'./input/derevia-tree.jpg',
    r'./temp/current.jpg'
)

mainLabelWindowX = 500
mainLabelWindowY = 500
activeEffectDisplay = "cs"

window = tkinter.Tk()
Vscale_val = tkinter.IntVar()
Vscale_val.set(0)



def reduceLeft(self, left=0):
    self.crop(
        left=left
    )

def Vc_toRatio(l_cs, sum):
    return l_cs/sum

    
def wandImage_getWidth(p_img):
    img = wandImage(filename=r'./input/'+Vfilename)
    return img.width




def Vresize(self,p_width):
    self.resize(p_width,
                  int(p_width/self.width*self.height)
                  )



wandImage.reduceLeft = reduceLeft
wandImage.Vresize = Vresize



def neutralizeEffectDisplayed():
    global activeEffectDisplay
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


        
def Vcontrast_stretch__Button(Vfilename):
    global VlabelImage, VmainImage, lastUsed_data
    try:
        Vimage = wandImage(filename=r"./temp/current.jpg")
        l_cs = Vscale_val.get() # l_cs is local contrast stretch
        print(l_cs)
        ratio=Vc_toRatio(l_cs, 90)
        Vimage.contrast_stretch(ratio, ratio)
        # TEST: Vimage.contrast_stretch(20,20)
        Vimage.save(filename=r"./temp/current.jpg")
        # ===== endleftcrop
        
        Vimage = wandImage(filename=r"./temp/current.jpg")
        blob = Vimage.make_blob(format="jpg")
        # if Photoimage below is imported globally, it will not work, PhotoImage object needs to redefined inside scope, otherwise it doesnt track image changes, weird.
        VmainImage = ImageTk.PhotoImage(data=blob)
        # ===== endgloballyupdatevar


        lastUsed_data.append({"effect": "contrast_stretch", "value1": l_cs})
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

    

        
def VShow_cs():
    global frameEffect_cs, activeEffectDisplay
    if activeEffectDisplay == "":
        frameEffect_cs.grid(row=1,column=1)
        activeEffectDisplay = "cs"
    else:
        frameEffect_cs.grid_forget()
        neutralizeEffectDisplayed()
        
    


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
    height = 600
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.geometry(f"+{x}+{y}")
    
# def setSize(window):
#     x = 500
#     y = 500
#     window.geometry(f"+{x}+{y}")
        



frame_mc = tkinter.Frame(window) # frame main control
frame_mc.grid(row=0,column=0,padx=10,pady=10)
# endframemaincontrol

VShow_cs_button = tkinter.Button(frame_mc, text='Show effect', command=lambda:VShow_cs())
VShow_cs_button.pack()

VpicChosen = tkinter.StringVar()
VpicList = ttk.Combobox(frame_mc, width = 27, textvariable = VpicChosen)

# Adding combobox drop down list
VpicList['values'] = os.listdir("./input")
VpicList.bind("<<ComboboxSelected>>", on_picList_select)
VpicList.pack()




Vimage = PILimage.open(r"./temp/current.jpg")
Vimage.thumbnail((500,500))
VmainImage = ImageTk.PhotoImage(Vimage)
VlabelImage = tkinter.Label(window, image=VmainImage, width=mainLabelWindowX, height=mainLabelWindowY)
VlabelImage.grid(row=0,column=1,padx=10,pady=10)
#endmainimagelabel

Vlabel2 = tkinter.Label(window, text="Some image details").grid(row=0, column=2)


# w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
# w.pack()



# VButton_leftSide = tkinter.Button(window, text='Crop', command=lambda:leftSide(Vfilename)).grid(row=1, column=0)


frameEffect_cs = tkinter.Frame(window) # frameEffect_cs is frame effect contrast stretch
frameEffect_cs.grid(row=1,column=1)
Vscale = tkinter.Scale(frameEffect_cs, from_=0, to=100, orient='horizontal', variable=Vscale_val)
Vscale.pack(padx=10,pady=10)
tkinter.Button(frameEffect_cs, text='Contrast', command=lambda:Vcontrast_stretch__Button(Vfilename)).pack(padx=10,pady=10)


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



