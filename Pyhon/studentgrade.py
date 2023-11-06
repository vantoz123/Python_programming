def calculate_grade(assign1, assign2, final_exam):
    if assign1 > 50 or assign2 > 50 or final_exam > 100:
        return "Error: Assignment or final exam score exceeds maximum allowed."
    
    assignment_score = (assign1 + assign2) * (25/100)
    final_exam_score = final_exam

    final_score = (assignment_score) + (0.75 * final_exam_score)

    if final_score > 90:
        return "A+ (Outstanding)"
    elif final_score > 80:
        return "A (Very Good)"
    elif final_score >= 70:
        return "B (Good)"
    else:
        return "Fail"

def main():
    try:
        assign1 = float(input("Enter Assignment 1 score (out of 50): "))
        assign2 = float(input("Enter Assignment 2 score (out of 50): "))
        final_exam = float(input("Enter Final Examination score (out of 100): "))

        grade = calculate_grade(assign1, assign2, final_exam)

        print(f"Final Grade: {grade}")
    except ValueError:
        print("Error: Please enter valid numerical scores.")

if __name__ == "__main__":
    main()
