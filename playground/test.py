from build_regex import *


sample = "id: 2023-02-06T13:23"

pattern = build_regex(
    exactly("id: ")
        .then(digit().times(3).capture("time"))
        .then("m")
        .then(digit().times(3).capture("date"))
)

id = exactly("id: ")
time = digit().between(1,2).then(":").then(digit().between(1, 2)).capture("time")
date = (
    digit().times(4)
        .then("-")
        .then(digit().between(1, 2))
        .then("-")
        .then(digit().between(1, 2))
        .capture("date")
)

expr = build_regex(id.then(date).then("T").then(time))
match = expr.match(sample)

print(sample)
print(match, match.groups())
print(f"time: {match.group('time')}, date: {match.group('date')}")