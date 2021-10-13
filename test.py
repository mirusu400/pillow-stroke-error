
from PIL import Image, ImageDraw, ImageFont, ImageOps
import PIL
import os
import sys
import platform



def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
 
def draw(fname, oname):
    img = Image.new("RGBA", (100, 100), color=(255, 255, 255, 255))
    fnt = ImageFont.truetype(fname, 16)

    draw = ImageDraw.Draw(img)
    text="This is test."
    draw.text(
        (0, 0),
        text,
        fill=(0,0,0,255),
        font=fnt,
        anchor="la",
        stroke_width=2,
        stroke_fill=(255,255,255,255)
    )

    img.save(oname)

def check(dirname):
    print(f"Your OS version: {platform.platform()}")
    print(f"Your Python version: {sys.version}")
    print(f"Your pillow version: {PIL.__version__}")
    input("Press start to test")
    try:
        os.mkdir("./output")
    except:
        pass
    filenames = os.listdir(dirname)
    for filename in filenames:
        fontname = os.path.join(dirname, filename)
        outputname = "./output/" + filename.split(".")[0] + ".png"
        print(f"Trying {filename}...", end="\t")
        try:
            draw(fontname, outputname)
        except OSError as e:
            print("Error:", e)
            continue
        print("is nice!")

if __name__ == "__main__":
    check("./fonts/")
    exit()
