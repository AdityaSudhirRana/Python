def manipulate_sentence():    
    sentence = input("Enter a sentence: ")
    
    word_count = len(sentence.split())
    char_count = len(sentence)
    
    lower_case = sentence.lower()
    upper_case = sentence.upper()
    underscore_replace = sentence.replace(" ", "_")
    
    print("\n" + "=" * 60)
    print(f"Original:        {sentence}")
    print("-" * 60)
    print(f"Word Count:      {word_count}")
    print(f"Character Count: {char_count}")
    print(f"Lowercase:       {lower_case}")
    print(f"Uppercase:       {upper_case}")
    print(f"Underscored:     {underscore_replace}")
    print("=" * 60)

manipulate_sentence()
