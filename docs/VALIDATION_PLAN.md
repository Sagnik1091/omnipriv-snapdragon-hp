# Validation plan

All measurements must identify the exact HP device, Snapdragon SKU, Windows build, runtime version, model artifact, precision, power mode, and test input.

## 1. Functional validation

- Run at least three different audio samples.
- Confirm transcript output changes with the input.
- Record word-error observations on a manually checked sample.
- Verify that action items and answers cite transcript segments.

## 2. Runtime validation

- Capture available ONNX Runtime execution providers.
- Record provider assignment and any CPU fallback.
- Save QNN/runtime logs with the benchmark report.
- Treat mixed-provider execution as mixed execution, not “100% NPU.”

## 3. Offline validation

- Pre-provision every required artifact.
- Disconnect the network and repeat the full workflow.
- Monitor outbound connection attempts during the run.
- Document any optional online setup or download step separately.

## 4. Performance validation

Measure warm-up separately from steady state:

- transcript update latency;
- model initialization time;
- tokens per second where applicable;
- working-set memory;
- CPU and NPU utilization;
- package power using a documented tool and sampling interval.

Compare identical inputs and output settings against a documented CPU reference path.

## 5. Reporting rule

A target becomes a result only when the repository contains the raw log, test configuration, date, device information, and reproducible command.
