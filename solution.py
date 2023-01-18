def solution(args):
    if not args:
        return ""
    res = []
    start = args[0]
    end = args[0]
    for i in range(1, len(args)):
        if args[i] - args[i - 1] == 1:
            end = args[i]
        else:
            if start == end:
                res.append(str(start))
            elif end - start == 1:
                res.append(str(start) + "," + str(end))
            else:
                res.append(str(start) + "-" + str(end))
            start = args[i]
            end = args[i]
    if start == end:
        res.append(str(start))
    elif end - start == 1:
        res.append(str(start) + "," + str(end))
    else:
        res.append(str(start) + "-" + str(end))
    return ",".join(res)
  
  
  test.describe("Sample Test Cases")

test.it("Simple Tests")
test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')
