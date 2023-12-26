def main(num, nums): #main algorithm

    if nums[0] > nums[1] or nums[-1] > nums[-2]: #quick checks and requirements
        return -1
    elif min(nums) == max(nums):
        return 0

    counter = 0

    #this was my fix to an out of range error I previously received
    if nums[-1] < nums[-2] and num >= 3:
        diff = abs(nums[-1] - nums[-2])
        nums[-3] -= diff
        nums[-2] -= diff
        counter += diff*2

    #main loop
    for j in range(num-1): #end goal is to end up with all of the same numbers
        if nums[j] != nums[j+1]: #if two consecutive numbers are equivalent, then they can both remain unchanged.
            diff = abs(nums[j + 1] - nums[j])
            if nums[j] > nums[j+1]: #check which side is higher, because we have to subtract from the higher side
                nums[j] -= diff
                nums[j-1] -= diff
                counter += 2*diff
            elif nums[j] < nums[j+1]:
                if j == num-2: #problematic code
                    return -1
                else:
                    nums[j+1] -= diff
                    nums[j+2] -= diff
                    counter += 2*diff

    if min(nums) < 0:
        return -1

    return counter


reps = int(input())

for _ in range(reps):

    input_num = int(input())
    input_nums = list(map(int, input().split()))

    if input_num == 1:
        print(0)
    else:
        print(main(input_num, input_nums))