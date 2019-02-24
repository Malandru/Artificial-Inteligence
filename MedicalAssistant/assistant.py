import json
import watson_developer_cloud

assistant = None
response = None

def init():
    global assistant
    assistant = watson_developer_cloud.AssistantV1(
        username='2cf63380-0ac9-42f6-9cf7-786de0069ba9',
        password='3R5nIhQa15YS',
        version='2018-09-20'
    )

def sendMessage(message, cont, out):
    global response
    response = assistant.message(
        workspace_id='55ab8457-6ac4-4bef-8202-663fbd7d13c4',
        input={
            'text': message
        },
        context=cont,
        output=out,
        nodes_visited_details=True
    ).get_result()

#~~~~~~~~~~EXECUTABLE CODE~~~~~~~~~~
init()
output = None
context = None
while True:
    input = raw_input('Mensaje: ')
    sendMessage(input, context, output)
    myJson = json.dumps(response, indent=2)
    #print myJson
    context = response['context']
    output = response['output']
    #print output
    print 'Respuesta:', output['generic'][-1]['text']

#print obj["text"]