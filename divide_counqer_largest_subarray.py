def find_largest_subarray(s):
	num = len(s)
	if num == 1:
		return [s,s[0],s,s]
	else:
		s1 = s[0:num/2]
		s2 = s[num/2:]
		[subS1,sum1,preS1,sufS1] = find_largest_subarray(s1)
		[subS2,sum2,preS2,sufS2] = find_largest_subarray(s2)
		spanS = sufS1 + preS2
		sum3 = sum(spanS)
		# [spanS,sum3] = find_span_largest_subarray(s1,s2)
		if sum1 > sum2 and sum1 > sum3:
			return [subS1,sum1]
		elif sum2 > sum1 and sum2 > sum3:
			return [subS2,sum2]
		else:
			return [spanS,sum3]
def find_span_largest_subarray(s1,s2):
	num1 = len(s1)
	num2 = len(s2)
	sumS1 = 0
	index1 = num1-1
	temSum1 = 0
	sumS2 = 0
	index2 = 0
	temSum2 = 0
	for i in range(num1-1,-1,-1):
		temSum1 = temSum1 + s1[i]
		if temSum1 > sumS1:
			index1 = i
			sumS1 = temSum1
	for j in range(num2):
		temSum2 = temSum2 + s2[j]
		if temSum2 > sumS2:
			index2 = j
			sumS2 = temSum2
	subArray = s1[index1:]+s2[0:index2+1]
	return [subArray,sum(subArray)]

if __name__ == '__main__':
	s = [6,4,-4,29,-45,51,43,11,-12,6,87,-9,-7,-6,3,5,1,2,6,-9,45,32,-34,5,90,32,-80,34]
	result = find_largest_subarray(s)
	print result
	








