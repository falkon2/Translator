from tkinter import *
from tkinter import ttk,messagebox 
import translators as ts


root = Tk()
root.geometry = "1920x1080"
root.title = "Translator"
img = PhotoImage(file = 'translator.png')
root.tk.call('wm', 'iconphoto', root._w, img)


dictionary = {
    "af": "Afrikaans",
    "as": "Assamese",
    "am": "Amharic",
    "sq": "Albanian",
    "hq": "Armenian",
    "az": "Azerbaijani",
    "ar": "Arabic",
    "be": "Belarusian",
    "ba": "Bashkir",
    "bn": "Bengali",
    "bs": "Bosnian",
    "zh-Hans": "Chinese",
    "cs": "Czech",
    "da": "Danish",
    "nl": "Dutch",
    "en": "English",
    "fi": "Finnish",
    "fr": "French",
    "de": "German",
    "el": "Greek",
    "gu": "Gujarati",
    "ht": "Haitian Creole",
    "hi": "Hindi",
    "fe": "Hebrew",
    "hu": "Hungarian",
    "id": "Indonesian",
    "ga": "Irish",
    "it": "Italian",
    "ja": "Japanese",
    "ne": "Nepali",
    "nb": "Norwegian",
    "ru": "Russian",
    "ko": "Kannada",
    "ko": "Korean",
    "te": "Telugu",
    "th": "Thai",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
}

lang_list = list(dictionary.values())
#print(lang_list)

def translate():
    output_text_box.delete(1.0, END)
    try:
        # Getting the keys
        for code, value in dictionary.items():
            if (value == input_combo_box.get()):
                original_language = code
                
        
        for code, value in dictionary.items():
            if (value == output_combo_box.get()):
                converted_language = code
                
        text = input_text_box.get(1.0, END)
        print(text)
        text = ts.bing(text, from_language=original_language, to_language=converted_language)
        output_text_box.insert(1.0, text)
    except Exception as error:
        messagebox.showerror("Translator", error)

input_combo_box = ttk.Combobox(root, value =lang_list )
input_combo_box.config(width = 40)
input_combo_box.current(9)
input_text_box = Text(root, width = 100, height = 15)


output_combo_box = ttk.Combobox(root, value =lang_list )
output_combo_box.config(width = 40)
output_combo_box.current(12)
output_text_box = Text(root, width = 100, height = 15)


convert_button = Button(root, text = "Convert", command= translate)
convert_button.config(width = 40)

input_combo_box.pack()
input_text_box.pack()
output_combo_box.pack()
output_text_box.pack()
convert_button.pack()   
root.mainloop()
