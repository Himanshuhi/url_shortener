import pyshorteners

shortener = pyshorteners.Shortener()

short_url = shortener.tinyurl.short('https://google.com')
#you can use below code to
#short_url = shortener.bitly.short('https://www.example.com')

#himanshu
print(short_url)



