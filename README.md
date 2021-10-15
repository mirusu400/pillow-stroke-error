# pillow-stroke-error
A checker for pillow stroke error

# Error resolved!
The pillow team resolved this error and merged into main branch (https://github.com/python-pillow/Pillow/pull/5761), You'll resolve this issue after `pillow >= 8.4.0` 😍

# What is stroke error?
When we draw a font with specific font, it gets `invaild argument` Error.
```
Traceback (most recent call last):
  File "C:\Users\User\Documents\_github\drawfontimage\core.py", line 180, in create
    draw.text(
  File "C:\Users\User\AppData\Local\Programs\Python\Python39\lib\site-packages\PIL\ImageDraw.py", line 457, in text
    draw_text(stroke_ink, stroke_width)
  File "C:\Users\User\AppData\Local\Programs\Python\Python39\lib\site-packages\PIL\ImageDraw.py", line 408, in draw_text
    mask, offset = font.getmask2(
  File "C:\Users\User\AppData\Local\Programs\Python\Python39\lib\site-packages\PIL\ImageFont.py", line 676, in getmask2
    self.font.render(
OSError: invalid argument
```
But I don't know which font gets error, so I just make simple test scripts to check even the font gets error.

# Usage
```
python3 test.py
```

# In my case..
```
Your OS version: Windows-10-10.0.17763-SP0
Your Python version: 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)]
Your pillow version: 8.3.2
Press start to test
Trying arial.ttf...     is nice!
Trying arialbd.ttf...   is nice!
Trying arialbi.ttf...   is nice!
Trying ariali.ttf...    is nice!
Trying ARIALN.TTF...    is nice!
Trying ARIALNB.TTF...   is nice!
Trying ARIALNBI.TTF...  is nice!
Trying ARIALNI.TTF...   is nice!
Trying ariblk.ttf...    is nice!
Trying batang.ttc...    Error: invalid argument
Trying calibri.ttf...   Error: invalid argument
Trying calibrib.ttf...  Error: invalid argument
Trying calibrii.ttf...  Error: invalid argument
Trying calibril.ttf...  is nice!
Trying calibrili.ttf... is nice!
Trying calibriz.ttf...  Error: invalid argument
Trying comic.ttf...     is nice!
Trying comicbd.ttf...   is nice!
Trying comici.ttf...    is nice!
Trying comicz.ttf...    is nice!
Trying GOTHIC.TTF...    is nice!
Trying GOTHICB.TTF...   is nice!
Trying GOTHICBI.TTF...  is nice!
Trying GOTHICI.TTF...   is nice!
Trying gulim.ttc...     Error: invalid argument
Trying malgun.ttf...    is nice!
Trying malgunbd.ttf...  is nice!
Trying malgunsl.ttf...  is nice!
```

# Solution?
`Python 3.8` with `pillow==7.2.0` **PERFECTLY** works.
```
Your OS version: Windows-10-10.0.17763-SP0
Your Python version: 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
Your pillow version: 7.2.0
Press start to test
Trying arial.ttf...	is nice!
Trying arialbd.ttf...	is nice!
Trying arialbi.ttf...	is nice!
Trying ariali.ttf...	is nice!
Trying ARIALN.TTF...	is nice!
Trying ARIALNB.TTF...	is nice!
Trying ARIALNBI.TTF...	is nice!
Trying ARIALNI.TTF...	is nice!
Trying ariblk.ttf...	is nice!
Trying batang.ttc...	is nice!
Trying calibri.ttf...	is nice!
Trying calibrib.ttf...	is nice!
Trying calibrii.ttf...	is nice!
Trying calibril.ttf...	is nice!
Trying calibrili.ttf...	is nice!
Trying calibriz.ttf...	is nice!
Trying comic.ttf...	is nice!
Trying comicbd.ttf...	is nice!
Trying comici.ttf...	is nice!
Trying comicz.ttf...	is nice!
Trying GOTHIC.TTF...	is nice!
Trying GOTHICB.TTF...	is nice!
Trying GOTHICBI.TTF...	is nice!
Trying GOTHICI.TTF...	is nice!
Trying gulim.ttc...	is nice!
Trying malgun.ttf...	is nice!
Trying malgunbd.ttf...	is nice!
Trying malgunsl.ttf...	is nice!
```

# Reason
I don't know. please help.
