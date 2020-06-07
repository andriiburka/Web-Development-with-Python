
# NOT FINISHED YET
li = [int(i) for i in input().split()]

di = {}
negatives = {'negatives': i for i in li if i < 0}
positives = {'positives': i for i in li if i >= 0}
di.update(negatives)
di.update(positives)


print(di)
print(negatives)