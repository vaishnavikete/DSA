# Input the list of customer account IDs
account_ids = list(map(int, input("Enter customer account IDs: ").split()))

# Input the account ID to search
key = int(input("Enter account ID to search: "))

# -------- Linear Search --------
found = False
for i in range(len(account_ids)):
    if account_ids[i] == key:
        print("Linear Search: Account ID found at index", i)
        found = True
        break

if not found:
    print("Linear Search: Account ID not found")

# -------- Binary Search --------
# Binary Search requires the list to be sorted
account_ids.sort()

low = 0
high = len(account_ids) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if account_ids[mid] == key:
        print("Binary Search: Account ID found")
        found = True
        break
    elif account_ids[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Binary Search: Account ID not found")