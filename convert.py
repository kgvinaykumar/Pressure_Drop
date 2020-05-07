def convert(id, flrt, fltg, iunits, funits, lunits):
    #Convert ID.
        if iunits == "in":
            id=(id/39.37)
        else:
            id=(id/100)

    #Convert Flow Rate
        if funits== "gpm":
            flrt=(flrt*0.000063)
        else:
            flrt=(flrt*0.0000167)

    #Convert Pipe Length.
        if lunits == "in":
            fltg=(fltg/39.37)
        else:
            fltg=(fltg/100)

        return id, flrt, fltg;
