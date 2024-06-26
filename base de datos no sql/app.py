import boto3

#crear cliente para dynamodb
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

tabla = dynamodb.Table('tabla-luis-grisales')

#leer un elemento de la tabla
#response = tabla.get_item(Key={'id':'2'})
#print(response['Item'])

#leer todos los elementos de la tabla
#response = tabla.scan()
#print(response['Items'])

#insertar elementos en una tabla
#item = {
#   'id': '3',
#    'nombre': 'Camila',
#    'Ciudad': 'Caldas'
#}

#tabla.put_item(Item=item)

#response = tabla.scan()
#print(response['Items'])

#actualizar elemento de una tabla
 #elemento antes de actualizar
response = tabla.update_item(
    Key={
        'id': '3'  
    },
    UpdateExpression='SET Ciudad = :val1',  # Expresión de actualización
    ExpressionAttributeValues={
        ':val1': 'Cali'  # Nuevo valor para atributo2
    }
)

response = tabla.scan()
print(response['Items'])