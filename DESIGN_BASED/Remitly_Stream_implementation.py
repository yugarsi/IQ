# Your last Python3 code is saved below:
# print("Hello")


'''
String input


Stream(String input)


boolean hasNext()
String next();

String = "Test"
true
T
true
e
true
s
true
t
false
error (RntimeException)

"h"

$10,000,
"I have $20 with $10 in it"

getCurrencyValues(String currency, Stream stream) {
  return [20, 10];
}

1. currency (multicharacter currency); "mB" "hytuhg" "$$$$"
2. decimal value (.);

'''


class Stream:

    def __init__(self, string):
        self.buffer = string
        self.counter = 0

    def next(self):
        if len(self.buffer) == self.counter:
            raise ("Error")

        res = self.buffer[self.counter]
        self.counter += 1
        return res

    def hasnext(self):
        return self.counter < len(self.buffer)


stream = Stream(
    "In have $$$20 with $ 10  $asbde54  $2$3$4$5$54.67$.789$45.9.78 $34545756576 $.46765 $0.24 $56.43 $34.56.788.765 $sdbdhe.45 $65.ndjwf $54.000000");


def getCurrencyValues(currency, stream):
    res = []
    while stream.hasnext():
        cur = stream.next()
        if cur == currency:
            amount = ""
            while stream.hasnext():
                num = stream.next();
                if num.isnumeric():
                    amount += num
                elif num == currency:
                    if amount != "":
                        res.append(amount)
                        amount = ""
                else:
                    break
            if amount != "":
                res.append(amount)

    return res


def getCurrencyValuesWithdecimal(currency, stream):
    res = []
    while stream.hasnext():
        cur = stream.next()
        if cur == currency:
            amount = ""
            while stream.hasnext():
                num = stream.next();
                if num.isnumeric():
                    amount += num

                elif num == ".":
                    if amount == "":
                        break
                    if amount != "" and "." not in amount:
                        amount += num

                elif num == currency:
                    if amount != "":
                        res.append(amount)
                        amount = ""

                else:
                    break

            if amount != "":
                res.append(amount)

    return res


# stream = Stream("my $10, $20")
"$.5"

stream = Stream(
    "In have $$$20 with $ 10  $asbde54  $2$3$4$5$54.67$.789$45.9.78 $34545756576 $.46765 $0.24 $56.43 $34.56.788.765 $sdbdhe.45 $65.ndjwf $54.000000");

print(getCurrencyValuesWithdecimal("$", stream))
