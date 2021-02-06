import scipy.stats as stats

def constructTwoWayFrequencyTable(v1,v2,v3,v4,t1,t2,t3,t4):
    return {t1:{t3:v1,t4:v3},t2:{t3:v2,t4:v4}}
    
def displayTwoWayFrequencyTable(table):
    t1,t2 = table.keys()
    t3,t4 = table[t1].keys()
    v1,v2,v3,v4 = table[t1][t3],table[t2][t3],table[t1][t4],table[t2][t4]
    prnt = [["",t1,t2,"Totals"],
            [t3,v1,v2,v1+v2],
            [t4,v3,v4,v3+v4],
            ["Totals",v1+v3,v2+v4,sum([v1,v2,v3,v4])]]
    for line in prnt:
        for value in line:
            print("{}\t".format(value),end="")
        print("\n")
        
def P(eq,**kwargs):
    relational_operators = [' U ',' I ',' | ',' < ',' > ',' == ',' <= ',' >= ']
    rel_op = "rel_op not defined";
    for operator in relational_operators:
        if operator in eq:
            rel_op = operator
    
    if rel_op == "rel_op not defined" and 'S' not in kwargs:
        raise ValueError("No recognized relational operator in equation: '{}'".format(eq))
        
    if rel_op == "rel_op not defined" and 'S' in kwargs:
        S = kwargs['S']
        print(S.keys())
        if eq in S.keys():
            return sum([S[eq][key] for key in S[eq].keys()])
        else:
            return sum([S[key][eq] for key in S.keys()])
    
    LHS,RHS = eq.split(rel_op)
    LHS = LHS.strip()
    RHS = RHS.strip()
    #print("LHS: '{}'".format(LHS))
    #print("RHS: '{}'".format(RHS))
    #print("RelOp: '{}'".format(rel_op.strip()))
    
    if rel_op in [' < ',' > ',' == ',' <= ',' >= '] and (LHS == 'Z' or LHS == 'T' or LHS == 'T0' or LHS == 'Z0' or LHS == 'T_0' or LHS == 'Z_0') and rel_op.strip() not in ['U','I','|']:
        if RHS not in kwargs:
            raise ValueError("Variable '{}' not provided.".format(RHS))
        #print("This is a table problem, with {}: {}".format(RHS,kwargs[RHS]))
        if LHS == 'Z':
            # returns z-score
            if '<' in rel_op.strip():
                return round(stats.norm.ppf(kwargs[RHS]),3)
            elif '>' in rel_op.strip():
                return round(stats.norm.ppf(1-kwargs[RHS]),3)
        elif LHS == 'T':
            # returns t-score
            if 'n' not in kwargs:
                raise ValueError("Sample size 'n' not provided.")
            df = kwargs['n']-1
            if '<' in rel_op.strip():
                return round(stats.t.ppf(kwargs[RHS],df),3)
            elif '>' in rel_op.strip():
                return round(stats.t.ppf(1-kwargs[RHS],df),3)
        elif LHS == 'T_0' or LHS == 'T0':
            # returns t-value
            if 'n' not in kwargs:
                raise ValueError("Sample size 'n' not provided.")
            df = kwargs['n']-1
            return round(stats.t.cdf(kwargs[RHS],df),6)
        elif LHS == 'Z_0' or LHS == 'Z0':
            # returns z-value
            return round(stats.norm.cdf(kwargs[RHS]),6)
        
    elif rel_op.strip() in ['U','I','|']:
        #print("You're gonna need some equations here.")
        if 'S' not in kwargs:
            raise ValueError("Sample space 'S' not provided.")
        S = kwargs['S']
        total = sum([sum([S[k1][k2] for k2 in S[k1].keys()]) for k1 in S.keys()])
        
        if LHS not in S.keys() and rel_op.strip() != '|':
            raise KeyError("Sample Space setup up improperly. No key '{}' in keys '{}'".format(LHS,S.keys()))
        if RHS not in S[list(S.keys())[0]].keys() and rel_op.strip() != '|':
            raise KeyError("Sample Space setup up improperly. No key '{}' in keys '{}'".format(RHS,S[list(S.keys())[0]].keys()))
        if rel_op.strip() == 'U' and 'disjoint' not in kwargs:
            raise ValueError("Disjointedness ('disjoint=...') not defined.")
        if rel_op.strip() in ['I','|'] and 'independent' not in kwargs:
            raise ValueError("Independence ('independent=...') not defined.")
            
        if rel_op.strip() == 'U':
            if kwargs['disjoint']:
                return (sum([S[LHS][key] for key in S[LHS].keys()]) + sum([S[key][RHS] for key in S.keys()]))/total
            else:
                return (sum([S[LHS][key] for key in S[LHS].keys()]) + sum([S[key][RHS] for key in S.keys()]) - S[LHS][RHS])/total
            
        if rel_op.strip() == 'I':
            if kwargs['independent']:
                return (sum([S[LHS][key] for key in S[LHS].keys()]) * sum([S[key][RHS] for key in S.keys()]))/total
            else:
                return (S[LHS][RHS])/total
                
        if rel_op.strip() == '|':
            return P(LHS+" I "+RHS,independent=kwargs['independent'],S=S)/P(RHS,S=S)
            
    else:
        raise ValueError("Unknown values or syntax.")
