# Build Regex

Class that allows you to build a regex string from understandably named methods. Allows for advanced regex operations and opens regex up for everyone without knowing the advanced parts of it. It will be treated similar to a query system or key word class builder syntax. Inspiration for this project is [magic-regexp](https://regexp.dev/getting-started/setup).

```python
"""
?Character classes
([xyz] or [a-z]) Character class matching one of enclosed characters
    !chars()
([^xyz] or [^a-z]) negated for complemented character class
    !not.chars()
(.) Matches any single character that isn't a line terminator
    !any()
(\d) Matches any digit == ([0-9])
    !digit()
(\D) Matches any character that is not a digit == ([^0-9])
    !not.digit()
(\w) Matches any alphanumeric character from basic Latin alphabet == ([A-Za-z0-9_])
    !word_char()
(\W) Matches any character that is not a word character from basic Latin alphabet == ([^A-Za-z0-9_])
    !not.word_char()
(\s) Matches signle white space. Space, tab, form feed, line feed, ==
    ([ \f\n\r\t\v\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff])
    !whitespace()
(\S) Matches a signle character other than white space ==
    ([^ \f\n\r\t\v\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff])
    !not.whitespace()
(\t) Horizontal tab
    !htab()
(\r) Carriage return
    !cr()
(\n) Line feed
    !new_line()
(\v) Vertical tab
    !vtab()
(\f) Form feed
    !form_feed()
([\b]) Backspace
    !backspace()
(\0) NUL
    !nul()
(\cX) Matches control character using caret notation where X == [A-Z]. \cM == "\r" in "\r\n"
    !control()
(\xhh) Matches character with two hexadecimal digits
    !hex_2()
(\uhhhh) Matcches UTF-16 code-unit. Four hexadecimal digit
    !utf_16()
(\u{hhhh} or \u{hhhhh}) Only when u is set. Matches unicode value U+hhhh or U+hhhhh
    !unicode()
(\) Escape
    !exactly()
(x|y) Disjunction. either "x" or "y"
    !or()

?Boundry Assertions
(^) begin
    !begin()
($) end
    !end()
(\b) word boundry
    !wb()
(\B) non-word boundry
    !not.wb()

?Assertions
(?=) look ahead
    !before()
(?!) negative lookahead
    !after()
(?<=) lookbehind
    !not_before()
(?<!) negative lookbehind
    !not_after()

?Groups and backreferences
(x) Capturing group
    !capture()
(?<Name>x) Named capturing group
    !capture("name")
(?:x) non capturing group
    !group()
(\n) where n is a number. A back reference to the last substring matching the n parenthetical
    !ref(n>=0)
(\k<Name>) A back reference to the last substring matching the Named capture group
    !ref("name")

?Quantifiers
(*) 0 or more
    !noneOrMore()
(+) 1 or more
    !oneOrMore()
(?) matches the preceding object 0 or 1 times
    !optional()
({n}) matches exactly n occurrences
    !times()
({n,}) matches at least n occurrences
    !times.atLeast()
({n,m}) matches at least n and up to m occurrences
    !times.range()
\? following *, +, ?, {n}, {n,}, {m,n} makes the quantifiers stop after first match. Makes them non greedy

!maybe(), word(), options(), letter 
"""
```