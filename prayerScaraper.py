'''
READ ME
This script scrapes prayer times from the Najaf website for two cities: London and Birmingham.
It uses the requests library to fetch the HTML content and BeautifulSoup to parse it.
It also uses customtkinter to create a simple GUI for displaying the prayer times.
(copilot autofilled the readme very nicely lmao)

Motivation:
I just installed firefox (switched from chrome) - everytime i opened the Najaf website, it would open in arabic on the wrong city
and firefox never learns my preferences. I was getting annoyed so I decided to make a script that would scrape the prayer times instead.
Includes two cities, because uni and home.
So i done this one night before a brawlhalla sesh.

If you want to change the cities, you can do so by changing the CITY1_URL and CITY2_URL variables at the top of the script (strictly Najaf.org).
Adding more cities will need a little fiddling with the code, but it's not too hard.

I didnt bother handling any errors, so if the website changes, the script will break.

Uploading for my brethren who wish to scrape from Najaf.org


To run:
pip install requests
pip install beautifulsoup4
pip install customtkinter


'''


import requests
from bs4 import BeautifulSoup
from customtkinter import *


CITY1_URL = 'https://najaf.org/english/'
CITY2_URL = 'https://www.najaf.org/english/?city=birmingham'

def getPrayerTimes(city, url, position):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    prayer_contianer = soup.find('div', id="prayertime")

    if prayer_contianer:
        ul_element = prayer_contianer.find('ul')

        if ul_element:
            # Find all li elements within the ul
            li_elements = ul_element.find_all('li')


            if li_elements:
                cityLabel = CTkLabel(app, text=f"{city}:", font=("Arial Bold", 20))
                cityLabel.place(relx=(position), rely=0.1, anchor=CENTER)

                y_coord = 0.25

                for li in li_elements:
                    # Extract the text from each li element
                    timeSpan = li.find('span')
                    prayerTime = ""
                    prayerName = ""

                    if timeSpan:
                        prayerTime = timeSpan.get_text(strip=False)
                        fullText = li.get_text(strip=True)
                        prayerName = fullText.strip(f'{prayerTime}')
                    #print (f"{prayerName} : {prayerTime}")
                    timeLabel = CTkLabel(app, text=f"{prayerName} : {prayerTime}", font=("Arial", 16))
                    timeLabel.place(relx=(position), rely=y_coord, anchor=CENTER)
                    y_coord += 0.07


def updatePrayerTimes():
    # Clear previous labels
    for widget in app.winfo_children():
        if isinstance(widget, CTkLabel):
            widget.destroy()

    getPrayerTimes("London", CITY1_URL, 0.3)
    getPrayerTimes("Birmingham", CITY2_URL, 0.7)

if __name__ == "__main__":
    app = CTk()
    app.maxsize(450, 400)
    app.minsize(450, 400)

    # print("\nScript execution finished.")
    updatePrayerTimes()

    app.geometry("450x400")
    app.title("Prayer Times")


    btn = CTkButton(master=app, text="Update", command=updatePrayerTimes, corner_radius=32)
    btn.place(relx=0.5, rely=0.85, anchor=CENTER)

    app.mainloop()
