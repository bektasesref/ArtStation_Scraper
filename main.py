#region Imports
import cloudscraper
import json
import time
from datamodels import Artist
#endregion

#region Custom Input Parameters
filterKeyword = "Artist"
bioKeywordContainList = ["fx","effect","visual","shader","vfx"]
checkGender = False
countryToSearch = "TR" # iso code of country
checkingGender = "K" #K for female, E for male, U for unknown. Name wordlist is Turkish names only. Change it as you like
#endregion

#region Global Parameters
url = "https://www.artstation.com/api/v2/search/users.json?page={page}&per_page=30&query=" + filterKeyword +"&filters=[{%22field%22:%22countries%22,%22method%22:%22include%22,%22value%22:[%22"+countryToSearch+"%22]}]"

with open("isimler.json", "r", encoding="utf-8") as file:
    names = json.load(file)

name_gender_dict = {item["name"]: item["sex"] for item in names}
#endregion
def check_gender(name):
    gender = name_gender_dict.get(name)
    if gender is not None:
        return gender
    else:
        return "U"


def scrape():
    scraper = cloudscraper.create_scraper()
    current_page = 1
    total_page = 1

    while current_page <= total_page:
        #print(f"Scraping page {current_page} of {total_page}")
        response = scraper.get(url.replace("{page}", str(current_page)))
        text = response.text
        #print(url.replace("{page}", str(current_page)))
        #print(text)
        try:
            json_obj = json.loads(text)
            total_count = json_obj["total_count"]
            total_page = total_count // 30
            artists = [Artist(data) for data in json_obj["data"]]
            for artist in artists:
                artist.headline_lowered = str(artist.headline).lower()
                if any(keyword in artist.headline_lowered for keyword in bioKeywordContainList):
                    if checkGender:
                        for splitted in artist.full_name.split(' '):
                            gender = check_gender(splitted)
                            if gender == checkingGender:
                                print("Artist: " + str(artist.__dict__))
                                continue
                    else:
                        print(
                            f"Artist Name: {artist.full_name}, Headline: {artist.headline}, Link: https://artstation.com/{artist.username}. Page: {current_page}/{total_page}")
            current_page += 1
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)
    print("Finished")


if __name__ == '__main__':
    scrape()