#link : https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen
#time : O(N)
def activityNotifications(n,expenditure, d):
    # Write your code here
    y =  expenditure[:d]
    m = 0
    z = expenditure[d:]
    for i in z :
        x =sorted(y)        
        if len(x)%2 !=0 :
            s =  x[int(len(x)/2)]
            if i>= 2*s:
               m+= 1
               y[0] = i
        else :
            s =  (x[int(len(x)/2)] +x[int(len(x)/2)-1])/2
            if i>= 2*s:
               m+= 1
               y[0] = i
    return m 
        

print(activityNotifications(5,[10,20,30,40,50],3))
