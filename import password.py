import re

def analyze_password(password):
    """
    Analyze a password for complexity requirements.
    
    Args:
        password (str): The password to analyze.
    
    Returns:
        dict: A dictionary with results of the analysis.
    """
    result = {
        "has_uppercase": bool(re.search(r'[A-Z]', password)),
        "has_lowercase": bool(re.search(r'[a-z]', password)),
        "has_digit": bool(re.search(r'\d', password)),
        "has_special_char": bool(re.search(r'[$%*&_]', password)),
        "is_complex": False
    }

    # A password is considered complex if it meets all requirements
    result["is_complex"] = all(result.values())
    return result

def test_password(password):
    analysis = analyze_password(password)
    print(f"Password: {password}")
    print("Complexity Analysis:")
    for key, value in analysis.items():
        print(f"  {key.replace('_', ' ').capitalize()}: {'Yes' if value else 'No'}")
    if not analysis["is_complex"]:
        print("The password does not meet all complexity requirements.")
    else:
        print("The password meets all complexity requirements.")
    print("\n")

# Example usage
if _name_ == "_main_":
    passwords = [
        "Simple123",
        "Complex$123",
        "weakpassword",
        "UPPER123",
        "Lower$123",
        "NoSpecialChar123",
        "OnlySpecial_$"
    ]
    for pw in passwords:
        test_password(pw)
