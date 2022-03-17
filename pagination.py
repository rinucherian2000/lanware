def paginator(array, page_number):
    n, remainder = page_number, len(array) % page_number
    curr, idx, old_idx = 1, 0, 0
    while n + remainder != 0:
        idx += len(array) // page_number + bool(remainder)
        print(f"this is page {curr} have object {array[old_idx:idx]}")
        n -= 1
        remainder = max(remainder - 1, 0)
        curr += 1
        old_idx = idx


lst = list(range(1, 10))
page_number = 4

paginator(lst, page_number)