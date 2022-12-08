import time
from datetime import datetime

import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from config import x_paths_generator


class EspnScraper:
    """
    Class that scrapes the ESPN website and extracts NBA player stats
    """

    def __init__(self,
                 webdriver_location: str,
                 chrome_options: dict = None,
                 url: str = None):
        """Class related to ESPN website scraping.

        Parameters
        ----------
        webdriver_location : str
            The path of the driver.
            Currently only chrome driver supported.
        chrome_options : dict
            A dictionary with any specifics to chrome options.
        url : str
            URL to scrape, if None a custom for the current
            year will be used.
        """

        self.final_dataframe = pd.DataFrame()
        self.data_list = []
        self.webdriver_location = webdriver_location

        # if you need to specify any options for chrome, like silent scraping (without opening a chrome window)
        # or minizing, or maximizing the chrome window.
        if chrome_options is None:
            self.chrome_options = Options()  # TODO: Adjust code to accept a dictionary with chrome options

        # If url is not specified by initialization assign to the URL the current regular season
        if url is None:
            current_year = datetime.now().year
            season_type = 2  # means regular season, 3 means post season

            self.url = f"https://www.espn.com/nba/stats/player/_/season/{current_year}/seasontype/{season_type}"

        service = Service(self.webdriver_location)

        # Initiate the chrome web driver
        self.webdriver = webdriver.Chrome(service=service, options=self.chrome_options)

    def scrape_espn_page(self, season: str = None, seasontype: str = "regular") -> None:
        """
        Scrape the ESPN URL.

        Parameters
        ----------
        season : str
            The season to scrape the ESPN website.
        seasontype : str
            The type of the season, can be either
            'regular' or 'postseason'. Defaults to 'regular'.

        """

        if seasontype == "regular":
            type = 2
        elif seasontype == "postseason":
            type = 3
        else:
            raise Exception("Season type parameter can either 'regular' or 'postseason'.")

        if season is not None:
            self.url = f"https://www.espn.com/nba/stats/player/_/season/{season}/seasontype/{type}"

        self.webdriver.get(url=self.url)
        time.sleep(3)

        try:
            # Click on "Accept" for cookies
            WebDriverWait(self.webdriver, 10).until(
                ec.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()
        except:
            print("No cookies accepted")

        # Approximately 500 players total in the stats page, 50 players shown by default (50*10)
        for iter in range(1, 11):
            # Click on "Show More" to get all the player stats
            try:
                self.webdriver.find_element(by=By.XPATH,
                                            value='//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div[2]/a').click()
                time.sleep(3)
            except:
                print(f"Could not find 'Show more' element in iteration {iter}")

        early_break = 50
        concec_no_stats = 0
        flag = True

        for row in range(1, 500):

            path_dict = x_paths_generator(row=row)

            info_list = []

            for info_field in path_dict.keys():

                try:
                    # Extract all the text of a row to a list
                    info_list.append(self.webdriver.find_element(by=By.XPATH, value=path_dict[info_field]).text)

                except:

                    concec_no_stats += 1

                    if concec_no_stats >= early_break:
                        flag = False

            # Early termination no need to loop over 500 times
            if not flag:
                break

            # Append to the main list
            self.data_list.append(info_list)

            if row % 10:
                # Print all info in console every ten players
                print(info_list)

        self.final_dataframe = pd.DataFrame(self.data_list,
                                            columns=['Current_Ranking', 'Player_Name', "Team", "Position",
                                                     "Games_Played",
                                                     "Minutes_per_Game", "Points_per_Game", "Field_Goals_Made_per_Game",
                                                     "Field_Goals_Attempted_per_Game",
                                                     "Field_Goals_Percentage_per_Game",
                                                     "3Pointers_Made_per_Game", "3Pointers_Attempted_per_Game",
                                                     "3Pointers_Percentage_per_Game", "Free_Throws_Made_per_Game",
                                                     "Free_Throws_Attempted_per_Game",
                                                     "Free_Throws_Percentage_per_Game",
                                                     "Rebounds_per_Game", "Assists_per_Game", "Steals_per_Game",
                                                     "Blocks_per_Game",
                                                     "Turnovers_per_Game", "Total_Double_Doubles",
                                                     "Total_Triple_Doubles",
                                                     # "Player_Efficiency_Rating_per_Game"
                                                     ])

        self.webdriver.quit()

    def save_dataset_to_csv(self, csv_name: str = None):

        if csv_name is None:
            self.final_dataframe.to_csv('espn_player_stats.csv')
        else:
            self.final_dataframe.to_csv(f'{csv_name}.csv')


if __name__ == "__main__":

    scraper = EspnScraper(webdriver_location="C:\\Users\\adorr\\Desktop\\chromedriver_win32\\chromedriver.exe",
                          chrome_options=None,
                          url=None)

    scraper.scrape_espn_page(season="2023", seasontype="regular")

    scraper.save_dataset_to_csv(csv_name=None)
