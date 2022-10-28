import requests
from bs4 import BeautifulSoup

source = requests.get('https://boards.greenhouse.io/embed/job_board?for=coursera').text
soup = BeautifulSoup(source,'html5lib')

opening = soup.find_all('div', {"class":"opening"})


job_list = []
for jobs in opening :
    job_desc = jobs.find('a')
    job_link = job_desc.get('href')
    job_title = job_desc.text
    job_location = jobs.find('span', {"class":"location"}).text
    

    entry = {
        'title': job_title,
        'link': job_link,
        'location': job_location
    }

    job_list.append(entry)


#print(job_list)

imp_fields = ['Job Overview:', 'Responsibilities:', 'Basic Qualifications:', 'Preferred Qualifications:', 'Job Overview']

for entry in job_list :

    job_id = entry['link'].split('=')[1]
    #print(job_id)
    link_check = 'https://boards.greenhouse.io/embed/job_app?for=coursera&token=' + job_id + '&b=https%3A%2F%2Fabout.coursera.org%2Fcareers%2Fjobs%2F'


    link_source = requests.get(link_check).text
    link_soup = BeautifulSoup(link_source,'html5lib')

    content_list = link_soup.find("div", {'id':"content"}).findChildren()

    print(entry['title'].upper())
    print('===============================')

    for i in range(len(content_list)):

        strong_tag = content_list[i].find('strong')

        if strong_tag != None and strong_tag.text in imp_fields:

            print(strong_tag.text)
            print(content_list[i+2].text)
            print('===============================')

