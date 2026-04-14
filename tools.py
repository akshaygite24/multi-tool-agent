from langchain.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Useful for solving mathematical expressions like addition, subtraction, multiplication, division.
    use this tool for any numeric calculations.
    Example: "25 * 4"
    """

    try:
        return str(eval(expression))
    except:
        return "Error in calculation!"
    

@tool
def string_length(text: str) -> str:
    """
    Useful for counting the number of characters in the text or sentence.
    use this tool if user asks to count characters.
    Example: "hello" = 5
    """
    try:
        return str(len(text))
    except:
        return "Error finding number of characters!"
    
@tool
def word_count(text: str) -> str:
    """
    Useful for counting the number of words in the text or sentence.
    use this tool if user asks to count words.
    Example: "I Love Agents" = 3
    """
    try:
        return str(len(text.split()))
    except:
        return "Error finding number of words!"