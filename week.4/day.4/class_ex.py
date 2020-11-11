def sum(given_list):
	total = 0
	for num in given_list:
		total += num
	return total

def min(nums):
	total = nums[0]
	for num in nums:
		if num < total:
			total = num
	return total

def max(nums):
	total = nums[0]
	for num in nums:
		if num > total:
			total = num
	return total

