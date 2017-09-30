from selenium import webdriver

driver = webdriver.Firefox()
UserURL = 'PUT YOUR PROFILE URL HERE' #Example: http://cinderella.pro/user/USERID/USERNAME/
driver.get(UserURL)

ownedCards = driver.find_elements_by_xpath('//*[contains(@id, "ownedcard")]')

NameArray = []
URLArray = []
ColorArray = []
SkillArray = []
VocalArray = []
VisualArray = []
DanceArray = []

def findMax(vocal, visual, dance):
	if((vocal > visual) & (vocal > dance)):
		return "Vocal", vocal
	elif((visual > vocal) & (visual > dance)):
		return "Visual", visual		
	elif((dance > vocal) & (dance > visual)):
		return "Dance", dance		

for card in ownedCards:
	NameArray.append(card.get_attribute('data-card-title'))

ownedCardURLs = driver.find_elements_by_xpath('//*[contains(@id, "ownedcard")]/div/div/a')

for cardURL in ownedCardURLs:
	URLArray.append(cardURL.get_attribute('href'))

for URL in URLArray:
	driver.get(URL)
	cardColor = driver.find_element_by_xpath('//*[contains(@id, "card")]').get_attribute('class')
	ColorArray.append(cardColor.rsplit(' ', 1)[1])
	try:
		skill = driver.find_element_by_xpath('/html/body/main/div/div[3]/div[1]/table[2]/tbody/tr/td[1]/p[1]').text
		SkillArray.append(skill)
	except:
		SkillArray.append('NONE')
		pass
	vocal = driver.find_element_by_xpath('/html/body/main/div/div[3]/div[1]/div[1]/div/div/div/div[3]/div[2]').text
	VocalArray.append(vocal)
	visual = driver.find_element_by_xpath('/html/body/main/div/div[3]/div[1]/div[1]/div/div/div/div[4]/div[2]').text
	VisualArray.append(visual) 
	dance = driver.find_element_by_xpath('/html/body/main/div/div[3]/div[1]/div[1]/div/div/div/div[5]/div[2]').text
	DanceArray.append(dance)

f = open('cinderella.txt', 'w', encoding='utf-8')

for index, card in enumerate(ownedCards):
	max = findMax(VocalArray[index], VisualArray[index], DanceArray[index])
	f.write(NameArray[index] + " | " + ColorArray[index] + " | " + SkillArray[index] + " | Highest: " + max[0] + " (" + max[1] + ")" + "\n")  
 
f.close()