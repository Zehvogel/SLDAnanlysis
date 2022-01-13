import ROOT

def makeFilter(name, inputs, condition):
    sinputs = ", ".join((f"ROOT::RVec<int> {i}" for i in inputs))
    fun = f"""
    ROOT::RVec<int> {name}({sinputs}) {{
        ROOT::RVec<int> res{{}};
        for (size_t i = 0; i < {inputs[0]}.size(); i++) {{
            int r = 0;
            if ({condition}) {{
                r = 1;
            }}
            res.push_back(r);
        }}
        return res;
    }}
    """
    #print(fun)
    ROOT.gInterpreter.ProcessLine(fun)