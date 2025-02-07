
lines = [[0,5],[3,9],[1,10]]
# 0 1 2 3 4 5
#   1 2 3 4 5 6 7 8 9 10
#       3 4 5 6 7 8 9
lines = sorted(lines)
print(lines)
i=0
j=0
k=0

if lines[0][0] < lines[1][0] < lines[0][1]:
    i = [lines[0][1],lines[1][0]]
if lines[0][0] < lines[2][0] < lines[0][1]:
    j = [lines[0][1],lines[2][0]]
if lines[1][0] < lines[2][0] < lines[1][1]:
    k = [lines[1][1],lines[2][0]]

# if lines[0][0] < lines[1][0] < lines[0][1]:
#     i = lines[0][1] - lines[1][0]
# if lines[1][0] < lines[2][0] < lines[1][1]:
#     j = lines[1][1] - lines[2][0]
# if lines[2][0] < lines[0][0] < lines[2][1]:
#     k = lines[2][1] - lines[0][0]

print(i,j,k)
print(i+j+k)
