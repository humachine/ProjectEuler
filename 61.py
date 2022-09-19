grid = {i:[] for i in range(1000,10000)}
gonalsets = {i:[] for i in range(3,9)}
prefsets = {i:[] for i in range(3,9)}
suffsets = {i:[] for i in range(3,9)}

for j in range(1, 7):
  for n in range(142):
    mul = (j*n + 2 - j)
    prod = mul*n/2
    if prod > 10000:
      break
    if prod < 1000:
      continue
    if prod in grid: 
      grid[prod].append(j+2)
      gonalsets[j+2].append(str(prod))

def noprefixes(num, gonalsets, ind):
  for i in range(3, 9):
    if i == ind:
      continue
    for j in range(len(gonalsets[i])):
      if num[2:] == gonalsets[i][j][:2]:
        return False
  return True

def nosuffixes(num, gonalsets, ind):
  for i in range(3, 9):
    if i == ind:
      continue
    for j in range(len(gonalsets[i])):
      if num[:2] == gonalsets[i][j][2:]:
        return False
  return True


# Trim and remove all orphan/dead end nodes (i.e nodes which do not have both a forward and backward path)
# Then pick the polygon with least 4-digit numbers. For each of those check if they have a viable suffix and prefix
# This gives us 14 options (variable: traversal)
# Then for each of those 14 options, let's search out one more level and see how many we get). We already are down to 9 (prefix2/suffix2). 
# Brute force manually for those 9


trimsets = {i:[] for i in range(3,9)}
for i in range(3,9):
  for j in range(len(gonalsets[i])):
    num = gonalsets[i][j]
    if noprefixes(num, gonalsets, i) or nosuffixes(num, gonalsets, i):
      continue
    trimsets[i].append(num)


gonalsets = trimsets
 
suffixnums = {}
prefixnums = {}
traversals = {i:[] for i in gonalsets[8]}
for nums in gonalsets[8]:
  suffix = nums[2:]
  for j in range(3,8):
    for keys in gonalsets[j]:
      if keys[:2] == suffix:
        suffixnums[nums] = (j, keys)
  prefix = nums[:2]
  for j in range(3,8):
    for keys in gonalsets[j]:
      if keys[2:] == prefix:
        prefixnums[nums] = (j, keys)

for key in set(prefixnums.keys()).intersection(suffixnums.keys()):
  if prefixnums[key][0] == suffixnums[key][0]:
    continue
  traversals[key].append(prefixnums[key])
  traversals[key].append(suffixnums[key])
traversals = {k: v for k, v in traversals.items() if v != []}
print len(traversals)
for i in traversals:
  print i, traversals[i]

 

suffixlist = [v[0] for k,v in traversals.items()]
prefix2 = {}
for item in suffixlist:
  num = item[1]
  col = item[0]
  prefix = str(num[:2])
  for j in range(3,8):
    if j == col:
      continue
    for keys in gonalsets[j]:
      if keys[2:] == prefix:
        prefix2[num] = (j, keys)

prefixlist = [v[1] for k,v in traversals.items()]
suffix2 = {}
for item in prefixlist:
  num = item[1]
  col = item[0]
  suffix = str(num[2:])
  for j in range(3,8):
    if j == col:
      continue
    for keys in gonalsets[j]:
      if keys[:2] == suffix:
        suffix2[num] = (j, keys)

print len(prefix2)
print len(suffix2)
