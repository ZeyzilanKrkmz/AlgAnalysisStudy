def linear_s(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        print(
            f"adım {steps}: arr[{i}]={arr[i]} {'bulundu!' if arr[i] == target else '≠ ' + str(target) + ',devam..'}"
        )
        if arr[i] == target:
            return i, steps
    return -1, steps


def demo():

    arr = [64, 25, 12, 22, 11, 90, 38, 56]
    target = 90
    print("=" * 50)
    print(f"dizi :{arr}")
    print(f"hedef: {target}")
    print("=" * 50)

    index, steps = linear_s(arr, target)

    print("-" * 50)
    if index != -1:
        print(f"'{target}' bulundu-> index: {index}")
    else:
        print(f"x '{target}' dizide yok.")
    print(f"Toplam adım: {steps}")
    print(f"Complexity: O(n)-n={len(arr)}")


if __name__ == "__main__":
    demo()
