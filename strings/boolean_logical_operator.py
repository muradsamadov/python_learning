#Booleans - logical operations
print((1 == 1) and (2 == 2)) #result is True; AND means that both operands should be True in order to get the expression evaluated as True
 
print((1 == 1) or (2 == 2)) #result is True; when using OR, it is enough if only one expression is True, in order to have True as the final result
 
print(not(1 == 1)) #result is False; using the NOT operator means denying an expression, in this case denying a True expression
 
print(not(1 == 2)) #result is True; using the NOT operator means denying an expression, in this case denying a False expression
 
None, 0, 0.0, 0L, 0j, empty string, empty list, empty tuple, empty dictionary #these values always evaluate to False
 
print(bool(None)) #returns False; function that evaluates values and expressions
 
print(bool(0)) #returns False; function that evaluates values and expressions
 
print(bool(2)) #returns True; function that evaluates values and expressions
 
print(bool("router")) #returns True; function that evaluates values and expressions