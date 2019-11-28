from clarifai.rest import ClarifaiApp

def getobjects(imageurl):
  app = ClarifaiApp()
  op=[]
  model = app.models.get('foodcustom')
  response = model.predict_by_filename(imageurl)
  concepts = response['outputs'][0]['data']['concepts']
  for concept in concepts:  
    #print(concept['name'])
    op.append(str(concept['name']))
    
  #op = list(map(str,op))
  return op
