# output-dataset

With the launch of this new feature, we are enabling writing back to Blob, ADLS Gen 1, ADLS Gen 2, FileShare via either mount or upload. Simplified code experience is designed comparing with existing Pipelinedata to address feedback that there is no easy way to output data to a user defined folder, parse the pipeline intermediate data into Tabulardataset so that it can be used in the subsequent steps (e.g. automl step).

## Customer experience

- Users will be able to define dataset as the output of experiment (pythonscript, estimator, hyperdrive, pipelines)

- Users will be able to write back to Blob, ADLS Gen 1, ADLS Gen 2, FileShare via either upload or mount

- Users will be able to track the lineage between experiment and output dataset

## Known issues

- Parallel Run Step with multiple nodes is not supported at the moment. 
