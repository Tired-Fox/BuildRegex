import { createRegExp, exactly, charIn, charNotIn, letter, times, not, tab } from 'magic-regexp';

const r1 = createRegExp(charIn("abc").and(charNotIn("def")).and(not.letter.lowercase))
console.log(r1);

const r2 = createRegExp(tab.and(letter.uppercase))
const r3 = createRegExp(exactly(".[]()^${}|"))
const r4 = createRegExp(exactly(".[]()^${}|").optionally().at.lineStart().at.lineEnd().as("cat"))