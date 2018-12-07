from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

class NFLScraper:
    game_lines = []
    url = 'https://www.bovada.lv/sports/football/nfl'

    @classmethod
    def fill_games(cls):
        cls.game_lines = cls.get_weekly_lines()

    @classmethod
    def get_games_lines(cls):
        return cls.game_lines

    @classmethod
    def get_weekly_lines(cls):
        games_list = []
        options = Options()
        options.set_headless(headless=True)
        driver = webdriver.Chrome(chrome_options=options)
        print(cls.url)
        driver.get(cls.url)
        for game_element in driver.find_elements_by_class_name('coupon-content'):
            game_data = cls.parse_game_element(game_element)
            if game_data:
                games_list.append(game_data)
        driver.close()
        return games_list

    @classmethod
    def parse_game_element(cls, game_element):
        game_data = {}
        fav_index = -1
        for indx, team_element in enumerate(game_element.find_elements_by_class_name('competitor-name')):
            if 'favorite' in team_element.get_attribute("class"):
                fav_index = indx
                game_data['Favorite'] = team_element.get_attribute('innerText')
            else:
                game_data['Underdog'] = team_element.get_attribute('innerText')

        if fav_index == -1:
            return None

        spread = game_element.find_elements_by_class_name('market-line')[fav_index].get_attribute('innerText')
        game_data['Line'] = spread
        date = game_element.find_elements_by_class_name('scores')[0].get_attribute('innerText')
        format = '%m/%d/%y %I:%M %p'
        try:
            game_data['Date'] = datetime.strptime(' '.join(date.splitlines()), format)
        except ValueError:
            return None
        return game_data

