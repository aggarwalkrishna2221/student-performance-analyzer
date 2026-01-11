# This function calculates grade based on average marks

total = 0
count = 0
initial = True

while initial is True:
    input_score = input("Enter your marks (out of 100):- ")
    if input_score=="done":
        break
    try:
        float_input = float(input_score)
    except:
        print("Invalid Input")
        continue

    total += float_input
    count+=1

average = total/count
print("Average: ", average)
if average>80:
    print("Grade: A")
elif average>70:
    print("Grade: B")
elif average>50:
    print("Grade: C")
elif average>40:
    print("Grade: D")
elif average<40:
    print("Grade: Fail")



