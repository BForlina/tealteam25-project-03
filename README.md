# EC2 Shutdown Lambda - GitHub CI/CD

## Overview
This repo implements a GitHub-based CI/CD pipeline that deploys an AWS Lambda (Python 3.12) which stops running EC2 instances on a schedule using EventBridge. The CloudFormation template to deploy is located at `infrastructure/cloudformation/lambda-ec2-shutdown.yml`.

## Files
- `src/lambda_function.py` — Lambda handler (uses boto3).
- `infrastructure/cloudformation/lambda-ec2-shutdown.yml` — CloudFormation template (provided).
- `.github/workflows/on_pull_request.yml` — zip/upload/deploy to beta on PR.
- `.github/workflows/on_merge.yml` — zip/upload/deploy to prod on merge to `main`.

## Setup
1. Add repository secrets (see list in README above).
2. Ensure the S3 buckets exist and the deployer IAM has `PutObject` into those buckets.
3. Create PR to trigger `on_pull_request.yml` (beta deploy). Merge to `main` to trigger production deploy.

## Modifying the Lambda logic
- Edit `src/lambda_function.py`.
- If you want to filter instances, set environment vars `INSTANCE_TAG_KEY` and `INSTANCE_TAG_VALUE` on the Lambda (via CloudFormation or in the console).
  - Example: tag all auto-stoppable instances with `AutoStop=true`.

## Trigger workflows
- **Beta (PR):** Open or update a pull request; `on_pull_request.yml` runs.
- **Prod (merge):** Merge into `main`; `on_merge.yml` runs.

## Verify
- CloudFormation console (stack resources).
- Lambda console (invocations & environment variables).
- CloudWatch Logs (Lambda execution logs).
- EC2 console (check instance state transitions).

## References
- AWS SDK for Python (Boto3) — official docs. :contentReference[oaicite:9]{index=9}
- Boto3 `stop_instances` API reference. :contentReference[oaicite:10]{index=10}
- CloudFormation template used (gist). :contentReference[oaicite:11]{index=11}

