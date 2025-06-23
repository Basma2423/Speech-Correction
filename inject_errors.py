from src.error_injection import inject_error, ErrorProbabilities

text = "ثُمَّ ذَكَرَهَا هَكَذَا مِائَةً مِائَةً حَتَّى بَلَغَ أَلْفًا قَالَ ثُمَّ فِى كُلِّ مَا زَادَتْ مِائَةَ شَاةٍ شَاةٌ"
print("Original text:", text)
print("Text with errors:", inject_error(text, error_type="speech"))

# try with custom probabilities

ep = ErrorProbabilities(
    phonetic=0.1,
    no_error=0.1,
    replace_diacritics=0.9,
    remove_diacritics=0.1
)

print("Original text:", text)
print("Text with errors:", inject_error(text, error_type="speech", probs=ep))