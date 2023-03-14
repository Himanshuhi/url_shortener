import pyshorteners

# Create an instance of the Shortener class
shortener = pyshorteners.Shortener()

# Shorten a URL using the TinyURL service
short_url = shortener.tinyurl.short('https://google.com')

# Shorten a URL using the Bit.ly service
#short_url = shortener.bitly.short('https://www.example.com')


# Print the shortened URL
print(short_url)


#pip install pyshorteners
