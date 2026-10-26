# Jobs: product, simplicity, and presentation evidence

Research date: 2026-10-26. Scope: three supplied transcripts, read through their unique content; exact repeated halves verified programmatically. This document separates what the materials report from operational rules proposed for the combined founder skill. Proposed rules are adaptations, not historical quotations or proof that a modern feature will work.

## Source identity and integrity

| Local ID | Supplied attachment | Material identified internally | Attribution and limits |
|---|---|---|---|
| JP | `8ff17b69-5864-49c4-af4c-d8391efecfb4/Pasted text.txt` | Founders episode discussing *The Presentation Secrets of Steve Jobs*, by Carmine Gallo; book identified lines 1–2, 0:00–0:06; episode identifies itself as 350 at lines 350–351, 36:00–36:07. | Narrator reads and interprets Gallo, interleaving other founders, personal anecdotes, and promotion. Not a Jobs interview. No original recording URL or publication date was supplied. |
| JC | `756ecf80-7e3c-46ec-86fe-59385374ff23/Pasted text.txt` | Founders episode 281 discussing *Creative Selection: Inside Apple’s Design Process During the Golden Age of Steve Jobs*, by Ken Kocienda; lines 32–41, 3:11–4:04; episode close lines 402–403, 40:59–41:06. | Narrator quotes a practitioner’s recollections. Kocienda’s reported experience is valuable first-person testimony, but the supplied text adds a second narrator and transcription layer. |
| JS | `0f888afa-b1a3-483d-87e7-3ff631df3d44/Pasted text.txt` | Founders episode 349 discussing *Insanely Simple: The Obsession That Drives Apple’s Success*, by Ken Segall; lines 1–7, 0:00–0:35; episode close line 417, 42:28. | Narrator summarizes and quotes Segall’s advertising-agency experience working with Jobs. The narrator also draws his own conclusions. Not every claim is Segall’s or Jobs’s. |

Paths above resolve under `/Users/angelobaricante/.codex/attachments/`. The host identifies his show as Founders and refers to listeners addressing him as David (JS lines 421–423); identifying him as David Senra is plausible, but not independently established from audio or publication metadata here.

All three files contain two identical copies: JP lines 1–457 repeat at 458–914; JC lines 1–403 repeat at 404–806; JS lines 1–514 repeat at 515–1028. These are one source each, not corroborating witnesses. The lack of a terminal newline causes `wc -l` to undercount by one. Canonical locators below use the first copy.

Transcription errors include author surnames rendered as “Gallow,” “Kenda,” and “seagull.” Treat exact wording, quotations, and named-entity spelling as provisional unless checked against an original. Preserve the supplied text as evidence; do not silently rewrite it and then cite the rewrite as original.

## Primary-source checks

1. [Apple Presents iPod, October 23, 2001](https://www.apple.com/newsroom/2001/10/23Apple-Presents-iPod/). Apple’s announcement confirms the customer-facing thousand-song pocket proposition and automatic synchronization with iTunes. This independently supports the launch message and system behavior described in JP and JS; it does not verify the narrator’s complete explanation of Jobs’s reasoning or competitive causality.
2. [Apple Unveils Safari, January 7, 2003](https://www.apple.com/newsroom/2003/01/07Apple-Unveils-Safari/). Apple led the launch with speed, stated comparative performance figures, and included a Jobs quotation emphasizing speed. This corroborates the public product priority in JC. Those were Apple’s launch claims; this research did not reproduce the historical benchmarks or establish the internal decision process.
3. [Steve Jobs Archive, *Make Something Wonderful*](https://book.stevejobsarchive.com/), sections “Speech to Apple Employees” (1997) and “Speech at Macworld” (1998). Jobs describes reducing the roadmap, simplifying customer choice, and concentrating teams on four products. This corroborates deliberate focus; it does not establish that every product must have one feature. The archive explicitly says its contents were edited and excerpted.

These checks establish selected historical evidence. They do not upgrade unverified quotations elsewhere in the transcripts into verified Jobs quotations.

## Ten operational principles

### JPR-01 — Define the customer improvement before choosing technology

**Evidence:** JP lines 16–38, 1:34–3:48: narrator attributes to Jobs a customer-experience-first approach and walks through the iMac internet-use proposition. JP lines 90–113, 9:22–11:42 contrast a product’s features with the improvement it offers. The exact 1997 quotation remains transcript-reported in this review. The iPod announcement above corroborates a concrete example of benefit-led positioning.

**Adaptation:** A feature proposal must name the user, situation, existing difficulty, and intended improvement before selecting an implementation. Mark unobserved customer needs as hypotheses.

**Test:** Someone unfamiliar with the proposal can explain the intended improvement without naming the stack or an AI model. Evidence of customer demand must come from the current project, not this historical example.

**Tension:** A benefit statement can still be wrong. Founder intuition does not replace customer observations or technical feasibility work.

### JPR-02 — Give a product a dominant quality target

**Evidence:** JC lines 180–187, 18:25–19:08: Kocienda’s account says Safari’s defining priority was speed and explains the expected immediate customer benefit. Apple’s Safari launch corroborates its public emphasis on performance. JC’s opening Lombardi analogy is Kocienda/narrator framing, not Jobs’s own analogy.

**Adaptation:** Set one dominant outcome for the current slice, with explicit minimum requirements for correctness, usability, and reliability. Use that outcome to reject attractive distractions.

**Test:** Given two viable designs, the team can explain which better serves the named priority and demonstrate the difference under an agreed measurement method.

**Tension:** Dominant does not mean exclusive. A fast browser that fails to render pages is not supported by this principle.

### JPR-03 — Advance decisions through concrete demos

**Evidence:** JC lines 51–61, 5:03–6:06 describe progression through problem, design, demo, and shipping. JC lines 208–230, 21:13–23:34 describe concrete artifacts, feedback, and successive iterations. These are Kocienda’s process recollections relayed by the host, not direct Jobs instructions to the present user.

**Adaptation:** Where an uncertainty concerns behavior, build the smallest artifact that exposes it. Record the question, what the demo showed, feedback, and the next change.

**Test:** Reviewers can interact with or inspect the disputed behavior. A follow-up demo visibly addresses prior feedback. Screenshots alone do not establish backend correctness.

**Tension:** A convincing demo may conceal reliability problems. Retain appropriate engineering checks and distinguish prototype behavior from completed implementation.

### JPR-04 — Remove unnecessary choices from the core experience

**Evidence:** JC lines 99–124, 10:01–12:43 recount Jobs examining two iPad keyboard designs, asking whether both were needed, then choosing after hearing the implementer’s preference. JC lines 149–173, 15:11–17:39 explain reducing features that overload users. JS lines 255–260, 26:00–26:31 recount a simpler disc-burning flow. The archive supports product-line focus at the company level.

**Adaptation:** Before adding a mode, option, configuration, or skill, identify the distinct user need it serves and whether a sensible default could satisfy it.

**Test:** Compare task completion and confusion for the simpler default against the proposed extra choice. Explain which necessary capabilities remain available.

**Tension:** The historical examples do not justify deleting accessibility, recovery, expert, or genuinely distinct workflow needs. “Always one” is an overgeneralization.

### JPR-05 — Review the artifact under the conditions in which users encounter it

**Evidence:** JC lines 163–173, 16:36–17:39 explain why software must make sense without someone narrating every feature. JS lines 180–188, 18:17–18:59 recount Jobs rejecting explanatory setup for advertisements because a reader would not receive it.

**Adaptation:** Review the first experience without coaching, developer context, or a sales explanation. Evaluate the interface and its actual in-product help together.

**Test:** A representative user can discover the primary action, complete the task, and recognize success. Capture where explanation was needed and decide whether the product should supply it.

**Tension:** Absence of a presenter does not mean absence of instructions. Complex, unfamiliar, or consequential tasks may need well-designed guidance.

### JPR-06 — Design the behavior and the whole journey

**Evidence:** JC lines 269–281, 27:33–28:46 relay a Jobs statement about design and then Kocienda’s interpretation that attractive appearance is insufficient. JC lines 237–253, 24:17–26:00 discuss preventing bad experiences and shift into *Becoming Steve Jobs* for the reputation argument. These passages change source layers and should not be flattened into a single direct quotation.

**Adaptation:** Review the path from discovery through setup, use, failure, support, and completion. Include interaction behavior and errors in design reviews.

**Test:** Demonstrate a complete realistic task, including a likely failure and recovery, instead of approving only an attractive static view.

**Tension:** The claim that one bad experience undoes dozens or hundreds of good ones is rhetorical here, not a verified numeric model.

### JPR-07 — Use judgment explicitly and keep it revisable

**Evidence:** JC lines 111–124, 11:22–12:43 show Jobs soliciting the implementer’s experience before a decision. JC lines 290–317, 29:44–32:33 contrast Kocienda’s account with Douglas Bowman’s Google criticism; the host adds broad anti-data interpretations. JS lines 213–227, 21:36–23:05 recount naming and advertising-supported-OS ideas Jobs reportedly reconsidered.

**Adaptation:** Name the decision owner, distinguish preference from evidence, explain the tradeoff, and specify what new observation would change the decision. Acknowledge when the materials contain no applicable founder evidence.

**Test:** A reader can identify the recommendation’s factual basis, subjective judgment, unresolved uncertainty, and review trigger.

**Tension:** Neither “Jobs was always right” nor “never use A/B tests” follows. Taste and measurable correctness answer different questions; current customer data can contradict a preference.

### JPR-08 — Pair decision authority with sustained engagement and specific feedback

**Evidence:** JC lines 67–81, 6:44–8:12 describe repeated reviews and precise next steps. JC lines 334–345, 34:04–35:10 explicitly reject leaders copying Jobs’s authority without his involvement. JS lines 146–163, 14:53–16:34 describe small groups and personal marketing involvement. Broad claims about approving every image are testimony, not independently audited facts.

**Adaptation:** Give each consequential decision an owner who reviews the evidence, states the next concrete change, and returns to assess it. Keep review participation relevant.

**Test:** Feedback specifies an observable improvement and a reviewer; the next review evaluates that change. Do not multiply simulated founder agents merely to create more opinions.

**Tension:** Personal engagement can become a bottleneck. These accounts do not prove that micromanagement, intimidation, insults, arbitrary headcount, or overriding specialist safeguards is required for good work.

### JPR-09 — Give communication one clear central idea and prove the benefit

**Evidence:** JS lines 229–248, 23:18–25:16 recount Lee Clow’s paper-ball demonstration against five simultaneous advertising messages. It was Clow teaching Jobs, not a tactic invented by Jobs. JP lines 119–145, 12:22–15:01 discuss a repeatable central message; JP lines 157–180, 16:18–18:38 discuss organizing supporting points. The iPod launch corroborates benefit-led wording.

**Adaptation:** State the central benefit plainly, then support it with relevant evidence and a demonstration. For a specification, use one goal and as much supporting detail as execution requires.

**Test:** An audience member can repeat the intended main idea and point to evidence supporting it. Check that simplification did not remove material limitations.

**Tension:** One message per advertisement and three supporting stories per talk are different units, not contradictory universal counting rules. Avoid imposing either count on every agent response.

### JPR-10 — Put technical facts in useful context and rehearse consequential demonstrations

**Evidence:** JP lines 203–218, 20:57–22:30 describe converting a large sales count into a daily rate; JP lines 271–281, 28:01–29:05 discuss practice. JC lines 191–196, 19:30–20:00 independently relay Kocienda’s rehearsal observations. JS lines 359–364, 36:38–37:08 distinguish informal internal conversation from carefully rehearsed public launches.

**Adaptation:** Explain what a measurement means for the audience, retaining denominator, scope, and uncertainty. Rehearse the real demo flow and prepare for likely failures before a consequential presentation.

**Test:** Recompute every derived metric; confirm the comparison is meaningful. Complete a timed rehearsal and exercise the fallback. Mark simulated data visibly.

**Tension:** Memorable framing must not inflate evidence. The claimed 90:1 practice ratio in JP is an unverified general statistic, not a prescribed Jobs rule. Rehearsal intensity should fit the stakes.

## Attribution traps to exclude from the skill

- JS lines 369–409, 37:37–41:41: the host explicitly says he coined the “Hearst principle.” Do not label it a Jobs method, even though he connects it to an iPod story.
- JS lines 249–254, 25:21–25:54: the remark about later Apple Pencil variants is the host’s counterfactual guess about Jobs. Exclude it as founder evidence.
- JS lines 170–173, 17:15–17:31: the “moral obligation” marketing formulation is the host’s interpretation, signaled as his own note.
- JC lines 282–326, 28:55–33:18: anti-data conclusions combine Kocienda’s viewpoint, Bowman’s experience, and host commentary. They do not establish a universal Jobs ban on experiments.
- JP lines 282–336, 29:10–34:35: “Messianic” purpose is Gallo/host framing, mixed with Phil Knight, Ogilvy, and attributed Jobs quotations. Use a concrete mission without manufacturing certainty or copying personality.
- Analogies involving Lombardi, Walton, Buffett, Munger, Disney, Dyson, and Southwest remain those people’s examples or the narrator’s comparisons. They are not independent evidence of what Jobs said.
- Promotions begin at JP line 351, JC line 396, and JS line 418. They illustrate the host’s current business and are not Jobs evidence.

## What this implies for the skill architecture

Keep an evidence registry beneath the operating instructions. A retrieval result should expose source identity, speaker, exact locator, evidence type, and limitations. A principle record should link to that evidence and keep the modern adaptation in a separate field. A feature recommendation should distinguish historical evidence, current project facts, inferred application, and a proposed verification step.

The ten principles above are candidates for the product and communication lens. They are not a replacement for the current user’s goals, empirical engineering evidence, or a fact-checked Musk corpus. Resolution rules between the two founder lenses are a new design decision and must be labeled as such.
