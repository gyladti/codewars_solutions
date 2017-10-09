# You are given an array strarr of strings and an integer k.
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.

def longest_consec(strarr, k):
    ans = ''
    k -= 1
    l = 0
    i = 0
    while i < len(strarr) - k:
        temp_arr = list()
        j = 0
        while j <= k:
            temp_arr.append(strarr[i + j])
            j += 1

        temp = ''.join(temp_arr)
        if len(temp) > l:
            l = len(temp)
            ans = temp
        i += 1
    return ''.join(ans)

print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
