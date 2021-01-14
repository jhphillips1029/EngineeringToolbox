from IPython.display import Latex

def newpage():
    display(Latex(r"\newpage"))
    
def answer(printMe):
    display(Latex(r"\fbox{"+printMe.replace('\n',r'\newline')+"}"))