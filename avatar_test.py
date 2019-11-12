import webbrowser
import random
import os
import subprocess

valid_tops = ["NoHair", "Eyepatch", "Hat", "Hijab", "WinterHat3", "LongHairBigHair", "LongHairBob", "LongHairBun", "LongHairFro", "ShortHairShortFlat", "ShortHairDreads01", "LongHairStraight"]
valid_accessories = ["Blank", "Kurt", "Prescription01", "Prescription02", "Wayfarers"]
valid_hair_color = ["Auburn", "Black", "Blonde", "BlondeGolden", "Brown", "BrownDark", "PastelPink", "Platinum", "Red", "SilverGray"]
valid_facial_hair = ["Blank", "BeardMedium", "BeardLight", "BeardMajestic", "MoustacheFancy", "MoustacheMagnum"]
valid_clothes = ["BlazerSweater", "BlazerShirt", "CollarSweater", "GraphicShirt", "Hoodie", "Overall", "ShirtCrewNeck", "ShirtScoopNeck", "ShirtVNeck"]
valid_fabric_color = ["Black", "Blue01", "Blue02", "Blue03", "Gray01", "Gray02", "Heather", "PastelGreen", "PastelBlue", "PastelOrange", "PastelYellow", "PastelRed", "Pink", "Red", "White"]
valid_eyes = ["Close", "Cry", "Default", "Dizzy", "EyeRoll", "Happy", "Hearts", "Side", "Squint", "Surprised", "Wink", "WinkWacky"]
valid_eyebrow = ["Angry", "AngryNatural", "Default", "DefaultNatural", "FlatNatural", "RaisedExcited", "RaisedExcitedNatural", "SadConcerned", "SadConcernedNatural", "UnibrowNatural", "Updown", "UpdownNatural"]
valid_mouth = ["Concerned", "Default", "Disbelief", "Eating", "Grimace", "Sad", "ScreamOpen", "Serious", "Smile", "Tongue", "Twinkle", "Vomit"]
valid_skin = ["Tanned", "Yellow", "Pale", "Light", "Brown", "DarkBrown", "Black"]

class avatar:
    def __init__(self, top="", accessories="", hair_color="", facial_hair="", clothes="", fabric_color="", eyes="", eyebrow="", mouth="", skin=""):
        if (top not in valid_tops):
            self.top = random.choice(valid_tops)
        else: self.top = top
        if (accessories not in valid_accessories):
            self.accessories = random.choice(valid_accessories)
        else: self.accessories = accessories
        if (hair_color not in valid_hair_color):
            self.hair_color = random.choice(valid_hair_color)
        else: self.hair_color = hair_color
        if (facial_hair not in valid_facial_hair):
            self.facial_hair = random.choice(valid_facial_hair)
        else: self.facial_hair = facial_hair
        if (clothes not in valid_clothes):
            self.clothes = random.choice(valid_clothes)
        else: self.clothes = clothes
        if (fabric_color not in valid_fabric_color):
            self.fabric_color = random.choice(valid_fabric_color)
        else: self.fabric_color = fabric_color
        if (eyes not in valid_eyes):
            self.eyes = random.choice(valid_eyes)
        else: self.eyes = eyes
        if (eyebrow not in valid_eyebrow):
            self.eyebrow = random.choice(valid_eyebrow)
        else: self.eyebrow = eyebrow
        if (mouth not in valid_mouth):
            self.mouth = random.choice(valid_mouth)
        else: self.mouth = mouth
        if (skin not in valid_skin):
            self.skin = random.choice(valid_skin)
        else: self.skin = skin

    def construct_html(self):
        return "<img src='https://avataaars.io/?avatarStyle=Transparent&topType=" + self.top + "&accessoriesType=" + self.accessories + "&hairColor=" + self.hair_color +"&facialHairType=" + self.facial_hair +"&clotheType=" + self.clothes +"&clotheColor=" + self.fabric_color +"&eyeType=" + self.eyes +"&eyebrowType=" + self.eyebrow +"&mouthType=" + self.mouth +"&skinColor=" + self.skin + "'/>"

    def open_avatar(self, file):
        f = open(file, "w")
        f.write(self.construct_html())
        f.close()
        url = 'file://' + os.path.realpath(file)
        browser = webbrowser.get("safari")
        browser.open(url)

def prompt_user_for_avatar():
    print("Generating a personalized avatar. Please describe yourself.")
    print("Choose a hairstyle from the following list. And you'd better choose carefully, because even a typo will cause your body to take on a random attribute which, much like life, you cannot control.")
    print(*valid_tops, sep = ", ")
    top = input("-> ")

    print("Choose a hair color. Be honest, now...")
    print(*valid_hair_color, sep = ", ")
    hair_color = input("-> ")

    print("Now choose an eye style from the list:")
    print(*valid_eyes, sep = ", ")
    eyes = input("-> ")

    print("You know the drill... time for an eyebrow style:")
    print(*valid_eyebrow, sep = ", ")
    eyebrow = input("-> ")

    print("MWAH! Pick a mouth shape!")
    print(*valid_mouth, sep = ", ")
    mouth = input("-> ")

    print("Somehow this computer can only comprehend 7 skin tones. Now you have to pick one.")
    print(*valid_skin, sep = ", ")
    skin = input("-> ")

    print("Get! Some! Bling!")
    print(*valid_accessories, sep = ", ")
    accessories = input("-> ")

    print("I know you want a beard: ")
    print(*valid_facial_hair, sep = ", ")
    facial_hair = input("-> ")

    print("The KEY to any wardrobe is: ")
    print(*valid_clothes, sep = ", ")
    clothes = input("-> ")

    print("And finally, choose a fabric color:")
    print(*valid_fabric_color, sep = ", ")
    fabric_color = input("-> ")

    return avatar(top, accessories, hair_color, facial_hair, clothes, fabric_color, eyes, eyebrow, mouth, skin)

    

    

    

file = "avatar.html"
#my_avatar = prompt_user_for_avatar()
my_avatar = avatar()
my_avatar.open_avatar(file)
with open('browser.sh', 'rb') as file:
    script = file.read()
subprocess.call(script, shell=True)