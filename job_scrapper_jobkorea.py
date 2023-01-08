from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

base_url = "https://www.jobkorea.co.kr/Search/?stext="
search_term = "python"
location_term = "&local=I000" # 서울 == "I000"
career_type = "&careerType=1" # 신입 == "1"

response = get(f"{base_url}{search_term}{location_term}{career_type}")

if response.status_code != 200:
  print("Can't request page")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  job_list = soup.find("ul", class_="clear")
  print(job_list)
  jobs = job_list.find_all('li')
  print("jobs: ", jobs)