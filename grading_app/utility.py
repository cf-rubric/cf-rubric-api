"""[script]
"""



class Criteria:
    
    def __init__(self, question:str, desc:str, possible:int):
        self.question = question
        self.desc = desc
        self.possible = possible
        

    def __str__(self):
        return self.desc


    

def report_gen():
    _report = list()

    _report.append(Criteria('identified', 'identified inputs and outputs', 2))
    _report.append(Criteria('visual', 'visually illustrated the problem domain', 2))
    _report.append(Criteria('ident_optimal', 'identified optimal data structure or algorithm', 4))
    _report.append(Criteria('presented', 'presented and understood a working algorithm', 4))
    _report.append(Criteria('syntax', 'final code was syntactically correct', 2))
    _report.append(Criteria('idioms', 'final code was idiomatically correct', 2))
    _report.append(Criteria('best_solve', 'solution was the best possible option', 2))
    _report.append(Criteria('asked', 'asked meaningful clarifying questions', 2))
    _report.append(Criteria('step_through', 'stepped through their solution', 2))
    _report.append(Criteria('big_O', 'big-O time and space are analyzed', 2))
    _report.append(Criteria('testing', 'explained an approach to testing', 2))
    _report.append(Criteria('verbal', 'verbalized their thought process', 6))
    _report.append(Criteria('terms', 'used correct terminology', 2))
    _report.append(Criteria('time', 'used the time available effectively',1))
    _report.append(Criteria('over', 'was not over-confident (not listening to suggestions)', 1))
    _report.append(Criteria('under', 'was not under-confident (unsure of known algorithm)', 1))
    _report.append(Criteria('readable', 'whiteboard was readable (penmanship and spacing)', 1))
    
    
    return print([crit.question for crit in _report])




