from requests import get
from bs4 import BeautifulSoup

base_url = 'http://weworkremotely.com/remote-jobs/search?term='
search_term = 'python'

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  # print(soup.findAll("section", class_="jobs"))
  jobs = soup.find_all("section", class_="jobs")
  print(len(jobs))
  for job_section in jobs:
    job_posts = job_section.find_all('li')
    for post in job_posts:
      print(post)
      print("///////////////////////")
        