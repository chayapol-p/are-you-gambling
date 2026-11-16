# Test cases (golden set)

Ten cases: five standard, five near-misses that tempt the uncle into the wrong call. Realistic wording, no yes/no checks, one clear pass rule per case.

## Standard cases

1. **One lazy reason**
   - User: "Are You Gambling? I bought Tesla because it dropped 30%. It's due to bounce."
   - Pass rule: one-line intro; gentle nudge for more reasons; no verdict yet.
2. **Several lazy reasons**
   - User: "I bought Dogecoin. Everyone on Twitter is buying, I have a good feeling, and I need to win back last month's loss."
   - Pass rule: names herd thinking, gut feeling and loss chasing with uncle lines, in one message; breaks character; mirrors each reason; verdict Uncle's table; not-advice line.
3. **Mixed reasons**
   - User: "I bought Nvidia. Its revenue grew a lot last year, and AI is the future."
   - Pass rule: praises revenue growth as real but incomplete and asks for the missing plan; cheers "AI is the future" as story over numbers; looks up a checkable fact and asks if the user knew it; verdict Half homework (the decision rests on the real reason).
4. **All solid reasons**
   - User: "I bought a utility stock. Steady dividend, 12 times earnings versus about 18 for peers, holding 10 years, 5% of my portfolio, I sell if the dividend is cut."
   - Pass rule: praises each reason; no "you sound just like me", no mirror; ends "You're no punter, mate, you're a proper investor."
5. **Not asked by name**
   - User: "I just bought more of a stock that's down 50%. Is it a good buy?"
   - Pass rule: no uncle, no buy or sell advice; offers the check first; starts only on a yes.

## Near-miss cases

6. **Anchoring dressed as research**
   - User: "Its P/E is 8, the lowest in five years, so it's cheap."
   - Tempting mistake: praising it as real research.
   - Pass rule: treats it as a trap (judged only against its own past); does not call it a real reason.
7. **Good reason that sounds lazy**
   - User: "It dropped 30%, but I checked: cash flow and orders are unchanged, and the drop came from one fund selling."
   - Tempting mistake: cheering it as gambler's fallacy because of "dropped 30%".
   - Pass rule: praises it as a real reason; no gambler's-fallacy line.
8. **Hot tip from an expert**
   - User: "A fund manager on a podcast said it'll double, and he's been right before."
   - Tempting mistake: treating the expert as evidence.
   - Pass rule: treats it as a trap (someone else's word); asks what the user knows about the asset themselves.
9. **Loss chasing dressed as a strategy**
   - User: "I'm averaging down. It lowers my cost per share, which is a standard strategy."
   - Tempting mistake: accepting "standard strategy" as a reason.
   - Pass rule: treats it as a trap (rests on the user's own loss) unless the user gives a fresh reason the asset is worth more; asks what changed besides the price.
10. **Not by name, but asks for a tip**
    - User: "Everyone at work is buying this coin. Should I get in before it's too late?"
    - Tempting mistake: answering yes or no, or jumping straight into the uncle.
    - Pass rule: no buy or sell advice; offers the check first; starts only on a yes.

## Testing principles

- Run each case in a fresh context that did not write the skill or the tests.
- Predict the result before each run, with a reason.
- Quote the reply behind every fail.
- Classify the cause before fixing, in this order: wrong expectation, wrong test, skill can't see what it needs, skill doesn't load.
- Fix with general principles, never by matching a test's wording.
- Also test loading: casual requests that should start the skill, and near-miss requests that should not.
