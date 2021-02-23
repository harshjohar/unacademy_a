n = int(input())
teams = list(map(int, input().split()))
profitable_matches = [0]
# recursion may help here
# hint: merge sort
# if(len(set(Alist)) == len(Alist)): -> to check if the list contains all the unique element:

def team_fixtures(li, left, right, result):
    if len(li)<=1:
        return
    mid = (left+right)//2
    l_h = li[left:mid+1]
    r_h = li[mid+1:right+1]

    if len(set(l_h)&set(r_h)) == 0:
        result[0]+=1
    team_fixtures(l_h, left, mid, result)
    team_fixtures(r_h, mid+1, right, result)

team_fixtures(teams, 0, len(teams)-1, profitable_matches)
print(profitable_matches[0])

