import requests



r = requests.get('https://w3schools.com')
print(str(r.status_code));

print("Raw HTML:\n")
print(r.text)
print("Status Code:",str(r.status_code));
# print(r.content)