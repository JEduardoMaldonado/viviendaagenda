import web
# @
from web import form
db = web.database(dbn='mysql', host='ehc1u4pmphj917qf.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',db='aw10o7i0uoowomzw', user='bt9w0v9g0v8uz4x3', pw='ct31cqvwybrmkqku')
render=web.template.render('templates')
urls = (
   '/','index',
    '/nuevo', 'nuevo',
    '/editar/(.+)','editar',
    '/ver/(.+)','ver',
    '/eliminar/(.+)','eliminar'
)



myformAgenda=form.Form(
    form.Textbox('Nombre'), 
    form.Textbox('Apellido'),
    form.Textbox('Telefono'),
    form.Textbox('Correo')
   
)
class index:
    def GET(self):
        
        result=db.select('datosagenda')
        return render.index(result)
    def POST(self):           
        raise web.seeother("/nuevo")    
class nuevo:
    def GET(self):
        formNew=myformAgenda()
        return render.nuevo(formNew)
    def POST(self): 
        formNew = myformAgenda()
        if not formNew.validates(): 
            return render.nuevo(formNew)
        else:
            db.insert('datosagenda', 
            nombre=formNew.d.Nombre, 
            apellido=formNew.d.Apellido, 
            telefono=formNew.d.Telefono,
             correo=formNew.d.Correo)
            result=db.select('datosagenda')
            raise web.seeother('/')
            

class editar:
    def GET(self,id):
        formEdit=myformAgenda()
        
        
        result=db.select('datosagenda', where= "id=%s"%(id))
        
        for row in result:
            formEdit['Nombre'].value=row.nombre
            formEdit['Apellido'].value=row.apellido
            formEdit['Telefono'].value=row.telefono
            formEdit['Correo'].value=row.correo
        return render.editar(formEdit)        
    def POST(self,id):
        formEdit=myformAgenda()
        if not formEdit.validates(): 
            return render.editar(formEdit)
        else:
            db.update('datosagenda', where='id=%s'%(id), nombre=formEdit.d.Nombre,
             apellido=formEdit.d.Apellido, telefono=formEdit.d.Telefono,
              correo=formEdit.d.Correo)
            result=db.select('datosagenda')
            raise web.seeother('/')
class eliminar:
    def GET(self,id):
        formEdit=myformAgenda()
        
        result=db.select('datosagenda', where='id=%s'%(id))
        for row in result:
            formEdit['Nombre'].value=row.nombre
            formEdit['Apellido'].value=row.apellido
            formEdit['Telefono'].value=row.telefono
            formEdit['Correo'].value=row.correo
        
        return render.eliminar(formEdit)        
    def POST(self,id):
        formEdit=myformAgenda()
        if not formEdit.validates(): 
            return render.eliminar(formEdit)
        else:
            db.delete('datosagenda', where="id=%s"%(id))
            raise web.seeother('/')
class ver:
    def GET(self,id):
        
        result=db.select('datosagenda', where="id=%s"%(id))
        return render.ver(result)

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()
