import akinator
from  jarvis_command import speak,listen_to_user
from difflib import get_close_matches
aki = akinator.Akinator()
speak("welcome to akinator")
speak("Chose your mode")
mode=['character','animal','object']
print(mode)
take=listen_to_user()
if take==None:
    take="character"
chose=get_close_matches(take,mode)
if chose[0]=="character":
    q = aki.start_game()
elif chose[0]=="animal":
    q=aki.start_game(language="en_animals")
elif chose[0]=="object":
    q=aki.start_game(language="en_objects")
elif chose==[]:
    speak("not able to understand")
    q=aki.start_game()
answers=['yes','y','no','n','i','idk','i dont know','probably','probably not','b','back','0','1','2','3','4']
while aki.progression <= 80:
    speak(q)
    ans=listen_to_user()
    if ans==None:
        ans="yes"
    ans1=get_close_matches(ans,answers)
    if ans1==[]:
        ans1=['yes']
    a=ans1[0]
    print(a)
    if a == "b" or a=="back":
        try:
            q = aki.back()
        except akinator.CantGoBackAnyFurther:
            pass
    else:
        q = aki.answer(a)
aki.win()

speak(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?")
correct=listen_to_user()
if correct==None:
    correct="yes"
if correct.lower() == "yes" or correct.lower() == "y":
    speak("Yay")
else:
    speak("Oof")