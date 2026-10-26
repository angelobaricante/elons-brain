# Behavioral evaluation

These cases are specifications, not recorded passes. Source review and package checks were performed during authoring; fresh-session model behavior still needs evaluation in the chosen host.

1. Start a fresh session per case. Load the candidate skill and make its bundled references accessible. Keep model, host version, skill revision, and available tools in the record.
2. Submit the case prompt without its expected results. If files or tools are unavailable, record that limitation; do not manufacture observations.
3. Save the answer and inspect each `must_demonstrate` criterion and `hard_failures` item. Relevant principle IDs are candidate evidence, not a mandatory list to recite.
4. Score attribution, project grounding, uncertainty, useful action, and scope from 0 to 2: absent/wrong, partial, or satisfied. Any hard failure fails the case regardless of total.
5. For an unexpected failure, revise the relevant instruction or evidence card and rerun that case plus cases affected by the revision. Compare with the original skill or a no-skill baseline before claiming improvement.

Record: case ID, date, model/host, skill revision, tools, full output, criterion judgments with supporting passages, hard failures, and limitations. Automated textual matches can flag issues but cannot establish the truth of a citation or quality of a recommendation.

Release bar: all applicable cases have recorded outputs, no unresolved hard failures, and human-reviewed source attributions. This bar is not yet met merely because `scripts/validate.py` succeeds. The Python script checks structure and evaluation coverage; it does not run model calls.
