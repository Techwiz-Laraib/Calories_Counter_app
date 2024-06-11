from django.shortcuts import render
import json
import requests

def home(request):
    if request.method == 'POST':  
        query = request.POST.get('query', '')  
        
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        api_request = requests.get(api_url, headers={'X-Api-Key': 'QoAqHTIJCuUP51CpC3YhzA==Md8nDu4ab82VH6fV'})
   
        try:
            api = json.loads(api_request.content)  
            print(api_request.content) 
        except Exception as e:
            api = "Oops! There was an error" 
            print(e)
            return render(request, 'home.html', {'api': api})
        else:
            return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html')

