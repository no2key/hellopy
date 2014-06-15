from sys import argv
from weather import Weather


w = Weather('873a531cec3212a4906a683572b248b5')
res = w.get_weather(argv[1])

print(res)

