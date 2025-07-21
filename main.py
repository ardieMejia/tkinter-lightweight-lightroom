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
        if not Path("./input").is_dir() or not Path("./temp").is_dir() or not Path("./input/__first.jpg").is_file():
            errorMessage = "Make sure ./input, ./temp and ./input/_tree.jpg exist"
            messagebox.showinfo(message=f"App disabled becoz: {errorMessage}")
            window.destroy()
            sys.exit(0)
        return func(*args, **kwargs)
        print("asd")
    return wrapper


def batch_required(func):
    """
    A simple decorator that prints messages before and after
    the decorated function is called.
    """
    def wrapper(*args, **kwargs):
        if not Path("./batch").is_dir():
            VbatchButton.config(state=tkinter.DISABLED)
            VbatchButton.config(text="no batch folder found")
            return []
        elif not len(os.listdir("./batch")):
            VbatchButton.config(state=tkinter.DISABLED)
            VbatchButton.config(text="no files in batch")
            return []
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
Vscale_sptintR_val = tkinter.IntVar()
Vscale_sptintR_val.set(0)
Vscale_sptintG_val = tkinter.IntVar()
Vscale_sptintG_val.set(0)
Vscale_sptintB_val = tkinter.IntVar()
Vscale_sptintB_val.set(0)
Vscale_spgray_val = tkinter.IntVar()
Vscale_spgray_val.set(0)



@folder_required
def initMainImageLabel():    
    global mainLabelWindowX, mainLabelWindowY
    shutil.copyfile(    
        r'./input/__first.jpg',
        r'./temp/current.jpg'
    )
    Vimage = PILimage.open(r"./temp/current.jpg")
    Vimage.thumbnail((500,500))
    VmainImage = ImageTk.PhotoImage(Vimage)
    return VmainImage

@folder_required
def getListPics():
    return os.listdir("./input")
    
@batch_required
def getBatchPics():
    return os.listdir("./batch")


# def reduceLeft(self, left=0):
#     self.crop(
#         left=left
#     )

    
def Vc_toRatio(l_cs, sum):
    return l_cs/sum


def Vinvert_ratio(l_r):
    return 1 - l_r

    
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
    frameEffect_sptint.grid_forget()
    frameEffect_spgray.grid_forget()
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

def applyEffect(*value, **kwargs):
    # global VlabelImage, VmainImage, lastUsed_data
    if kwargs["effectName"] == "brightness":
        try:
            if len(value) != 1:
                messagebox.showwarning(message=f"Internal Error: tuple size not matching")
                return 
            Vimage = wandImage(filename=kwargs["inName"])
            print(Vimage)
            l_br = value[0]
            Vimage.brightness_contrast(brightness=l_br, contrast=0)
            Vimage.save(filename=kwargs["outName"])
        except:
            print(f"something went wrong")
    if kwargs["effectName"] == "highlights":
        print(type(value))
        print(value)
        try:
            if len(value) != 2:
                messagebox.showwarning(message=f"Internal Error: tuple size not matching")
                return 
            Vimage = wandImage(filename=kwargs["inName"])
            print(Vimage)
            ratio1 = value[0] 
            ratio2 = value[1]
            print(ratio1)
            print(ratio2)
            print(kwargs["outName"])
            # Vimage.brightness_contrast(brightness=l_br, contrast=0)
            # Vimage.brightness_contrast(brightness=0, contrast=l_ctr)
            Vimage.contrast_stretch(ratio1, ratio2)
            # Vimage.brightness_contrast(brightness=10, contrast=0)
            Vimage.save(filename=kwargs["outName"])
        except:
            print(f"something went wrong")
    if kwargs["effectName"] == "contrast":
        try:
            if len(value) != 1:
                messagebox.showwarning(message=f"Internal Error: tuple size not matching")
                return 
            Vimage = wandImage(filename=kwargs["inName"])
            print(Vimage)
            l_ctr= value[0]
            # Vimage.brightness_contrast(brightness=l_br, contrast=0)
            Vimage.brightness_contrast(brightness=0, contrast=l_ctr)
            Vimage.save(filename=kwargs["outName"])
        except:
            print(f"something went wrong")
    if kwargs["effectName"] == "exposure":
        try:
            if len(value) != 1:
                messagebox.showwarning(message=f"Internal Error: tuple size not matching")
                return 
            Vimage = wandImage(filename=kwargs["inName"])
            print(Vimage)
            l_mod= value[0]
            # Vimage.brightness_contrast(brightness=l_br, contrast=0)
            # Vimage.brightness_contrast(brightness=0, contrast=l_ctr)
            Vimage.modulate(brightness=l_mod)
            Vimage.save(filename=kwargs["outName"])
        except:
            print(f"something went wrong")
    if kwargs["effectName"] == "saturation":
        try:
            if len(value) != 1:
                messagebox.showwarning(message=f"Internal Error: tuple size not matching")
                return 
            Vimage = wandImage(filename=kwargs["inName"])
            print(Vimage)
            l_sat= value[0]
            # Vimage.modulate(brightness=l_mod)
            Vimage.modulate(saturation=l_sat)
            Vimage.save(filename=kwargs["outName"])
        except:
            print(f"something went wrong")
    if kwargs["effectName"] == "warmth":
        try:
            if len(value) != 1:
                messagebox.showwarning(message=f"Internal Error: tuple size not matching")
                return 
            Vimage = wandImage(filename=kwargs["inName"])
            print(Vimage)
            l_warmth= value[0]
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
            
            # ==========
            Vimage.save(filename=kwargs["outName"])
        except:
            print(f"something went wrong")
    if kwargs["effectName"] == "special tint":
        try:
            if len(value) != 3:
                messagebox.showwarning(message=f"Internal Error: tuple size not matching")
                return 
            Vimage = wandImage(filename=kwargs["inName"])
            print(Vimage)
            l_sptintR = value[0]
            l_sptintG = value[1]
            l_sptintB = value[2]

            print(l_sptintR)
            print(l_sptintG)
            print(l_sptintB)
            print(type(l_sptintB))

            matrix = [[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]]

            if l_sptintG == 0 and l_sptintB == 0:
                l_sptintR_pct = Vc_toRatio(l_sptintR, 100)
                l_v = Vinvert_ratio(l_sptintR_pct)
                matrix = [[1, 0, 0],
                          [0, l_v, 0],
                          [0, 0, l_v]]
            elif l_sptintR == 0 and l_sptintB == 0:
                l_sptintG_pct = Vc_toRatio(l_sptintG, 100)
                l_v = Vinvert_ratio(l_sptintG_pct)
                matrix = [[l_v, 0, 0],
                          [0, 1, 0],
                          [0, 0, l_v]]
            elif l_sptintR == 0 and l_sptintG == 0:
                l_sptintB_pct = Vc_toRatio(l_sptintB, 100)
                l_v = Vinvert_ratio(l_sptintB_pct)
                matrix = [[1, 0, 0],
                          [0, l_v, 0],
                          [0, 0, l_v]]
            elif l_sptintR == 0:
                l_sptintG_pct = Vc_toRatio(l_sptintG, 100)
                l_sptintB_pct = Vc_toRatio(l_sptintB, 100)
                # no inverting, coz dont know how to explain
                matrix = [[1, 0, 0],
                          [0, 1, l_sptintG_pct],
                          [0, l_sptintB_pct, 1]]
            elif l_sptintG == 0:
                l_sptintR_pct = Vc_toRatio(l_sptintR, 100)
                l_sptintB_pct = Vc_toRatio(l_sptintB, 100)
                # no inverting, coz dont know how to explain
                matrix = [[1, 0, l_sptintR_pct],
                          [0, 1, 0],
                          [l_sptintB_pct, 0, 1]]
            elif l_sptintB == 0:
                l_sptintR_pct = Vc_toRatio(l_sptintR, 100)
                l_sptintG_pct = Vc_toRatio(l_sptintG, 100)
                # no inverting, coz dont know how to explain
                matrix = [[1, l_sptintR_pct, 0],
                          [l_sptintG_pct, 1, 0],
                          [0, 0, 1]]
            # ===== endsptint
            Vimage.color_matrix(matrix)
            Vimage.save(filename=kwargs["outName"])
        except:
            print(f"something went wrong")
            
    if kwargs["effectName"] == "grayscale":
        try:
            if len(value) != 1:
                messagebox.showwarning(message=f"Internal Error: tuple size not matching")
                return 
            Vimage = wandImage(filename=kwargs["inName"])
            print(Vimage)
            l_gray= value[0]
            l_gray = Vc_toRatio(l_gray, 100)

            matrix = [[l_gray, l_gray, l_gray],
                      [l_gray, l_gray, l_gray],
                      [l_gray, l_gray, l_gray]]
        
            Vimage.color_matrix(matrix)
            
            # ==========
            Vimage.save(filename=kwargs["outName"])
        except:
            print(f"something went wrong")
            


def Vbrightness_event():
    global VlabelImage, VmainImage, lastUsed_data
    try:
        l_br = Vscale_br_val.get() # l_br is local brightness
        # tuple is undreadable concept
        applyEffect(*(l_br,), effectName="brightness", inName=r"./temp/current.jpg", outName=r"./temp/current.jpg")
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


        
def Vhighlight__Button():
    global VlabelImage, VmainImage, lastUsed_data
    try:
        l_cs1 = Vscale_high1_val.get() # l_cs1 is local contrast stretch
        print(l_cs1)
        ratio1=Vc_toRatio(l_cs1, 100)
        l_cs2 = Vscale_high2_val.get() # l_cs2 is local contrast stretch
        print(l_cs2)
        ratio2=Vc_toRatio((100-l_cs2), 100)
        applyEffect(*(ratio1,ratio2), effectName="highlights", inName=r"./temp/current.jpg", outName=r"./temp/current.jpg")
        # TEST: Vimage.contrast_stretch(20,20)
        # ===== endleftcrop
        
        Vimage = PILimage.open(r"./temp/current.jpg")
        Vimage.thumbnail((500,500))
        # blob = Vimage.make_blob(format="jpg")
        # if Photoimage below is imported globally, it will not work, PhotoImage object needs to redefined inside scope, otherwise it doesnt track image changes, weird.
        VmainImage = ImageTk.PhotoImage(Vimage)
        # ===== endgloballyupdatevar


        lastUsed_data.append({"effect": "highlights", "value1": ratio1, "value2": ratio2})
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
        l_ctr = Vscale_ctr_val.get() # l_ctr is local contrast
        applyEffect(*(l_ctr,), effectName="contrast", inName=r"./temp/current.jpg", outName=r"./temp/current.jpg")
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
        # Vimage = wandImage(filename=r"./temp/current.jpg")
        l_mod1 = Vscale_mod1_val.get() # l_mod1 is local br
        applyEffect(*(l_mod1,), effectName="exposure", inName=r"./temp/current.jpg", outName=r"./temp/current.jpg")
        # Vimage.save(filename=r"./temp/current.jpg")
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
        # Vimage = wandImage(filename=r"./temp/current.jpg")
        l_sat = Vscale_sat_val.get() # l_mod1 is local br
        applyEffect(*(l_sat,), effectName="saturation", inName=r"./temp/current.jpg", outName=r"./temp/current.jpg")
        # Vimage.modulate(saturation=l_sat)
        # Vimage.save(filename=r"./temp/current.jpg")
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

        l_warmth = Vscale_warmth_val.get() # l_mod1 is local br

        applyEffect(*(l_warmth,), effectName="warmth", inName=r"./temp/current.jpg", outName=r"./temp/current.jpg")

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

        
def Vsptint_event():
    global VlabelImage, VmainImage, lastUsed_data
    try:

        l_sptintR = Vscale_sptintR_val.get()
        l_sptintG = Vscale_sptintG_val.get()
        l_sptintB = Vscale_sptintB_val.get()        
        #endgetsptint
        
        applyEffect(*(l_sptintR, l_sptintG, l_sptintB), effectName="special tint", inName=r"./temp/current.jpg", outName=r"./temp/current.jpg")


        Vimage = PILimage.open(r"./temp/current.jpg")
        Vimage.thumbnail((500,500))
        VmainImage = ImageTk.PhotoImage(Vimage)
        # ===== endgloballyupdatevar

        lastUsed_data.append({"effect": "special tint", "valueR": l_sptintR, "valueG": l_sptintG, "valueB": l_sptintB})
        VappendJson()
        # endappendjson

        VlabelImage.config(image=VmainImage)
        # ===== endupdateimagelabel

    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")
        print(e)


def Vspgray_event():
    global VlabelImage, VmainImage, lastUsed_data
    try:
        l_gray = Vscale_spgray_val.get() # l_mod1 is local br
        #endgrayval

        applyEffect(*(l_gray, ), effectName="grayscale", inName=r"./temp/current.jpg", outName=r"./temp/current.jpg")

        print(l_gray)

        # ===== endsaturation
        
        Vimage = PILimage.open(r"./temp/current.jpg")
        Vimage.thumbnail((500,500))
        VmainImage = ImageTk.PhotoImage(Vimage)
        # ===== endgloballyupdatevar

        lastUsed_data.append({"effect": "grayscale", "value1": l_gray})
        VappendJson()
        # endappendjson        

        VlabelImage.config(image=VmainImage)
        # ===== endupdateimagelabel

    except Exception as e:
        messagebox.showwarning(message=f"Error: {e}")
        print(e)


def Vbatch_event():
    # global VlabelImage, VmainImage, lastUsed_data

    os.makedirs("./batch_output", exist_ok=True)

    print("hello there")

    with open("./config/last-used.json") as f:
        stackedEffect = json.load(f)        

    if not VbatchList.curselection():
        for raw_img in os.listdir("./batch"):
            shutil.copyfile(    
                f'./batch/{raw_img}',
                f'./batch_output/{raw_img}'
            )
            for effect in stackedEffect:
                if effect["effect"] == "brightness":
                    print("processing brighntess on"+ str(raw_img))
                    value1 = effect["value1"]
                    # Vimage = wandImage(filename=f"./batch_output/{raw_img}")
                    applyEffect(*(value1,), effectName="brightness",  inName=f"./batch/{raw_img}", outName=f"./batch_output/{raw_img}")
                    # Vimage.brightness_contrast(brightness=value1, contrast=0)
                    # Vimage.save(filename=outName)
                elif effect["effect"] == "highlights":
                    print("processing highlghts on"+ str(raw_img))
                    ratio1 = effect["value1"]
                    ratio2 = effect["value2"]
                    
                    # Vimage = wandImage(filename=f"./batch_output/{raw_img}")
                    # Vimage.brightness_contrast(brightness=value1, contrast=0)
                    applyEffect(*(ratio1,ratio2), effectName="highlights", inName=f"./batch/{raw_img}", outName=f"./batch_output/{raw_img}")
                    # Vimage.save(filename=f"./batch_output/{raw_img}")
                elif effect["effect"] == "contrast":
                    print("processing contrast on"+ str(raw_img))
                    value1 = effect["value1"]
                    
                    # Vimage = wandImage(filename=f"./batch_output/{raw_img}")
                    # Vimage.brightness_contrast(brightness=value1, contrast=0)
                    applyEffect(*(value1,), effectName="contrast", inName=f"./batch/{raw_img}", outName=f"./batch_output/{raw_img}")
                    # Vimage.save(filename=f"./batch_output/{raw_img}")
                elif effect["effect"] == "exposure":
                    print("processing exposure on"+ str(raw_img))
                    value1 = effect["value1"]
                    
                    # Vimage = wandImage(filename=f"./batch_output/{raw_img}")
                    # Vimage.brightness_contrast(brightness=value1, contrast=0)
                    applyEffect(*(value1,), effectName="exposure", inName=f"./batch/{raw_img}", outName=f"./batch_output/{raw_img}")
                    # Vimage.save(filename=f"./batch_output/{raw_img}")
                elif effect["effect"] == "saturation":
                    print("processing saturation on"+ str(raw_img))
                    value1 = effect["value1"]
                    
                    # Vimage = wandImage(filename=f"./batch_output/{raw_img}")
                    # Vimage.brightness_contrast(brightness=value1, contrast=0)
                    applyEffect(*(value1,), effectName="saturation", inName=f"./batch/{raw_img}", outName=f"./batch_output/{raw_img}")
                    # Vimage.save(filename=f"./batch_output/{raw_img}")
                elif effect["effect"] == "warmth":
                    print("processing warmth on"+ str(raw_img))
                    value1 = effect["value1"]                    
                    # Vimage = wandImage(filename=f"./batch_output/{raw_img}")
                    # Vimage.brightness_contrast(brightness=value1, contrast=0)
                    applyEffect(*(value1,), effectName="warmth", inName=f"./batch/{raw_img}", outName=f"./batch_output/{raw_img}")
                    # Vimage.save(filename=f"./batch_output/{raw_img}")
                elif effect["effect"] == "special tint":
                    print("processing special tint on"+ str(raw_img))
                    valueR = effect["valueR"]                    
                    valueG = effect["valueG"]                    
                    valueB = effect["valueB"]                    
                    applyEffect(*(valueR,valueG,valueB), effectName="special tint", inName=f"./batch/{raw_img}", outName=f"./batch_output/{raw_img}")
                    # Vimage.save(filename=f"./batch_output/{raw_img}")
                elif effect["effect"] == "grayscale":
                    print("processing grayscale on"+ str(raw_img))
                    value1 = effect["value1"]                    
                    applyEffect(*(value1,), effectName="grayscale", inName=f"./batch/{raw_img}", outName=f"./batch_output/{raw_img}")
                    # Vimage.save(filename=f"./batch_output/{raw_img}")

    for sel_i in VbatchList.curselection():
        print(VbatchList.get(sel_i))
        

    # for effect in stackedEffect:
    #     if effect["effect"] = "brightness":
    #         Vimage.brightness_contrast(brightness=l_br, contrast=0)

    #             Vimage = wandImage(filename=r"./temp/current.jpg")
    #     l_br = Vscale_br_val.get() # l_br is local brightness
    #     Vimage.save(filename=r"./temp/current.jpg")
    #     print(l_br)
        # ===== endleftcrop




        # endappendjson        


        # ===== endupdateimagelabel



        
        


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
    elif activeEffectDisplay == "special tint":
        frameEffect_sptint.grid(row=1,column=1)
    elif activeEffectDisplay == "grayscale":
        frameEffect_spgray.grid(row=1,column=1)

        
#delete
def VupdateImageLabel():
    global VmainImage, VlabelImage

    try:
        Vimage = PILimage.open(r"./temp/current.jpg")
        Vimage.thumbnail((500,500))
        VmainImage = ImageTk.PhotoImage(Vimage)
        VlabelImage.config(image=VmainImage)

        
        Vimage = wandImage(filename=r"./temp/current.jpg")
        textInfo = f"Image size: {Vimage.size}\n \
        Image depth: {Vimage.depth}\n \
        Image colorspace: {Vimage.colorspace}\n \
        Has alpha channel: {Vimage.alpha_channel}"
        VlabelInfo.config(text=textInfo)
        

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
VeffectList['values'] = ["brightness", "highlights", "contrast", "exposure", "saturation", "warmth", "special tint", "grayscale"]
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


VlabelInfo = tkinter.Label(window, text="Some image details")
VlabelInfo.grid(row=0, column=2)


# w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
# w.pack()



# we are not using VbatchChosen, and no function binded to event
frame_batch = tkinter.Frame(window) # 
frame_batch.grid(row=1,column=0,padx=10,pady=10, rowspan=10)
VbatchChosen = tkinter.StringVar()
VbatchList = tkinter.Listbox(frame_batch, height=10, selectmode=tkinter.MULTIPLE, yscrollcommand=True)
VbatchList.pack()
VbatchButton = tkinter.Button(frame_batch, text='Batch effect', command=lambda:Vbatch_event())
VbatchButton.pack(padx=10,pady=10)
#endarrangelistboxandbutton

VbatchValues = getBatchPics()
VbatchList.insert(tkinter.END, *VbatchValues)
# VbatchList.bind("<<ComboboxSelected>>")
#endeventlistboxandbutton


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

frameEffect_sptint = tkinter.Frame(window) # frameEffect_sptint is frame warmth
frameEffect_sptint.grid(row=1,column=1,rowspan=10)
Vlabel_sptint = tkinter.Label(frameEffect_sptint, text=f"warmth (below 50 is colder)")
Vlabel_sptint.pack(padx=10,pady=(10,0))
Vscale_sptintR = tkinter.Scale(frameEffect_sptint, from_=0, to=100, orient='horizontal', variable=Vscale_sptintR_val)
Vscale_sptintR.set(0)
Vscale_sptintR.pack(padx=10,pady=(0,10))
Vscale_sptintG = tkinter.Scale(frameEffect_sptint, from_=0, to=100, orient='horizontal', variable=Vscale_sptintG_val)
Vscale_sptintG.set(0)
Vscale_sptintG.pack(padx=10,pady=(0,10))
Vscale_sptintB = tkinter.Scale(frameEffect_sptint, from_=0, to=100, orient='horizontal', variable=Vscale_sptintB_val)
Vscale_sptintB.set(0)
Vscale_sptintB.pack(padx=10,pady=(0,10))
tkinter.Button(frameEffect_sptint, text='Exposure', command=lambda:Vsptint_event()).pack(padx=10,pady=10)
frameEffect_sptint.grid_forget()
# frameEffect_sptint is frame contrast
#endsptint


frameEffect_spgray = tkinter.Frame(window) # frameEffect_spgray is frame warmth
frameEffect_spgray.grid(row=1,column=1,rowspan=10)
Vlabel_spgray = tkinter.Label(frameEffect_sptint, text=f"warmth (below 50 is colder)")
Vlabel_spgray.pack(padx=10,pady=(10,0))
Vscale_spgray = tkinter.Scale(frameEffect_spgray, from_=0, to=100, orient='horizontal', variable=Vscale_spgray_val)
Vscale_spgray.set(50)
Vscale_spgray.pack(padx=10,pady=(0,10))
tkinter.Button(frameEffect_spgray, text='GRayscale', command=lambda:Vspgray_event()).pack(padx=10,pady=10)
frameEffect_spgray.grid_forget()
# frameEffect_spgray is frame contrast
#endsptint







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



