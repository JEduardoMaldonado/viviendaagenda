import web
# @
from web import form
db = web.database(dbn='mysql', host='y0nkiij6humroewt.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',db='b1i85x9we2kb7h3f', user='vh57xlv2tj1r8ovf', pw='clsbdiom4efdeqwe')
render=web.template.render('templates')
urls = (
    '/','index',
    '/nuevo', 'nuevo',
    '/editar/(.+)','editar',
    '/ver/(.+)','ver',
    '/eliminar/(.+)','eliminar'
)



myformBorrego=form.Form(
    form.Textbox('id_borrego'), 
    form.Textbox('id_raza'),
    form.Textbox('id_genetica'),
    form.Textbox('genero'),
    form.Textbox('edad'),
    form.Textbox('fecha_nacimiento'),
    form.Textbox('precio')
    
   
)

class index:
    def GET(self):
        
        result=db.select('Borrego')
        return render.index(result)
    def POST(self):           
        raise web.seeother("/nuevo")    
class nuevo:
    def GET(self):
        formNew=myformBorrego()
        return render.nuevo(formNew)
    def POST(self): 
        formNew = myformBorrego()
        if not formNew.validates(): 
            return render.nuevo(formNew)
        else:
            db.insert('Borrego', 
            id_raza=formNew.d.id_raza, 
            id_genetica=formNew.d.id_genetica, 
            genero=formNew.d.genero,
             edad=formNew.d.edad,
             fecha_nacimiento=formNew.d.fecha_nacimiento,
             precio=formNew.d.precio
             )
            result=db.select('Borrego')
            raise web.seeother('/index')
            

class editar:
    def GET(self,id):
        formEdit=myformBorrego()
        
        
        result=db.select('Borrego', where= "id=%s"%(id))
        
        for row in result:
            formEdit['genero'].value=row.genero
            formEdit['edad'].value=row.edad
            formEdit['fecha_nacimiento'].value=row.fecha_nacimiento
            formEdit['precio'].value=row.precio
        return render.editar(formEdit)        
    def POST(self,id):
        formEdit=myformBorrego()
        if not formEdit.validates(): 
            return render.editar(formEdit)
        else:
            db.update('Borrego', where='id=%s'%(id), genero=formEdit.d.genero,
             edad=formEdit.d.edad, fecha_nacimiento=formEdit.d.fecha_nacimiento,
              precio=formEdit.d.precio)
            result=db.select('Borrego')
            raise web.seeother('/index')
class eliminar:
    def GET(self,id):
        formEdit=myformBorrego()
        
        result=db.select('Borrego', where='id=%s'%(id))
        for row in result:
            formEdit['genero'].value=row.genero
            formEdit['edad'].value=row.edad
            formEdit['fecha_nacimiento'].value=row.fecha_nacimiento
            formEdit['precio'].value=row.precio
        
        return render.eliminar(formEdit)        
    def POST(self,id):
        formEdit=myformBorrego()
        if not formEdit.validates(): 
            return render.eliminar(formEdit)
        else:
            db.delete('Borrego', where="id=%s"%(id))
            raise web.seeother('/index')
class ver:
    def GET(self,id):
        
        result=db.select('Borrego', where="id=%s"%(id))
        return render.ver(result)

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()
