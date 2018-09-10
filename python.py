#importing required libraries
from bs4 import BeautifulSoup
import urllib.request
import csv

#specifying the url
url_page = 'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

#querying the website and returning the html to the following variable
html_of_page = urllib.request.urlopen(url_page)

#parsing the html obtained using BEAUTIFUL SOUP and storing it in another variable 
soup = BeautifulSoup(html_of_page,'html.parser')


####print(soup)  
#this will print the parsed html of the website

#at this point if there's an error or 'soup' variable is empty, then request hasnt been successful
#it is a good idea to implement error handling here - urllib.error



# find results within the table
table = soup.find('table',attrs={'class':'tableSorter'})
results = table.find_all('tr')

print('number of results is :- ', len(results))



#creating & writing headers to a list data structure
rows = []
rows.append(['Rank','Company name','Webpage','Description','Location','Year end','Annual sales rise over 3 years','Sales','Staff','Comments'])
###print(rows)



#looping over the results
for result in results:
	#findingall columns as per result
	data = result.find_all('td')
	#checking that columns indeed have some data
	if len(data) == 0:
		continue

	#now write the columns into variables
	rank = data[0].getText()
	company = data[1].getText()
	location = data[2].getText()
	yearend = data[3].getText()
	salesrise = data[4].getText()
	sales = data[5].getText()
	staff = data[6].getText()
	comments = data[7].getText()

###	print('company is',company)
###	print('sales',sales)

	
	#extracting description from the company name
	company_name = data[1].find('span',attrs={'class':'company-name'}).getText()
	company_description = company.replace(company_name,'')

	#removing unwantedsybols/characters from sales
	sales = sales.strip('*').strip('†').replace(',','')


	#going to the link and extracting the company's website
	url = data[1].find('a').get('href')
	page = urllib.request.urlopen(url)

	#again parsing the html
	soup = BeautifulSoup(page,'html.parser')
	#finding the ;ast result ion the table and getting the link
	try:
		table_row = soup.find('table').find_all('tr')[-1]
		webpage = table_row.find('a').get('href')
	except:
		webpage = None
	#i am using try-except condition in case a url is not found
	
	# write each result to rows
	rows.append([rank, company_name, webpage, company_description, location, yearend, salesrise, sales, staff, comments])

for i in rows:
	print(i)
#or just - print(rows) to get a dirty looking list


#Create a csv and write rows to this file
with open('techtrack100.csv','w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)