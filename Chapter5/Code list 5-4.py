import urllib2
file = urllib2.urlopen('https://www.manning.com/books/hello-world/data/message.txt')
message = file.read()
print  message
