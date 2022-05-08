from bs4 import BeautifulSoup

import requests 
url="https://www.programmableweb.com/category/tools/apis"
no_of_rows=0
job_dict={}
while True:
  response = requests.get(url)
  data = response.text
  soup = BeautifulSoup(data,'html.parser')
  html=soup.find_all('tr')
  for data in html:
    Names=data.find_all('td',{'class':'views-field views-field-pw-version-title'})
    Descriptions=data.find_all('td',{'class':'views-field views-field-search-api-excerpt views-field-field-api-description hidden-xs visible-md visible-sm col-md-8'})
    Categories=data.find_all('td',{'class':'views-field views-field-field-article-primary-category'})
    for Name in Names:
      print(Name.find('a').text,end=",")
      print(Name.find('a').get('href'),end=",")
      for Category in Categories:
        cat=Category.find('a')
        print(cat.text if cat else "N/A",end=",")
        for Description in Descriptions:
          print(Description.text)
  url_tag = soup.find('a',{'title':'Go to next page'})
  if url_tag.get('href'):
    url= 'https://www.programmableweb.com/category/tools/apis' + url_tag.get('href')
  else:
    break
