#Import input from HTML and convert to SI units.
import convert
import sj
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

    id, flrt, fltg = convert.convert(id, flrt, fltg, iunits, funits, lunits)

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
    final, message = sj.swameejain(flrt, fltg, id, rho, mu, eps)
#Conversion back to display values.
    if iunits == "in":
        final = final/6894.76
        return render_template("result.html",message=message, result=final, punits="psi")
    else:
        final = final/1000
        return render_template("result.html",message=message, result=final, punits="kpa")
