# Speech-Correction

## Error Types:
|=======================================================|
| Error types (each has it's own probability):          |
|=======================================================|
| 1. No errors                                          |
| 2. Speech errors                                      |
|   2.1. Phonetic errors                                |
|  2.2. Diacritic errors                                |
|       2.2.1. Remove diacritics (full, word, letter)   |
|       2.2.2. Replace diacritics                       |
| 3. Typing errors                                      |      
|   3.1. Keyboard errors                                |
|   3.2. Ordering errors                                |  
| 4. All errors combined (speech + typing)              | 
|=======================================================|

## To Preprocess a Txt File:
```python src/preprocess.py PATH_TO_THE_TXT_FILE.txt```
The file will be saved under the same name in ```preprocessed/```

# Main Approach

**\[Alshoki \+ …\]**  
Task 1: user speech \--\> Whisper \---\> text with diacritics (vocalized text)

**\[Selsabeel, Basma, …\]**  
Task 2: text with diacritics (vocalized text) **with some errors\*** \---\> LLM \---\> text with diacritics (vocalized text) but error-free

Step 2.1: Preprocess the  [Abdou/arabic-tashkeel-dataset](https://huggingface.co/datasets/Abdou/arabic-tashkeel-dataset) dataset with tools, or regex

Step 2.2: Introduce some errors to the processed dataset  

Step 2.3: Train an LLM 

\*errors include:  
	 typos like: (keyboard typing errors, e.g. j, m, l, or i instead of k),  
	 or characters sound like the correct character (س instead of ث),  
	or different diacritics (mispronunciations) (فتحة instead of كسرة أو ضمة)

Got some help from here:
[Arabic Text Diactrization](https://github.com/AbdelrahmanHamdyy/Arabic-Text-Diactrization)
