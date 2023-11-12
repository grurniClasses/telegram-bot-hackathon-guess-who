people_images = {}
lst_of_cheers = ["לפעמים צריך להגיד לבן אדם את האמת בפנים: אתה אפס" ,"אווץ' זה כאב","לך תנוח, תשתה קפה","אם היית טוב לא היית עושה בוטקאמפ","חוכמה זה לא הצד החזק שלך","לא ברור איך התקבלת לתוכנית", "במקרה שלך ספציפית האשמה היא של ורד ומיכל", "אם כל טיפש היה עץ הקבוצה הזו הייתה פרדס"
                 "נראה לי שרייכמן גדול עליך"]
lst_names =["ברק אובמה","בנימין נתניהו", "שאול מופז", "לוי אשכול", "דני קושמרו", "עמית סגל", "בר רפאלי","גל גדות" ]
basic_url = r"C:\Users\97252\Documents\בוטקאמפ\botP\ "
basic_url = basic_url.rstrip()
for name in lst_names:
    people_images[name] = basic_url + name + ".jpg"

def hint_0(name: str):
    index =name.find(' ')
    output_str = f"first name: {index} letters, last name: {len(name)- index-1} letters"
    return output_str
print(people_images)
