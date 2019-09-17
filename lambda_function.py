import json

def lambda_handler(event, context):
    path = event.get('path', {})
    resultPage = None
    result = {
        "statusCode": 200,
        "headers": {
        'Content-Type': 'text/html',
        },
        "body": resultPage
    }
    if path == "/main.js":
        with open('main.js', 'r') as f:
            result["body"] = f.read() 
        result["headers"]["Content-Type"] = "text/javascript;charset=UTF-8"
    else:
        with open('index.html', 'r') as f:
            result["body"] = f.read()   

    return result
