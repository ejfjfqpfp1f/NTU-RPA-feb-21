from flask import Flask,request,render_template

app=Flask(_name_)

@app.route("/",methods=["GET","POST"])
def index():
 return(render_template("index,html"))

@app.route("/main",methods=["GET","POST"])
 def main():
name=request,form,get("name")
return(rander_templates("main,html",r=name))

if_name_=="_main_";
 app.run()
