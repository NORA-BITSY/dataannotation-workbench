# Assessment-day toolkit

**Default during the real assessment: use the platform and follow the exact instructions on screen.** This repository contains original preparation material. A tool that is offline or has no AI can still be outside the rules. If the live instructions are silent or unclear about a tool or resource, leave it closed until permission is clear. If the instructions prohibit LLMs, keep ChatGPT, Copilot, AI completions, answer checking and AI search assistants off throughout the attempt, including on a second device.

## Set up before starting

- Confirm the existing account's track label and whether this is a Starter or later qualification. Verify any displayed time limit and what happens on leaving the page. The public FAQ documents one Starter attempt. It does not establish a universal tool list or later retake policy. [Official FAQ](https://www.dataannotation.tech/faqs)
- Make time for the full displayed session, put the Mac on power, use a stable connection, silence notifications and close unrelated browser tabs and apps. Disable AI editor extensions and completions before the live screen opens. Confirm accessibility accommodations through the platform where needed.
- In an original practice session, test your input method, Python runtime or calculator if relevant, and the way you will check arithmetic and formatting without assistance. Use the actual test's built-in tools if provided and allowed.
- Finish one cold diagnostic, review it, then finish a fresh alternate. The study threshold is 80/100 and no critical errors. Technical forms additionally require at least 36/50 in each half. See [study index](../README.md) for the independent readiness path.

## Permissions card

| Resource | Before the assessment | During the assessment |
| --- | --- | --- |
| Original practice prompts, workbook, answer key, lab references and scoring tools | Study, complete a mock, and review after your attempt. | Keep closed unless the actual instructions explicitly allow that exact type of resource. |
| This repo's practice timer | Use it to learn pacing in the original mock. It only prints elapsed-time cues. | Default to the platform timer. Use an outside clock or timer only when allowed. |
| Blank paper or plain editor, calculator, spreadsheet, compiler or terminal | Rehearse with the minimum needed for your track. | Use only what the live instructions permit. Leave AI features disabled. |
| Official docs, search, or saved reference notes | Study beforehand. | Use only if that source type is expressly allowed. Public availability is not permission. |
| AI chat, completions, agents, generation or outside answer feedback | Use for learning or after grading an original mock. | Follow the prohibition where stated. Do not send live questions, code, screenshots or answers to any outside tool. |

This toolkit does not interact with DataAnnotation. The [practice timer](../../scripts/practice_timer.py) takes a track choice, has no external dependencies, and reads no assessment content. From the repository root, print checkpoints or run the countdown:

```sh
python3 scripts/practice_timer.py finance
python3 scripts/practice_timer.py technical --run
```

## Routines to memorize

- **Generalist:** Extract the exact requested outputs and constraints. Check each material claim against the evidence. Choose the supported verdict, explain the decisive difference, and verify the requested format.
- **Coding:** Clarify the input, return type and tie-break. Check a normal case and boundary, then test duplicates, empty inputs or retries where relevant. Explain time and space with the right variable.
- **DevOps:** Name the failure and the evidence. Decide hold, promote or recover. Identify the artifact, schema compatibility and a test through the actual traffic path.
- **Finance:** Mark units, period, cash versus accrual, and sign. Reconcile the endpoints by a separate calculation. State the business action and which assumption could change it.

On practice runs, spend roughly the first tenth reading constraints and reserve the final tenth to audit the response. For the live assessment, use its actual timing and rules. In the final review, check every requested subpart, material facts or numbers, and formatting. Do not copy live material into the repository, timer or score log.
