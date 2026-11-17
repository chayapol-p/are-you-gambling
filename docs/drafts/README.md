# Are You Gambling?

**If your reason isn't better than the uncle's red or black, you're gambling, not investing.**

A Claude skill that tests your reason for buying a stock or coin. Tell it why you bought. Your neighbour uncle, who loves a flutter, will cheer you on if your reason sounds like his. That's the problem.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/mirror-dark.png">
  <img src="docs/images/mirror.png" width="100%" alt="Diagram that shows a stock down 30 percent beside a roulette table with five reds in a row: both bet the past will turn.">
</picture>

> **You:** I bought a stock that's down 30%. It'll bounce back now.
>
> **Uncle:** Down 30%, so it's due to come back? **Black is due!** Five reds in a row at my table, and I put the lot on black, mate.
>
> **Uncle:** Hang on, mate, you sound just like me.
>
> **Verdict: Uncle's table.** The buy rests on the price drop alone, with no reason about the company itself.

<sub>Trimmed from a real test run. The full reply also checks a fact about how often big drops come back, and asks what you know about the company that the uncle doesn't.</sub>

## What it does

- Asks for all your reasons in one go.
- Cheers the weak ones with the uncle's version, and praises the real ones out loud.
- Breaks character, puts your reasons beside his, and looks up facts you may have missed.
- Gives a verdict: Uncle's table, Lucky punter, Half homework, or Proper investor.

It judges the thinking behind a reason, not its wording. Ten common traps are in `references/traps.md`, from the gambler's fallacy to loss chasing.

## Install

**Claude Code** (as a plugin; `claude plugin update are-you-gambling` gets new versions):

```bash
claude plugin marketplace add chayapol-p/are-you-gambling
claude plugin install are-you-gambling@are-you-gambling
```

Inside a Claude Code session, the same two commands start with `/plugin` instead of `claude plugin`.

**Claude Code** (as a plain skill folder):

```bash
git clone https://github.com/chayapol-p/are-you-gambling
mkdir -p ~/.claude/skills
cp -r are-you-gambling/skills/are-you-gambling ~/.claude/skills/
```

**Claude app** (web, desktop or mobile, on any plan with code execution turned on):

1. Download `are-you-gambling.zip` from the [latest release](https://github.com/chayapol-p/are-you-gambling/releases/latest).
2. Open **Customize → Skills**, click **+**, then **Create skill → Upload a skill**, and pick the zip.

## Try it

Type: `Are You Gambling? I bought <asset> because <your reason>.`

## Not financial advice

This is a thinking check. It never tells you to buy or sell.

## Licence

MIT, by chayapol.par
