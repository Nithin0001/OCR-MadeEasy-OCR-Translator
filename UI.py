# for random name generation to save file
import random
from datetime import date
# for UI creation
from tkinter import *
from tkinter import filedialog, ttk, scrolledtext, messagebox
# for using extract & translate functions
import main
# to open hyperlink
import webbrowser

# constants
FONT_TXT_WLC = ("Poppins", 28, "bold")
FONT_TXT_PATH = ("Poppins", 18, "bold")
FONT_TXT_COMBO = ("Poppins", 15, "bold")
BG_COLOR = "#5cdb95"
FONT_COLOR = "#edf5e1"
BLUE = "#05386b"
LANGUAGES_CODE_EXTRACT = ('afr', 'amh', 'ara', 'asm', 'aze', 'bel', 'ben', 'bod', 'bos', 'bul', 'cat', 'ceb', 'ces',
                          'chi', 'chi', 'chr', 'cym', 'dan', 'deu', 'ell', 'eng', 'enm', 'epo', 'est', 'eus', 'fin',
                          'fra', 'frk', 'frm', 'grc', 'guj', 'heb', 'hin', 'hrv', 'hun', 'hye', 'iku', 'ind', 'isl',
                          'ita', 'ita', 'jav', 'jpn', 'kan', 'kat', 'kat', 'khm', 'kir', 'kmr', 'kor', 'kor', 'kur',
                          'lat', 'lav', 'lit', 'ltz', 'mal', 'mar', 'mkd', 'mlt', 'mon', 'mri', 'msa', 'mya', 'nep',
                          'nld', 'nor', 'oci', 'ori', 'pan', 'pol', 'por', 'pus', 'que', 'ron', 'rus', 'san', 'sin',
                          'slk', 'slk', 'slv', 'snd', 'spa', 'spa', 'sqi', 'srp', 'srp', 'sun', 'swa', 'swe', 'syr',
                          'tam', 'tat', 'tel', 'tgk', 'tgl', 'tha', 'tir', 'ton', 'tur', 'uig', 'ukr', 'urd', 'uzb',
                          'uzb', 'vie', 'yid', 'yor')
LANGUAGES = ('Afrikaans', 'Amharic', 'Arabic', 'Assamese', 'Azerbaijani', 'Belarusian', 'Bengali', 'Tibetan', 'Bosnian',
             'Bulgarian', 'Catalan', 'Cebuano', 'Czech', 'Chinese-Simplified', 'Chinese-Traditional', 'Cherokee',
             'Welsh', 'Danish', 'German', 'GreekModern(1453-)', 'English', 'EnglishMiddle(1100-1500)', 'Esperanto',
             'Estonian', 'Basque', 'Finnish', 'French', 'GermanFraktur', 'FrenchMiddle(ca.1400-1600)',
             'GreekAncient(to', 'Gujarati', 'Hebrew', 'Hindi', 'Croatian', 'Hungarian', 'Armenian', 'Inuktitut',
             'Indonesian', 'Icelandic', 'Italian', 'oldItalianOld', 'Javanese', 'Japanese', 'Kannada', 'Georgian',
             'oldGeorgianOld', 'Central', 'KirghizKyrgyz', 'Kurmanji(Kurdish-Latin', 'Korean', 'vert', 'Kurdish(Arabic',
             'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Malayalam', 'Marathi', 'Macedonian', 'Maltese',
             'Mongolian', 'Maori', 'Malay', 'Burmese', 'Nepali', 'Dutch;', 'Norwegian', 'Occitan(post', 'Oriya',
             'PanjabiPunjabi', 'Polish', 'Portuguese', 'PushtoPashto', 'Quechua', 'RomanianMoldavianMoldovan',
             'Russian', 'Sanskrit', 'SinhalaSinhalese', 'Slovak', 'frak', 'Slovenian', 'Sindhi', 'SpanishCastilian',
             'oldSpanishCastilianOld', 'Albanian', 'Serbian', 'latin', 'Sundanese', 'Swahili', 'Swedish', 'Syriac',
             'Tamil', 'Tatar', 'Telugu', 'Tajik', 'Tagalog(new-Filipino)', 'Thai', 'Tigrinya', 'Tonga', 'Turkish',
             'UighurUyghur', 'Ukrainian', 'Urdu', 'Uzbek', 'cyrl', 'Vietnamese', 'Yiddish', 'Yoruba')

# main frame
window = Tk()
window.title("MadeEasy OCR & Translator")
window.maxsize(1280, 800)
window.minsize(1280, 800)
icon = PhotoImage(file="/Users/nithinr/PycharmProjects/Language Translator/icon/icon6.png")
window.iconphoto(False, icon)
window.configure(bg=BG_COLOR)
empty = 0

# wlc text
wlc_txt = Label(window, text="Welcome To MadeEasy OCR & Translator", font=FONT_TXT_WLC)
wlc_txt.grid(row=0, column=1)
wlc_txt.config(foreground=BLUE, background=BG_COLOR)
select_lbl = Label(window, text="Select the Image you want to extract text from ", font=FONT_TXT_PATH)
select_lbl.grid(row=1, column=0, pady=20)
select_lbl.config(background=BG_COLOR, foreground=BLUE)

file_path = ""
label_opened_file_path = ""
lan_selected = ""

label_opened_file_path = Label(window,
                               text="                                                                                                                                                ")
label_opened_file_path.grid(row=1, column=1)
label_opened_file_path.config(background=FONT_COLOR, foreground=BLUE, borderwidth=0)


# function to open the img file
def file_open():
    global file_path
    file_path = filedialog.askopenfilename(initialdir="/", title="Select An Image",
                                           filetypes=[("Images", ".jpeg .png .jpg")])
    global label_opened_file_path
    label_opened_file_path.config(text=file_path)


info = ""
a = ("kn", "ta", "te", "ml", "hi", "en", "ja", "ar", "he")
b = ("Kannada", "Tamil", "Telugu", "Malayalam", "Hindi", "English", "Japanese", "Arabic", "Hebrew")


# extract info btn function
def extract_info():
    try:
        global info, lan_selected, empty
        text_field_from.delete("1.0", "end")
        lan = lan_extract_menu.get()
        lan_selected = lan
        lan = LANGUAGES.index(lan)
        lan = LANGUAGES_CODE_EXTRACT[lan]
        index_value = b.index(lan_selected)
        from_menu.current(index_value)
        info = "\n"
        info = info + main.img_extract(file_path, lan)
        info = info + "\n"
        text_field_from.insert('insert', info)
        empty = 1
    except:
        messagebox.showwarning("Waring", "Select the correct language!\nOR\nSelect an IMAGE!")


# translate info btn
def translate_info():
    try:
        global info, empty
        info = ""
        from_ln = from_menu.get()
        to_ln = to_menu.get()
        from_ln = a[b.index(from_ln)]
        to_ln = a[b.index(to_ln)]
        info = str(text_field_from.get(CURRENT, END))
        info = main.translate(from_ln, to_ln, info)
        info = "\n" + info + "\n"
        text_field_to.insert('insert', info)
        empty = 1
    except:
        messagebox.showwarning("Waring", "Something went wrong try Again!")


# language select combobox
style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", background=BG_COLOR)
lan_select_lbl = Label(text="Select the Language of the image", font=FONT_TXT_PATH)
lan_select_lbl.grid(row=2, column=0)
lan_select_lbl.config(background=BG_COLOR, foreground=BLUE)

lan_extract_menu = ttk.Combobox(window, values=LANGUAGES, font=FONT_TXT_COMBO, state="readonly")
lan_extract_menu.grid(row=2, column=1)
lan_extract_menu.current(43)
lan_extract_menu.configure(foreground=BLUE)

# file open btn & text extract btn
open_btn_img = PhotoImage(file=r"/Users/nithinr/PycharmProjects/Language Translator/buttons/button_open.png")
file_open_btn = Button(window, text="Open", command=file_open, image=open_btn_img)
file_open_btn.grid(row=1, column=2)
file_open_btn.config(highlightbackground=BG_COLOR)
e_btn_img = PhotoImage(file="/Users/nithinr/PycharmProjects/Language Translator/buttons/button_extract.png")
text_extract_btn = Button(window, text="Extract", command=extract_info, image=e_btn_img,
                          highlightbackground=BG_COLOR).grid(row=1, column=3)

# label
t_lbl = Label(window, text="Translation", font=FONT_TXT_PATH)
t_lbl.grid(row=3, column=0)
t_lbl.config(background=BG_COLOR, foreground=BLUE)
from_translation = Label(window, text="From")
from_translation.grid(row=4, column=0)
from_translation.config(background=BG_COLOR)
to_translation = Label(window, text="To")
to_translation.grid(row=4, column=1)
to_translation.config(background=BG_COLOR)

# from lng combobox
from_menu = ttk.Combobox(window, values=b, font=FONT_TXT_COMBO, state="readonly")
from_menu.grid(row=5, column=0)
# from_menu.current(0)
from_menu.configure(foreground=BLUE)

# to lng combobox
to_menu = ttk.Combobox(window, values=b, font=FONT_TXT_COMBO, state="readonly")
to_menu.grid(row=5, column=1)
to_menu.current(5)
to_menu.configure(foreground=BLUE)

# translate btn
t_btn_img = PhotoImage(file="/Users/nithinr/PycharmProjects/Language Translator/buttons/button_translate.png")
translate_btn = Button(window, text="Translate", command=translate_info, image=t_btn_img,
                       highlightbackground=BG_COLOR).place(x=900, y=170)

# text field from
text_field_from = scrolledtext.ScrolledText(window, width=122, height=12, font=("Poppins", 15, "bold"))
text_field_from.place(x=20, y=250)
text_field_from.config(highlightthickness=1, highlightbackground=BG_COLOR, highlightcolor=BG_COLOR, fg=BLUE,
                       bg=FONT_COLOR)

# label
translated_txt = Label(window, text="Translated", font=FONT_TXT_COMBO)
translated_txt.place(x=20, y=472)
translated_txt.config(background=BG_COLOR, fg=BLUE)

# text field to
text_field_to = scrolledtext.ScrolledText(window, width=122, height=10, font=("Poppins", 15, "bold"))
text_field_to.place(x=20, y=500)
text_field_to.config(highlightthickness=1, highlightbackground=BG_COLOR, highlightcolor=BG_COLOR, fg=BLUE,
                     bg=FONT_COLOR)


# text field content clear function
def clear_btn():
    label_opened_file_path.config(
        text="                                                                                                                                                ")
    text_field_from.delete("1.0", "end")
    text_field_to.delete("1.0", "end")
    global file_path, empty
    file_path = ""
    empty = 0


# text field content save in a file function
def save_txt():
    if empty == 0:
        messagebox.showwarning("Warning", "No Text to Save!")
    else:
        try:
            today = "/Users/nithinr/Desktop/"
            today = today + str(date.today())
            r = random.randint(1000, 10000)
            today = today + str(r) + ".txt"
            text_field_info = text_field_from.get("1.0", "end")
            text_field_info += text_field_to.get("1.0", "end")
            file = open(today, "w")
            file.write(text_field_info)
            file.close()
        except:
            messagebox.showwarning("Waring", "Something went wrong try again!")


# clear btn
c_btn_img = PhotoImage(file="/Users/nithinr/PycharmProjects/Language Translator/buttons/button_clear-3.png")
clear_btn = Button(window, text="Clear", command=clear_btn, image=c_btn_img, highlightbackground=BG_COLOR)
clear_btn.place(x=20, y=700)

# save btn
s_btn_img = PhotoImage(file="/Users/nithinr/PycharmProjects/Language Translator/buttons/button_save-as-text-2.png")
save_txt_btn = Button(window, text="Save As Text", command=save_txt, image=s_btn_img,
                      highlightbackground=BG_COLOR).place(x=100, y=700)


# # open browser
# def callback(url):
#     webbrowser.open_new(url)
#
#
# # API urls
# about_url_tesseract = "https://opensource.google/projects/tesseract"
# about_url_google_translate = "https://cloud.google.com/translate"
#
# # label with hyperlink
# about_url_tesseract_lbl = Label(text="Tesseract", fg="#05386b", cursor="hand2")
# about_url_tesseract_lbl.place(x=1000, y=700)
# about_url_tesseract_lbl.config(background=BG_COLOR)
# about_url_tesseract_lbl.bind("<Button-1>", lambda e: callback(about_url_tesseract))
#
# # label with hyperlink
# about_url_google_translate_lbl = Label(text="Google API", fg="#05386b", cursor="hand2")
# about_url_google_translate_lbl.place(x=1100, y=700)
# about_url_google_translate_lbl.config(background=BG_COLOR)
# about_url_google_translate_lbl.bind("<Button-1>", lambda e: callback(about_url_google_translate))
#
# # app info
# about = "Created by Nithin. API's used Tesseract, Google Translation API. OS - macOS Monterey.\nIt will extract and translate all the languages supported by Tesseract. Python's Tkinter Module used for UI design. Not a MACHINE LEARNING APP!!!"
#
# # label
# info_txt_lbl = Label(window, text=about, font=FONT_TXT_COMBO)
# info_txt_lbl.place(x=20, y=725, )
# info_txt_lbl.config(background=BG_COLOR, foreground=FONT_COLOR)

# exit btn
exit_btn_img = PhotoImage(file="/Users/nithinr/PycharmProjects/Language Translator/buttons/button_exit-2.png")
exit_btn = Button(window, text="Exit", command=window.destroy, image=exit_btn_img, highlightbackground=BG_COLOR).grid(
    row=0, column=3)

lan_img = PhotoImage(file="/Users/nithinr/PycharmProjects/Language Translator/img/lan_img.png")
canvas = Canvas(window, width=1000, height=200, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=300, y=700)
canvas.create_image(0, 0, image=lan_img, anchor=NW)

window.mainloop()
