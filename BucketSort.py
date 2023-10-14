def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val

    # Create buckets
    num_buckets = len(arr)
    bucket_range = range_val / (num_buckets - 1) if range_val > 0 else 1
    buckets = [[] for _ in range(num_buckets)]

    # Place elements in buckets
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    # Sort each bucket (using another sorting algorithm or recursion)
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])

    # Concatenate sorted buckets to get the final sorted array
    sorted_array = [num for bucket in buckets for num in bucket]

    return sorted_array

# Example usage:
arr = [3.2, 6.1, 1.3, 2.5, 7.4, 2.0]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
