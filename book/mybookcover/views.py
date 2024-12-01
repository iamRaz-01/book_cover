from django.shortcuts import render

# Create your views here.
def bookCover (request) :
    host = request.get_host()
    port = host.split(':')[1] 
    print(f'The server is running on the port {port}')
    
    # Log the GET request
    print('GET request received...')
    
    # Render the HTML page
    response = render(request, 'mybookcover/bookcover.html') 
    
    # Log the status code
    print(f'Status code {response.status_code}')
    print('HTML response sent successfully.')
    return response