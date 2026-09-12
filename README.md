# Najaf Prayer Times Scraper

This script scrapes prayer times from the Najaf website for two cities: **London** and **Birmingham**. It uses the `requests` library to fetch the HTML content and `BeautifulSoup` to parse it. It also uses `customtkinter` to create a simple GUI for displaying the prayer times.

---

## Motivation

I just installed Firefox (switched from Chrome) – every time I opened the Najaf website, it would open in Arabic on the wrong city, and Firefox never learns my preferences. I was getting annoyed, so I decided to make a script that would scrape the prayer times instead. It includes two cities, because uni and home. So I done this one night before a Brawlhalla sesh.

---

## Customization

If you want to change the cities, you can do so by changing the `CITY1_URL` and `CITY2_URL` variables at the top of the script (strictly Najaf.org). Adding more cities will need a little fiddling with the code, but it's not too hard.

---

## Disclaimer

I didn't bother handling any errors, so if the website changes, the script will break.

---

## Note:

Uploading for my brethren who wish to scrape from Najaf.org.

---

## To Run (most terminals):

```bash
pip install requests
pip install beautifulsoup4
pip install customtkinter
