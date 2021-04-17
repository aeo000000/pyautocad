'''https://github.com/Rahulghuge94/Cad-Py/blob/main/utility.py'''
from pyautocad.types import Apoint


def getpoint(acad,point,inputstring="Click on Drawing to get point"):
    """
      acad= acad object
      Inputstring=prompt optional
    """
    return acad.doc.Utility.GetPoint(point,inputstring)
  
  #-----------------------------------------------------------------------
  
  
  
