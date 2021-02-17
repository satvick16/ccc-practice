def howSum_memo(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum < 0:
        return None
    if targetSum == 0:
        return []

    for num in numbers:
        remainder = targetSum - num
        result = howSum_memo(remainder, numbers, memo)
        if result != None:
            x = result
            x.append(num)
            memo[targetSum] = x
            return x

    memo[targetSum] = None
    return None

##memo = {}
##print(howSum_memo(300, [7, 14], memo))

##########################################################

def canSum(target_sum, numbers):
    table = [False] * (target_sum + 1)
    table[0] = True

    for i in range(target_sum):
        if table[i]:
            numbers = [num for num in numbers if i + num <= target_sum]

            for num in numbers:
                table[i + num] = True

    return table[-1]

# print(canSum(7, [5, 3, 4, 7]))

###########################################################

def howSum(targetSum, numbers):
    dp = [None for i in range(targetSum+1)]
    dp[0] = []

    for i in range(targetSum):
        if dp[i] is not None:
            numbers = [num for num in numbers if i + num <= targetSum]

            for num in numbers:
                dp[i + num] = dp[i] + [num]
                
    return dp[-1]

##print(howSum(7, [5, 3, 4, 7]))
##print(howSum(300, [7, 14]))

##########################################################

def bestSum(targetSum, numbers):
    dp = [None for i in range(targetSum+1)]
    dp[0] = []

    for i in range(targetSum):
        if dp[i] is not None:
            numbers = [num for num in numbers if i + num <= targetSum]

            for num in numbers:
                if dp[i + num] is None:
                    dp[i + num] = dp[i] + [num]
                else:
                    if len(dp[i] + [num]) <= len(dp[i + num]):
                        dp[i + num] = dp[i] + [num]
                    
    return dp[-1]

# print(bestSum(8, [2, 3, 5]))

############################################################

def countConstruct(target, wordBank):
    dp = [0 for i in range(len(target)+1)]
    dp[0] = 1

    for i in range(len(target)+1):
        if dp[i] > 0:
            for word in wordBank:
                if target[i:i+len(word)] == word:
                    dp[i + len(word)] += dp[i]

    return dp[-1]

# print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))

#############################################################

def allConstruct(target, wordBank):
    dp = [[] for i in range(len(target)+1)]
    dp[0].append([])

    for i in range(len(target)):
        if dp[i]:
            for word in wordBank:
                if target[i:i+len(word)] == word:
                    dp[i+len(word)] += dp[i]

    return dp[-1]

print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
