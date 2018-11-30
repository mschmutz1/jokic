from NFLScraper import NFLScraper

scraper = NFLScraper()
scraper.fill_games()
print(scraper.get_games_lines())