# Research brief — IT Helpdesk Ticket Classifier

**Area:** AI Agents & Workflow Automation  
**Portfolio level:** Foundations

## Research problem

Classifies incoming helpdesk tickets into service categories and estimates an operational priority using transparent urgency/impact rules.

## Question

Can ticket text support transparent routing and urgency prioritization without over-automation?

## Implementation scope

- Support-ticket routing and priority

### Reproducible inputs and outputs

The current baseline uses `sample/tickets.csv`. The implementation consists of `src/predict.py`, `src/train.py`. Execution records, where available, are retained in [`results/`](../results/).

## Evaluation plan

1. Establish a versioned data protocol, input schema and independent baseline.
2. Evaluate functional correctness and record both successful and failed cases.
3. Compare relevant outcomes under controlled input variations and fixed environment settings.
4. Measure resource use and execution time across replicates when meaningful.
5. Document limitations, data provenance and risks of deployment in consequential environments.

### Validity and scope

The included local inputs are not evidence of population-level accuracy or external impact. Any synthetic inputs, simulations, heuristics and estimated performance figures must remain explicitly identified. Future benchmarks should use representative datasets, appropriate baselines, pre-specified metrics and independently reviewed methods.

## Evidence

Refer to [the recorded run](RESULTS.md), or to [the original project instructions](ORIGINAL_README.md) where local execution is not established. No publication, patent, user adoption or real-world deployment is claimed.
