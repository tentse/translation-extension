from django.shortcuts import render
import requests,json

# Create your views here.
def home(request):
    if request.method == 'POST':
        text = request.POST['inputtext']
        url = "https://api.monlam.ai/api/v1/translation"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer asdfaheigkdin_sdfasd_feffes'
        }

        data = {
            "input": text,
            "target": "bo"
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print(response.status_code)
            translated = response.json()
            translated = translated['translation']
            print(translated)
            return render(request, 'home.html', {"translate": translated, "text": text})
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return render(request, 'error.html', {"message" : "1000 Word limit exceeded"})
    else:
        return render(request, 'home.html')

def error(request):
    return render(request, 'error.html')