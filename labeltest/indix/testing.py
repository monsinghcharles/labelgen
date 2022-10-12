import PIL

name = "asdf"


def RemoveOccasion(name):
    name = name.replace("<HBD>", "")
    name = name.replace("<HAA>", "")
    name = name.replace("<IRO>", "")
    return name

if name.find("<HBD>") != -1:
    fp = open(hbd_path, "rb")
    CH = 177
    LH = len(name)
    Ltype = 1
    if LH < 17:
        W = 190
        Lng = 16
    if LH > 17:
        W = 130
        Lng = 24
    if LH > 57:
        W = 100
        Lng = 31
elif name.find("<HAA>") != -1:
    fp = open(anni_path, "rb")
    CH = 177
    LH = len(name)
    Ltype = 1
    if LH < 17:
        W = 190
        Lng = 16
    if LH > 17:
        W = 130
        Lng = 24
    if LH > 57:
        W = 100
        Lng = 31
elif name.find("<IRO>") != -1:
    fp = open(iro_path, "rb")
    CH = 177
    LH = len(name)
    Ltype = 1
    if LH < 17:
        W = 190
        Lng = 16
    if LH > 17:
        W = 130
        Lng = 23
    if LH > 57:
        W = 100
        Lng = 31
else:
    fp = open(wlf_path, "rb")
    LH = len(name)
    CH = 77
    Ltype = 0
    if LH < 33:
        W = 190
        Lng = 16
    if LH > 32:
        W = 130
        Lng = 24
    if LH > 72:
        W = 100
        Lng = 31

wrname = RemoveOccasion(name)
name = name.upper()
# print(wrname)

if name.isascii() is False:

    para = textwrap.wrap(wrname, width=Lng)
    MAX_W, MAX_H = 2000, 1000
    wim = PIL.Image.open(white_path)
    draw = ImageDraw.Draw(wim)
    current_h = 0
    current_h, pad = CH, -5

    Lng = 1000
    font = ImageFont.truetype(arial_path, W)

    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font, fill=(0, 0, 0))
        current_h += h + pad
    wim = trim(wim)

    # fp = open("wlf.png", "rb")
    im = PIL.Image.open(fp)

    if Ltype == 0:
        wim = resize_with_padding(wim, (1207, 329))
        im.paste(wim, (18, 100))
    if Ltype == 1:
        wim = resize_with_padding(wim, (1207, 246))
        im.paste(wim, (18, 184))

    # im.show()

else:

    para = textwrap.wrap(wrname, width=Lng)
    MAX_W, MAX_H = 2000, 1000
    wim = PIL.Image.open(white_path)
    draw = ImageDraw.Draw(wim)
    current_h = 0
    current_h, pad = CH, -5

    Lng = 1000
    font = ImageFont.truetype(bebas_path, W)

    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font, fill=(0, 0, 0))
        current_h += h + pad
    wim = trim(wim)
    # wim = resize_with_padding(wim, (1207, 329))

    # fp = open("wlf.png", "rb")
    im = PIL.Image.open(fp)

    if Ltype == 0:
        wim = resize_with_padding(wim, (1207, 329))
        im.paste(wim, (18, 100))
    if Ltype == 1:
        wim = resize_with_padding(wim, (1207, 246))
        im.paste(wim, (18, 184))

# im.paste(qrimg,(0,438))
im.paste(qrimg, (25, 465))
print(wrname)
im.save(f'{temp_dir}/{y}.pdf', optimize=True, quality=50)