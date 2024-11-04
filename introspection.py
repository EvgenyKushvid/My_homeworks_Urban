import inspect
from pprint import pprint


def introspection_info(obj):
   result ={}
   res_atr = []
   res_metod =[]



   atr = [getattr(type(obj), f) for f in dir(obj)]
   metods = [a for a in atr if 'method' in str(a)]
   atributes = [a for a in atr if 'attribute' in str(a)]

   for elem in atributes:
      elem = str(elem).split()
      res_atr.append(elem[1].replace("'",''))
   # for elem in metods:
   #    elem = str(elem).split()
   #    res_metod.append(elem[1].replace("'",''))
   for elem in dir(obj):
      res_metod.append(elem)

   result['type'] = type(obj)
   result['metods'] = res_metod
   result['atributes'] = res_atr
   result['modules'] = inspect.getmodule(obj)

   return result


number_info = introspection_info(42)
print(number_info)

