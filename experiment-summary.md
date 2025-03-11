## Completed Sensitivity Tests

| Test / Feature                              | Parameter Changed        | Purged Output? | Output Directory | Truncation Errors | Model Version | Evaluation / Benchmarks | Status     | GitHub Issue                                                   |
|---------------------------------------------|--------------------------|----------------|------------------|-------------------|---------------|-------------------------|-----------|----------------------------------------------------------------|
| Timesteps                                   | Dynamic/Tracer/Coupling  | N/A            | N/A              | None              | 0.3.1         | N/A                     | Completed | [#138](https://github.com/COSIMA/access-om3/issues/138)        |
| Land Mask Changes                           | Land-sea mask updates    | N/A            | N/A              | None              | N/A           | N/A                     | Completed | [#177](https://github.com/COSIMA/access-om3/issues/177)        |
| Equation of State (WRIGHT_REDUCED)          | Equation of state        | N/A            | N/A              | None              | N/A           | N/A                     | Completed | [#180](https://github.com/COSIMA/access-om3/issues/180)        |

---

## Pending / In-Progress Sensitivity Tests

| Test / Feature                 | Parameter Changed          | Purged Output? | Output Directory  | Truncation Errors                     | Model Version | Evaluation / Benchmarks        | Status   | GitHub Issue                                                                                 |
|--------------------------------|----------------------------|----------------|-------------------|---------------------------------------|---------------|--------------------------------|----------|--------------------------------------------------------------------------------------------------|
| Single Step Call               | on/off check difference    | Yes            | N/A               | N/A                                    | N/A           | N/A                            | Pending  | [#140](https://github.com/COSIMA/access-om3/issues/140)                                          |
| Mesoscale Parameterisation     | w and wo meke              | Yes            | N/A               | N/A                                    | 0.3.1         | N/A                            | Pending  | [#179](https://github.com/COSIMA/access-om3/issues/179)                                          |
| Submesoscale Parameterisation  | Boldner et al (2023)       | No             | N/A               | N/A                                    | N/A           | N/A                            | Pending  | [#254](https://github.com/COSIMA/access-om3/issues/254)                                          |
| Vertical Mixing                | epbl and kpp               | No             | N/A               | Yes ([#189](https://github.com/COSIMA/access-om3/issues/189)<br>[#288](https://github.com/COSIMA/access-om3/issues/288))                       | Only MOM in 0.4.0 with bug fix           | N/A                            | Pending  | [#189](https://github.com/COSIMA/access-om3/issues/189)<br>[#288](https://github.com/COSIMA/access-om3/issues/288) |
| Lateral Friction               | Smargorinsky and Leith     | No             | N/A               | Extreme values detected (details TBD)  | N/A           | N/A                            | Pending  | [#253](https://github.com/COSIMA/access-om3/issues/253)                                          |
| Tidal Dissipation              | Tidal dissipation params   | N/A            | N/A               | Missing external files                 | N/A           | N/A                            | Pending  | [#280](https://github.com/COSIMA/access-om3/issues/280)                                          |
| Neutral Diffusion              | Already in config          | N/A            | N/A               | N/A                                    | N/A           | N/A                            | N/A      | –                                                                                                |

---

## Challenges & Suggested Approaches

| Challenge                                                                             | Suggested Approach                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Different model versions expose different parameters.                                 | Use v0.4.0 (or updated components) wherever possible. Keep track of which version is used for the control comparison.                                                                                            |
| Subject-specific knowledge needed to interpret parameter choices.                     | Leverage community expertise (e.g., ACCESS-NRI team). Individual researchers do not need to be the sole experts on every detail.                                                                                 |
| Evaluating parameter choices often requires bespoke outputs.                          | Try to avoid specialised output whenever possible, but if needed, write up minimal evaluation benchmarks. Use existing OM3/OM2 evaluation metrics (from published papers) as a template.                          |
| Limited internal knowledge on parameter choices; want alignment with upstream code.   | Use OM2 and upstream parameter values as a starting point. Revisit or revise only when there's a clear reason.                                                                                                    |
| Moving code base and difficulty aligning on a single version.                         | Consider freezing a stable model version (e.g., “release candidate”) for consistent comparisons, while continuing to develop in parallel.                                                                        |
