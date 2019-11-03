import json

COUNTER = 0

def handler(event, context):
    global COUNTER
    COUNTER = COUNTER + 1
    return {
        'statusCode':200,
        'body': json.dumps({
            "Message":"Hello, World!",
            "InMemoryCounter":COUNTER
        }),
        'isBase64Encoded': False
    }
