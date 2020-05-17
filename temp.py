import requests
k={}
l=[]
#loop iteration to take inputs &record temps
for i in range(5):
    city = input("Enter City Name:")
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=4f0c91c4dc7aeade90cf80a97865db71&units=metric')
    d= r.json()
    k[i]=d
    l.append(k[i]['main']['temp'])
print(l)    
a=max(l)
print(a)
#loop iteration to find city with highest temperature
for i in range(5):
    if a==k[i]['main']['temp']:
        print("The city with high temperature is:",k[i]['name'])