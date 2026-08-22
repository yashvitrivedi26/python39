''' write a program for male female marriage compatibility as per below link,  accept birth day and birth month from user as separate input. decide zodiac sign as per previous example and then use zodiac sign to decide  marriage compatibility

https://miro.medium.com/v2/resize:fit:1100/format:webp/1*f58HMTVzfN2XvCPR23wXgA.jpeg'''

# Female Birth Date
f_b_day = int(input("Enter Female Birth-Day: "))
f_b_month = int(input("Enter Female Birth-Month: "))

# Female Zodiac Sign

if (f_b_month == 1 and f_b_day >= 20) or (f_b_month == 2 and f_b_day <= 18):
    f_sign = "Aquarius"

elif (f_b_month == 2 and f_b_day >= 19) or (f_b_month == 3 and f_b_day <= 20):
    f_sign = "Pisces"

elif (f_b_month == 3 and f_b_day >= 21) or (f_b_month == 4 and f_b_day <= 19):
    f_sign = "Aries"

elif (f_b_month == 4 and f_b_day >= 20) or (f_b_month == 5 and f_b_day <= 20):
    f_sign = "Taurus"

elif (f_b_month == 5 and f_b_day >= 21) or (f_b_month == 6 and f_b_day <= 21):
    f_sign = "Gemini"

elif (f_b_month == 6 and f_b_day >= 22) or (f_b_month == 7 and f_b_day <= 22):
    f_sign = "Cancer"

elif (f_b_month == 7 and f_b_day >= 23) or (f_b_month == 8 and f_b_day <= 22):
    f_sign = "Leo"

elif (f_b_month == 8 and f_b_day >= 23) or (f_b_month == 9 and f_b_day <= 22):
    f_sign = "Virgo"

elif (f_b_month == 9 and f_b_day >= 23) or (f_b_month == 10 and f_b_day <= 22):
    f_sign = "Libra"

elif (f_b_month == 10 and f_b_day >= 24) or (f_b_month == 11 and f_b_day <= 21):
    f_sign = "Scorpio"

elif (f_b_month == 11 and f_b_day >= 22) or (f_b_month == 12 and f_b_day <= 21):
    f_sign = "Sagittarius"

elif (f_b_month == 12 and f_b_day >= 22) or (f_b_month == 1 and f_b_day <= 19):
    f_sign = "Capricorn"

else:
    f_sign = "Invalid"


# Male Birth Date
m_b_day = int(input("Enter Male Birth-Day: "))
m_b_month = int(input("Enter Male Birth-Month: "))

# Male Zodiac Sign

if (m_b_month == 1 and m_b_day >= 20) or (m_b_month == 2 and m_b_day <= 18):
    m_sign = "Aquarius"

elif (m_b_month == 2 and m_b_day >= 19) or (m_b_month == 3 and m_b_day <= 20):
    m_sign = "Pisces"

elif (m_b_month == 3 and m_b_day >= 21) or (m_b_month == 4 and m_b_day <= 19):
    m_sign = "Aries"

elif (m_b_month == 4 and m_b_day >= 20) or (m_b_month == 5 and m_b_day <= 20):
    m_sign = "Taurus"

elif (m_b_month == 5 and m_b_day >= 21) or (m_b_month == 6 and m_b_day <= 21):
    m_sign = "Gemini"

elif (m_b_month == 6 and m_b_day >= 22) or (m_b_month == 7 and m_b_day <= 22):
    m_sign = "Cancer"

elif (m_b_month == 7 and m_b_day >= 23) or (m_b_month == 8 and m_b_day <= 22):
    m_sign = "Leo"

elif (m_b_month == 8 and m_b_day >= 23) or (m_b_month == 9 and m_b_day <= 22):
    m_sign = "Virgo"

elif (m_b_month == 9 and m_b_day >= 23) or (m_b_month == 10 and m_b_day <= 22):
    m_sign = "Libra"

elif (m_b_month == 10 and m_b_day >= 24) or (m_b_month == 11 and m_b_day <= 21):
    m_sign = "Scorpio"

elif (m_b_month == 11 and m_b_day >= 22) or (m_b_month == 12 and m_b_day <= 21):
    m_sign = "Sagittarius"

elif (m_b_month == 12 and m_b_day >= 22) or (m_b_month == 1 and m_b_day <= 19):
    m_sign = "Capricorn"

else:
    m_sign = "Invalid"


# Display Zodiac Signs

print("\nFemale Zodiac Sign:", f_sign)
print("Male Zodiac Sign:", m_sign)


# Marriage Compatibility
# Based on the given chart

# Marriage Compatibility
if (
    (m_sign == "Aries" and f_sign == "Aries") or
    (m_sign == "Aries" and f_sign == "Leo") or
    (m_sign == "Aries" and f_sign == "Sagittarius") or
    (m_sign == "Aries" and f_sign == "Gemini") or
    (m_sign == "Aries" and f_sign == "Libra") or
    (m_sign == "Aries" and f_sign == "Aquarius") or
    (m_sign == "Leo" and f_sign == "Aries") or
    (m_sign == "Leo" and f_sign == "Leo") or
    (m_sign == "Leo" and f_sign == "Sagittarius") or
    (m_sign == "Leo" and f_sign == "Gemini") or
    (m_sign == "Leo" and f_sign == "Libra") or
    (m_sign == "Leo" and f_sign == "Aquarius") or
    (m_sign == "Leo" and f_sign == "Cancer") or
    (m_sign == "Leo" and f_sign == "Scorpio") or
    (m_sign == "Leo" and f_sign == "Pisces") or
    (m_sign == "Sagittarius" and f_sign == "Aries") or
    (m_sign == "Sagittarius" and f_sign == "Leo") or
    (m_sign == "Sagittarius" and f_sign == "Sagittarius") or
    (m_sign == "Sagittarius" and f_sign == "Gemini") or
    (m_sign == "Sagittarius" and f_sign == "Libra") or
    (m_sign == "Sagittarius" and f_sign == "Aquarius") or
    (m_sign == "Taurus" and f_sign == "Taurus") or
    (m_sign == "Taurus" and f_sign == "Virgo") or
    (m_sign == "Taurus" and f_sign == "Capricorn") or
    (m_sign == "Taurus" and f_sign == "Cancer") or
    (m_sign == "Taurus" and f_sign == "Scorpio") or
    (m_sign == "Taurus" and f_sign == "Pisces") or
    (m_sign == "Virgo" and f_sign == "Taurus") or
    (m_sign == "Virgo" and f_sign == "Virgo") or
    (m_sign == "Virgo" and f_sign == "Capricorn") or
    (m_sign == "Virgo" and f_sign == "Cancer") or
    (m_sign == "Virgo" and f_sign == "Scorpio") or
    (m_sign == "Capricorn" and f_sign == "Taurus") or
    (m_sign == "Capricorn" and f_sign == "Virgo") or
    (m_sign == "Capricorn" and f_sign == "Capricorn") or
    (m_sign == "Capricorn" and f_sign == "Cancer") or
    (m_sign == "Capricorn" and f_sign == "Scorpio") or
    (m_sign == "Capricorn" and f_sign == "Pisces") or
    (m_sign == "Gemini" and f_sign == "Aries") or
    (m_sign == "Gemini" and f_sign == "Leo") or
    (m_sign == "Gemini" and f_sign == "Gemini") or
    (m_sign == "Gemini" and f_sign == "Libra") or
    (m_sign == "Gemini" and f_sign == "Aquarius") or
    (m_sign == "Libra" and f_sign == "Leo") or
    (m_sign == "Libra" and f_sign == "Sagittarius") or
    (m_sign == "Libra" and f_sign == "Gemini") or
    (m_sign == "Libra" and f_sign == "Libra") or
    (m_sign == "Libra" and f_sign == "Aquarius") or
    (m_sign == "Aquarius" and f_sign == "Aries") or
    (m_sign == "Aquarius" and f_sign == "Leo") or
    (m_sign == "Aquarius" and f_sign == "Sagittarius") or
    (m_sign == "Aquarius" and f_sign == "Gemini") or
    (m_sign == "Aquarius" and f_sign == "Libra") or
    (m_sign == "Aquarius" and f_sign == "Aquarius") or
    (m_sign == "Cancer" and f_sign == "Taurus") or
    (m_sign == "Cancer" and f_sign == "Virgo") or
    (m_sign == "Cancer" and f_sign == "Capricorn") or
    (m_sign == "Cancer" and f_sign == "Cancer") or
    (m_sign == "Cancer" and f_sign == "Scorpio") or
    (m_sign == "Cancer" and f_sign == "Pisces") or
    (m_sign == "Scorpio" and f_sign == "Taurus") or
    (m_sign == "Scorpio" and f_sign == "Virgo") or
    (m_sign == "Scorpio" and f_sign == "Capricorn") or
    (m_sign == "Scorpio" and f_sign == "Cancer") or
    (m_sign == "Scorpio" and f_sign == "Scorpio") or
    (m_sign == "Scorpio" and f_sign == "Pisces") or
    (m_sign == "Pisces" and f_sign == "Taurus") or
    (m_sign == "Pisces" and f_sign == "Cancer") or
    (m_sign == "Pisces" and f_sign == "Scorpio") or
    (m_sign == "Pisces" and f_sign == "Pisces")
):
    print("Marriage Compatibility: Great Match")

elif (
    (m_sign == "Aries" and f_sign == "Virgo") or
    (m_sign == "Aries" and f_sign == "Pisces") or
    (m_sign == "Leo" and f_sign == "Taurus") or
    (m_sign == "Sagittarius" and f_sign == "Cancer") or
    (m_sign == "Sagittarius" and f_sign == "Scorpio") or
    (m_sign == "Sagittarius" and f_sign == "Pisces") or
    (m_sign == "Taurus" and f_sign == "Leo") or
    (m_sign == "Taurus" and f_sign == "Libra") or
    (m_sign == "Virgo" and f_sign == "Leo") or
    (m_sign == "Virgo" and f_sign == "Aquarius") or
    (m_sign == "Virgo" and f_sign == "Pisces") or
    (m_sign == "Capricorn" and f_sign == "Leo") or
    (m_sign == "Capricorn" and f_sign == "Libra") or
    (m_sign == "Gemini" and f_sign == "Sagittarius") or
    (m_sign == "Gemini" and f_sign == "Virgo") or
    (m_sign == "Gemini" and f_sign == "Capricorn") or
    (m_sign == "Libra" and f_sign == "Aries") or
    (m_sign == "Libra" and f_sign == "Taurus") or
    (m_sign == "Libra" and f_sign == "Pisces") or
    (m_sign == "Aquarius" and f_sign == "Scorpio") or
    (m_sign == "Aquarius" and f_sign == "Pisces") or
    (m_sign == "Cancer" and f_sign == "Leo") or
    (m_sign == "Cancer" and f_sign == "Sagittarius") or
    (m_sign == "Scorpio" and f_sign == "Aries") or
    (m_sign == "Scorpio" and f_sign == "Leo") or
    (m_sign == "Pisces" and f_sign == "Aries") or
    (m_sign == "Pisces" and f_sign == "Leo") or
    (m_sign == "Pisces" and f_sign == "Sagittarius") or
    (m_sign == "Pisces" and f_sign == "Virgo")
):
    print("Marriage Compatibility: Favorable Match")

else:
    print("Marriage Compatibility: Not Favorable")