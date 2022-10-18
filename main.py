import telegram_send
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "C:\Other\chromedriver.exe" # can be either "/" or "\"

# set as headless base on demand, but Epic required some headers, so headless will bring an error on this
options = Options()
# options.add_argument("--headless")
# options.add_argument('--disable-gpu') 

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
# driver.maximize_window()
driver.get("https://store.epicgames.com/en-US/")

free_game_section = driver.find_elements(By.CLASS_NAME, "css-11xvn05") # get the free game section division
for free_game in free_game_section: # check the "free game" text
    print(free_game.text)
    
number_of_free_game = len(free_game_section) # check the number of "free game" text
print(f"There are {number_of_free_game} free games in this week.")

free_game_counter = 0 # for counting the free game in iterating
telegram_send.send(messages=[f"Hey Simon! 👨‍💻\nThere are {number_of_free_game} free games this in week! Don't forget to grab it!\nClick the link below to get them.\nhttps://store.epicgames.com/en-US/"])
free_game_tags = driver.find_elements(By.CSS_SELECTOR, ".css-1myhtyb img") # get the free game <img> tag to read its title and image source 
free_game_links = driver.find_elements(By.CSS_SELECTOR, ".css-1myhtyb a") # get the free game <a> link for its webpage link
for free_game_title in free_game_tags[:number_of_free_game]: # iterate over the `free_game_tags` list
    game_title = free_game_title.get_attribute("alt") # get the value of alt attribute
    game_image_src = free_game_title.get_attribute("src") # get the value of srt attribute
    game_link = free_game_links[free_game_counter].get_attribute("href") # get the game link from `free_game_link` list
    print(game_title)
    print(game_image_src)
    print(game_link)
    free_game_counter += 1 
    telegram_send.send(messages=[f"{free_game_counter}. {game_title}\n\nImage source:\n{game_image_src}\n\nAccess the game webpage here:\n{game_link}"]) 

driver.quit()
