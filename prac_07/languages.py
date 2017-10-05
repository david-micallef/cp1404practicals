from prac_07.programming_language import ProgrammingLanguage

languages = []

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
languages.append(ruby)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
languages.append(python)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
languages.append(visual_basic)

print(python)

print("The dynamically typed languages are: ")
for language in languages:
    if language.is_dynamic():
        print(language.name)
