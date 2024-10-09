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
        text = ['a','b','c'] #remove this
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
            return render(request, 'error.html', {"message" : "Maybe you exceeded 1000 Word limit", "status_code": {response.status_code}, "status_response": {response.text}})
    else:
        return render(request, 'home.html')
