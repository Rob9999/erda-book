Continuous integration and publishing workflows for the project.

Reusable workflow components invoked by `orchestrator.yml` are stored
alongside this file in the `.github/workflows/` directory.

`publisher.yml` now executes the full publishing pipeline in a single container
invocation. The helper script `.github/tools/publishing/pipeline.py` refreshes
GitBook metadata and runs the PDF builder so other workflows no longer need to
duplicate those steps.

Cross-repository publishing requires a fine-scoped Personal Access Token with
`repo` scope stored as the `SPHERE_SPACE_STATION_EARTH_ONE_AND_BEYOND` secret
(named after the PAT). Workflows expose this token through the `GH_TOKEN`
environment variable for authentication.
