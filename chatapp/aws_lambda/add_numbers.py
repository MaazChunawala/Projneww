def lambda_handler(event, context):
    num1 = event['num1']
    num2 = event['num2']
    return {
        'statusCode': 200,
        'body': num1 + num2
    }