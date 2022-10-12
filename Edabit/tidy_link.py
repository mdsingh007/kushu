def tidy_link(link, name, hover_text=""):
    return f"[{name}]({link} {hover_text})"

print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))
# "[this](https://edabit.com/challenges "Go to the challenges!")"
print(tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!"))
# "[Click Me!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
