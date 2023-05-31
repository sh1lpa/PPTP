
def push_zeros(nums):
    count = 0
    for ind, i  in enumerate(nums):  
        if nums[ind-count] == 0:
            zero = nums.pop(ind-count)
            nums.append(zero)
            count +=1

        print(nums)

    return nums


def missing_repeat(nums):
    d = {}
    for i in nums:
        if i not in d.keys():
            d[i] = 1
        else:
            if i < min(nums) and min[nums]== max[nums]:
                return [i,i-1]
            else:
                return [i,i+1]
            


def main():
    nums= [0,0,1]
    missing_repeat(nums)
    # print(push_zeros(nums))

if __name__ == '__main__':
    main()