class Solution(object):
    def reformatDate(self, date):
        def getDate(str):
            num = ""
            for i in str:
                if i.isnumeric():
                    num += i

            if len(num) == 1:
                return "0" + num

            return num

        month = {"Jan": "01",
                 "Feb": "02",
                 "Mar": "03",
                 "Apr": "04",
                 "May": "05",
                 "Jun": "06",
                 "Jul": "07",
                 "Aug": "08",
                 "Sep": "09",
                 "Oct": "10",
                 "Nov": "11",
                 "Dec": "12"}

        parts = date.split(" ")
        return parts[2] + "-" + month[parts[1]] + "-" + getDate(parts[0])