def find_missing(list1,list2):
  count = 0
  if len(list1)< len(list2):
    num = (set(list2) - set(list1))
    count = num.pop()
    return count
  elif len(list1)> len(list2):
    num = (set(list1) - set(list2))
    count = num.pop()
    return count
  else:
    return 0