def binaryS_iterative(arr, target):
    low, high = 0, len(arr) - 1
    steps = 0

    print(f"\n{'-' * 55}")
    print(f"{'İter':>5}|{'low':>4}|{'high':>4}|{'mid':>4}|{'arr[mid]':>8}|Karar")
    print(f"{'-' * 55}")

    while low <= high:
        steps += 1
        mid = low + (high - low) // 2
        karar = ""

        if arr[mid] == target:
            karar = "bulundu"
            print(f"{steps:>5}|{low:>4}|{high:>4}|{mid:>4}|{arr[mid]:>8}|{karar}")
            return mid, steps
        elif arr[mid] < target:
            karar = f"-> low ={mid + 1} (sağa geç)"
            low = mid + 1

        else:
            karar = f"->high={mid - 1}(sola geç)"
            high = mid - 1

        print(
            f"{steps:>5}|{low if arr[mid] < target else low:>4}|{high:>4}|{mid:>4}|{arr[mid]:>8}|{karar}"
        )
    return -1, steps


def binaryS_recursive(arr, target, low=0, high=None, steps=0):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1, steps

    steps += 1
    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid, steps
    elif arr[mid] < target:
        return binaryS_recursive(arr, target, mid + 1, high, steps)
    else:
        return binaryS_recursive(arr, target, low, mid - 1, steps)


def demo():
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 56

    print("=" * 55)
    print(f"dizi: {arr}")
    print(f"hedef: {target}")
    print("=" * 55)

    print("\n Iterative binaty search:")
    idx, steps = binaryS_iterative(arr, target)
    print(f"\n Sonuç: index={idx},değer={arr[idx] if idx != -1 else 'yok'}")
    print(f"adım: {steps}|log₂({len(arr)}) ≈ {len(arr).bit_length() - 1}")

    print("\n🔄 RECURSIVE Binary Search:")
    idx2, steps2 = binaryS_recursive(arr, target)
    print(f"  Sonuç : index={idx2}, adım={steps2}")

    print("\n📊 Complexity:")
    print(f"  Best  : O(1)      — mid direkt hedef")
    print(f"  Avg   : O(log n)  — her adım alanı yarılar")
    print(f"  Worst : O(log n)  — n={len(arr)} → max {len(arr).bit_length()} adım")


if __name__ == "__main__":
    demo()
