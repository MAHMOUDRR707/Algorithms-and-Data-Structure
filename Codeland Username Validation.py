#time : o(1) 



import re
def CodelandUsernameValidation(strParam):

  # code goes here'
  if 4>len(strParam) or len(strParam)>25:
    return  False
  elif strParam[len(strParam)-1] == '_':
    return False
  elif not isinstance(strParam[0],str) : 
    return False
  elif  not re.findall("[0123]", strParam):
    return  False
  else :
    return True

# keep this function call here 
print (CodelandUsernameValidation(raw_input()))
