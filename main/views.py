from django.shortcuts import render, HttpResponse
from .get_salts import get_medicines_group, get_medicine_name

def home(request):
    return render(request, 'main/index.html')

def get_medicines(request):
    if request.method == "POST":
        medicine_name = request.POST.get('user_input')
        mini_df = get_medicine_name(medicine_name)
        mini_df_2 = get_medicines_group(medicine_name)
        if len(mini_df) > 0 and len(mini_df_2) == 0:
            return render(request, 'main/result.html', {'medicine_table':mini_df.to_html(classes='table-dark table-striped custom-table', index=False)})
        elif len(mini_df) == 0 and len(mini_df_2) > 0:
            return render(request, 'main/result.html', {'medicine_table':mini_df_2.to_html(classes='table-dark table-striped custom-table', index=False)})
        else:
            return render(request, 'main/result.html', {'error':True})
        
    return render(request, 'main/result.html')

