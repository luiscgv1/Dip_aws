import boto3

# Crear cliente para DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Nombre de la tabla que deseas eliminar
table_name = 'tabla-luis-grisales-2'

# Obtener objeto Table
table = dynamodb.Table(table_name)

# Eliminar la tabla
table.delete()

# Confirmación de eliminación
print(f'Tabla {table_name} eliminada correctamente.')

#crear la tabla
#response = dynamodb.create_table(
#    TableName='tabla-luis-grisales-2',
#    KeySchema=[
#        {
#            'AttributeName':'id',
#            'KeyType':'HASH'
#        }
#        ],
#        AttributeDefinitions=[
#            {
#            'AttributeName':'id',
#            'AttributeType':'S'
#            }
#            ],
#            BillingMode='PAY_PER_REQUEST'
#    )
    
  
        
        
        