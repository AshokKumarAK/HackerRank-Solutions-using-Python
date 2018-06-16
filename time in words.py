minutes= ["one minute","two minutes","three minutes","four minutes",
                "five minutes",
                "six minutes",
                "seven minutes",
                "eight minutes",
                "nine minutes",
                "ten minutes",
                "eleven minutes",
                "twelve minutes",
                "thirteen minutes",
                "forteen minutes",
                "quarter",
                "sixteen minutes",
                "seventeen minutes",
                "eighteen minutes",
                "nineteen minutes",
                "twenty minutes",
                "twenty one minutes",
                "twenty two minutes",
                "twenty three minutes",
                "twenty four minutes",
                "twenty five minutes",
                "twenty six minutes",
                "twenty seven minutes",
                "twenty eight minutes",
                "twenty nine minutes",
                "half"]
hours=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
h = int(input().strip())
m = int(input().strip())
if m==0:
    print(hours[h-1],"o' clock")
elif m<=30:
    print(minutes[m-1],"past",hours[h-1])
else:
    print(minutes[60-m - 1], "to", hours[h])
