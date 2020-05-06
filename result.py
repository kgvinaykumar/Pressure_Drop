#Import input from HTML and convert to SI units.
import math
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inputform():
    return render_template("inputform.html")
#Absolute roughness value averaged for most common materials.
eps=0.0157*(10**-3)
#Import data.
@app.route("/result", methods=["POST"])
def result():

    id=float(request.form.get("id"))
    flrt=float(request.form.get("flrt"))
    fltg=float(request.form.get("fltg"))
    iunits=request.form.get("iunits")
    punits=request.form.get("punits")
    funits=request.form.get("funits")
    lunits=request.form.get("lunits")
    ltypes=request.form.get("ltypes")
#Convert ID.
    if iunits == "in":
        id=(id/39.37)
    else:
        id=(id/100)

#Convert Flow Rate
    if funits=="gpm":
        flrt=(flrt*0.000063)
    else:
        flrt=(flrt*0.0000167)

#Convert Pipe Length.
    if lunits == "in":
        fltg=(fltg/39.37)
    else:
        fltg=(fltg/100)
#Select Liquid.
    if ltypes=="water":
        rho= 1000
        nu= 1.787e-6
        mu= 1.793e-3
    elif ltypes=="beer":
        rho=1010
        nu=1.8e-6
        mu=1.799e-3
    elif ltypes=="milk":
        rho= 1.030
        nu= 1.13e-6
        mu=0.003
#Calculate fluid flow velocity.
    vel = (4*flrt)/((22/7)*(id*id))
#Calculate the Reynold's number.
    re = (vel*rho*id)/mu
#Calculate the flow drop between inlet and outlet of pipe.
    if re < 2300:
        message = "The flow is laminar."
#Simplified Darcy-Weisbach equation for laminar flow.
        final = (128*mu*flrt*fltg)/(math.pi*(id**4))
    elif 2300<re<3500:
        final = "The flow is not fully developed. Please try modifying parameters."
    else:
        message = "The flow is turbulent."
#Swamee-Jain simplification for full-flowing circular cross-section.
        smpl = ((eps/id)/3.7)+(5.74/(re**0.9))
        f = 0.25/((math.log(smpl,10))**2)
        final = (f*rho*(vel**2)*fltg)/(2*id)
#Conversion back to display values.
    if iunits == "in":
        final = final/6894.76
        return render_template("result.html",message=message, result=final, punits="psi")
    else:
        final = final/1000
        return render_template("result.html",message=message, result=final, punits="kpa")
