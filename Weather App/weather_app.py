from tkinter import *
import requests

url = 'https://api.openweathermap.org/data/3.0/onecall?lattitude={lattitude}&lon={lon}&exclude={part}&appid={API key}'
def get_weather(lattitude, longitude):
    result = requests.get(url.format(lattitude, longitude, '', '2a2f3f5f7828274647633dc6d6b77617'))
    if result:
        print(result.content)
    else:
        return None

print(get_weather("37.783798", "-121.545258"))

def search():
    pass
app = Tk()
app.title("Control Alt Elite Clan")
app.geometry('700x400')

city_text = StringVar()
city_entry = Entry(app,textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Search", width=12, command=search)
search_btn.pack()

location_label = Label(app, text='', font=('bold',20))
location_label.pack()

image = Label(app, bitmap='')
image.pack()

temp_lbl = Label(app, text="")
temp_lbl.pack()


app.mainloop()