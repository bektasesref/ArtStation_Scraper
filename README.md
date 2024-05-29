# ArtStation_Scraper
 Profile scraper based on filtering biography by terms such as "3d", "vfx" etc. If gender name json by your language provided, can be filtered with gender too

Uses cloudscraper framework. Install it from pip
-------------------------------------


Change Custom Input Parameters as you want
-------------------------------------
filterKeyword: it's what you searched in artstation's search bar

bioKeywordContainList: Checklist that if the matched artists has some keyword in his bio any of these

checkGender: False/True

countryToSearch: ISO code for country. Can be found by making a search filtered with specific country and get the url on https://www.artstation.com/search/artists

checkingGender: K, E or U (female, male or unknown name). It's Turkish names only. Change it whatever language you are. Just beware of the check_gender function


-------------------------------------
GUI feature with tkinter/qt will be added at some point

Good scrapings!