"""Fixed-size sliding window template (window size = k)."""


def sliding_window_fixed(arr, k):
    i = j = 0
    window_sum = 0
    best = float("-inf")

    while j < len(arr):
        window_sum += arr[j]                 # add the new element

        if j - i + 1 < k:                    # window size not achieved
            j += 1
        elif j - i + 1 == k:                 # window size achieved
            best = max(best, window_sum)     # compute the answer
            window_sum -= arr[i]             # remove the element leaving the window
            i += 1
            j += 1
    return best


if __name__ == "__main__":
    print(sliding_window_fixed([2, 8, 7, 12, 15], 3))  # 34
