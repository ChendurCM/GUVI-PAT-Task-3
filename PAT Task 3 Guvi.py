# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through the list and separate even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Print the lists of even and odd numbers
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


def is_prime(num):
    # Function to check if a number is prime
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize a list to store prime numbers
prime_numbers = []

# Initialize a counter for the number of prime numbers
prime_count = 0

# Iterate through the list to find prime numbers and count them
for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)
        prime_count += 1

# Print the list of prime numbers and the count
print("Prime numbers:", prime_numbers)
print("Number of prime numbers:", prime_count)



def is_happy(num):
    # Function to check if a number is a happy number
    seen_numbers = set()  # Set to track numbers we've already seen in the process
    while num != 1 and num not in seen_numbers:
        seen_numbers.add(num)
        # Calculate the sum of the squares of the digits
        num = sum(int(digit) ** 2 for digit in str(num))
    # Return True if the number reaches 1, indicating it is a happy number
    return num == 1

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize a counter for the number of happy numbers
happy_count = 0

# Iterate through the list and count happy numbers
for num in numbers:
    if is_happy(num):
        happy_count += 1

# Print the number of happy numbers in the list
print("Number of happy numbers in the list:", happy_count)


def sum_first_last_digit(number):
    # Convert the number to a string to access its digits
    num_str = str(number)
    
    # Get the first digit (the first character in the string)
    first_digit = int(num_str[0])
    
    # Get the last digit (the last character in the string)
    last_digit = int(num_str[-1])
    
    # Calculate the sum of the first and last digit
    return first_digit + last_digit

if __name__ == "__main__":
    # Ask the user to enter an integer
    number = int(input("Enter an integer: "))
    
    # Calculate the sum of the first and last digit
    result = sum_first_last_digit(number)
    
    # Print the result
    print("Sum of the first and last digit of the integer:", result)



def can_distribute_mangoes(mango_bags, students, max_difference):
    # Function to check if it is possible to distribute the mango bags to the students
    # with the given maximum difference
    
    # Initialize the first student with the first bag
    student_count = 1
    current_min_mangoes = mango_bags[0]
    current_max_mangoes = mango_bags[0]
    
    for i in range(1, len(mango_bags)):
        # Update the current minimum and maximum mangoes for the current student
        current_min_mangoes = min(current_min_mangoes, mango_bags[i])
        current_max_mangoes = max(current_max_mangoes, mango_bags[i])
        
        # Check if the difference between max and min mangoes exceeds the allowed difference
        if current_max_mangoes - current_min_mangoes > max_difference:
            # If so, increment the student count and start with a new bag
            student_count += 1
            current_min_mangoes = mango_bags[i]
            current_max_mangoes = mango_bags[i]
        
        # If the number of students required exceeds the available students, return False
        if student_count > students:
            return False
    
    # Return True if the distribution is possible within the given maximum difference
    return True

def minimize_difference(mango_bags, students):
    # Sort the mango bags to facilitate the distribution process
    mango_bags.sort()
    
    # Initialize the binary search range
    left = 0
    right = mango_bags[-1] - mango_bags[0]
    
    # Perform binary search to find the minimum possible maximum difference
    while left < right:
        mid = (left + right) // 2
        
        # Check if the current difference can be achieved
        if can_distribute_mangoes(mango_bags, students, mid):
            right = mid
        else:
            left = mid + 1
    
    # The left pointer will point to the minimum possible maximum difference
    return left

if __name__ == "__main__":
    # List of N integers representing the number of mangoes in each bag
    mango_bags = [int(x) for x in input("Enter the number of mangoes in each bag (space-separated): ").split()]
    
    # Number of students in the class
    students = int(input("Enter the number of students in the class: "))
    
    # Calculate the minimum possible maximum difference
    result = minimize_difference(mango_bags, students)
    
    # Print the result
    print("Minimum possible maximum difference:", result)


def find_duplicates(list1, list2, list3):
    # Convert the lists to sets
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    # Find the intersection of the three sets
    duplicates = set1 & set2 & set3
    
    # Convert the set of duplicates back to a list and return it
    return list(duplicates)

if __name__ == "__main__":
    # You can replace these lists with your own lists
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [4, 5, 6, 7, 8, 9]
    list3 = [6, 7, 8, 9, 10]
    
    # Find the duplicates in the three lists
    duplicates = find_duplicates(list1, list2, list3)
    
    # Print the list of duplicates
    print("Duplicates in the three lists:", duplicates)


def find_first_non_repeating_element(nums):
    # Create a dictionary to store the count of each element
    count_dict = {}
    
    # First pass: Count the occurrences of each element in the list
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
            
    # Second pass: Find the first non-repeating element
    for num in nums:
        if count_dict[num] == 1:
            return num
    
    # If no non-repeating element is found, return None
    return None

# Example usage
nums = [4, 5, 1, 2, 0, 4, 1]
result = find_first_non_repeating_element(nums)
if result is not None:
    print(f"The first non-repeating element in the list is: {result}")
else:
    print("There is no non-repeating element in the list.")



def find_minimum_in_rotated_sorted_list(nums):
    # Initialize left and right pointers
    left = 0
    right = len(nums) - 1
    
    # Perform binary search
    while left < right:
        # Calculate the middle index
        mid = left + (right - left) // 2
        
        # Compare the middle element with the rightmost element
        if nums[mid] > nums[right]:
            # If the middle element is greater than the rightmost element,
            # the minimum element must be in the right half
            left = mid + 1
        else:
            # Otherwise, the minimum element must be in the left half (including mid)
            right = mid
    
    # At the end of the loop, left and right will point to the minimum element
    return nums[left]

# Example usage
nums = [15, 18, 2, 3, 6, 12]
minimum = find_minimum_in_rotated_sorted_list(nums)
print(f"The minimum element in the rotated sorted list is: {minimum}")


def find_triplet_with_sum(nums, target):
    # Sort the list to use two-pointer technique
    nums.sort()
    
    # Iterate through each element in the list
    for i in range(len(nums) - 2):
        # Set the left and right pointers
        left = i + 1
        right = len(nums) - 1
        
        # Use two-pointer technique to find a pair with the remaining sum
        while left < right:
            # Calculate the current sum of the triplet
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                # If the current sum is equal to the target, return the triplet
                return (nums[i], nums[left], nums[right])
            elif current_sum < target:
                # If the current sum is less than the target, move the left pointer to the right
                left += 1
            else:
                # If the current sum is greater than the target, move the right pointer to the left
                right -= 1
    
    # 


def has_sublist_with_sum_zero(nums):
    # Create a set to store cumulative sums
    cumulative_sum_set = set()
    # Initialize cumulative sum to zero
    cumulative_sum = 0
    
    # Iterate through the list
    for num in nums:
        # Add the current number to the cumulative sum
        cumulative_sum += num
        
        # If cumulative sum is zero, or it is already in the set, we have found a sub-list with sum zero
        if cumulative_sum == 0 or cumulative_sum in cumulative_sum_set:
            return True
        
        # Add the cumulative sum to the set
        cumulative_sum_set.add(cumulative_sum)
    
    # If no sub-list with sum zero is found, return False
    return False

# Example usage
nums = [4, 2, -3, 1, 6]
result = has_sublist_with_sum_zero(nums)
if result:
    print("There is a sub-list with sum equal to zero.")
else:
    print("There is no sub-list with sum equal to zero.")
