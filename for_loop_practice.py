websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://www.tictok.com"
)

for website in websites:
  if not website.startswith("https://"):
    website = f"https://" + website
  print(website)