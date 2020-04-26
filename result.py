#Import input from HTML and convert to SI units.
from flask import Flask, render_template, request
import math
eps=0.0127

app = Flask(__name__)

@app.route("/")
def inputform():
    return render_template("inputform.html")

#Import data.
@app.route("/result", method=["POST"])
def result():
    id=request.form.get("id")
    prs=request.form.get("prs")
    flrt=request.form.get("flrt")
    fltg=request.form.get("fltg")
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

    #Convert Pressure
    if punits == "psi":
        prs=(prs*6894.76)
    else:
        prs=prs

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
    re = (vel*fltg)/nu
#Calculate the flow drop between inlet and outlet of pipe. 
    if re < 2300:
        final = (128*mu*flrt*fltg)/((22/7)*(id**4))
    elif 2300<re<3500:
        final = "The flow is not fully developed. Please try modifying parameters."
    else:
        smpl = ((eps/id)/3.7)+(5.74/(re**0.9))
        final = (0.25*rho*vel*vel)/(2*id*((math.log(smpl,10))**2))
    return final