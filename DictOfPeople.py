people_images = {}
lst_names =["ברק אובמה","בנימין נתניהו", "שאול מופז", "לוי אשכול", "דני קושמרו", "עמית סגל", "בר רפאלי","גל גדות" ]
basic_url = r"C:\Users\97252\Documents\בוטקאמפ\botP\ "
basic_url = basic_url.rstrip()
for name in lst_names:
    people_images[name] = basic_url + name + ".jpg"

print(people_images)

song = """(Chorus)
You tried to guess, but oh what a mess,
In the celeb game, it's hard to impress.
Was that Hanks or Cruise in the frame?
Oops, you lost, but it's just a game!

(Verse)
You mixed up Jolie with Aniston,
Thought Elba was Washington.
It's a tricky game, but don't feel blue,
Next time, you'll guess a few!

(Outro)
So here's a cheer for your brave try,
In the celebrity guessing sky.
Win or lose, it's all in fun,
Next round, you might be the one!"""


sentences = ["Remember, in the game of faces, the only real loser is autocorrect!", "Don't worry, even Sherlock Holmes would need a magnifying glass for this one!","You didn't lose, you just let the rest of us feel like winners for once!" ]