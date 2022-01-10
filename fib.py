memo = {}
def fib(x):
    result_from_memo = memo.get(x)
    if result_from_memo is not None:
        return result_from_memo
    if x == 0 or x == 1:
        return 1
    else:
        result = fib(x-1) + fib(x-2)
        memo[x] = result
        return result
