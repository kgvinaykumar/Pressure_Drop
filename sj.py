import math
def swameejain(flowrate, flowlength, id, rho, mu, eps):
    #Calculate fluid flow velocity.
    velocity = (4*flowrate)/((22/7)*(id**2))
    #Calculate the Reynold's number.
    reynold = (velocity*rho*id)/mu
    #Calculate the flow drop between inlet and outlet of pipe.
    if reynold < 2300:
        message = "The flow is laminar."

    #Simplified Darcy-Weisbach equation for laminar flow.
        pressuredrop = (128*mu*flowrate*flowlength)/(math.pi*(id**4))
    elif 2300<reynold<3500:
        pressuredrop=0.00
        message = "The flow is not fully developed. Please try modifying parameters."
    else:
        message = "The flow is turbulent."
    #Swamee-Jain simplification for full-flowing circular cross-section.
        smpl = ((eps/id)/3.7)+(5.74/(reynold**0.9))
        f = 0.25/((math.log(smpl,10))**2)
        pressuredrop = (f*rho*(velocity**2)*flowlength)/(2*id)

    return (pressuredrop, message)
