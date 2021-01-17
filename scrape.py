from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import time
from get import filter_matchups

all_the_data = []

""" Set up the chrome webdriver """
PATH = r"E:\Hack The North\HackTheNorth\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.nba.com/stats/team/1610612761/boxscores/")

""" Chrome webdriver set up now """

def accept_cookies():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
    )
        element.click()
    except:
        driver.quit()

def get_games():
    games = []
    search = driver.find_elements_by_class_name("lineup")
    for t in search:
        if t.text != "MATCHUP" and t.text not in games:
            games.append(t.text)
    return games

def get_game_stats(x, game):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div/div[4]/div/div/div/div/nba-stat-table/div[2]/div[2]/table/tbody/tr[" + str(x + 1) + "]/td/a")))
        element.click()
    except:
        driver.quit()
    go_to_box_score()
    if "vs." in game:
        section = 3 
    else:
        section = 2
    # Get all the player stats in the game
    get_table(game, section)
    driver.back()
    driver.back()

def go_to_box_score():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "box-score")))
        element.click()
    except:
        driver.quit()

def get_table(game, section):
    # All the game data
    rows = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[5]/section[" + str(section) + "]/div[2]/div[2]/div/table/tbody/tr")
    print(len(rows))

    for x in range(len(rows)):
        # One player's data
        row_data = []
        row_data.append(game)
        columns = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[5]/section[" + str(section) + "]/div[2]/div[2]/div/table/tbody/tr[" + str(x + 1) + "]/td")
        
        if len(columns) == 21: # Check if they played

            for index, column in enumerate(columns): # Each stat for player
                if index == 0:
                    if "\n" in column.text:
                        row_data.append(column.text[:-2])
                    else:
                        row_data.append(column.text)
                else:
                    row_data.append(column.text)

        elif len(columns) == 2:
            for column in columns:
                row_data.append(column.text)

        all_the_data.append(row_data)
        print(row_data)

def scraper():

    accept_cookies() # Click accept cookies
    games = get_games() # get a list of all the games the team has played

    x = filter_matchups()
    CurrentWeb = len(games) #5
    CurrentDB = len(x) #4
    # print(x)
    # print(games)
    # print(CurrentDB, CurrentWeb)
    do = CurrentWeb - CurrentDB #1
    if do == 0:
        driver.quit()
    else:
        games = get_games()[:do]

    # Go through each game in the list of games
    for x, game in enumerate(games):
        get_game_stats(x, game)
        print(all_the_data)

    driver.quit()

    return all_the_data

if __name__ == '__main__':
    print(scraper())

#['JAN 16, 2021 - TOR vs. CHA', 'JAN 14, 2021 - TOR vs. CHA', 'JAN 11, 2021 - TOR @ POR', 'JAN 10, 2021 - TOR @ GSW', 'JAN 06, 2021 - TOR @ PHX', 'JAN 04, 2021 - TOR vs. BOS', 'JAN 02, 2021 - TOR @ NOP', 'DEC 31, 2020 - TOR vs. NYK', 'DEC 26, 2020 - TOR @ SAS', 'DEC 23, 2020 - TOR vs. NOP']
#['JAN 16, 2021 - TOR vs. CHA', 'JAN 14, 2021 - TOR vs. CHA', 'JAN 11, 2021 - TOR @ POR', 'JAN 10, 2021 - TOR @ GSW', 'JAN 08, 2021 - TOR @ SAC', 'JAN 06, 2021 - TOR @ PHX', 'JAN 04, 2021 - TOR vs. BOS', 'JAN 02, 2021 - TOR @ NOP', 'DEC 31, 2020 - TOR vs. NYK', 'DEC 29, 2020 - TOR @ PHI', 'DEC 26, 2020 - TOR @ SAS', 'DEC 23, 2020 - TOR vs. NOP']
