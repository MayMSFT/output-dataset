# [Public Preview] output-dataset 

With the launch of this new feature, we are enabling writing back to Blob, ADLS Gen 1, ADLS Gen 2, FileShare via either mount or upload. Simplified code experience is designed comparing with existing Pipelinedata to address feedback that there is no easy way to output data to a user defined folder, parse the pipeline intermediate data into Tabulardataset so that it can be used in the subsequent steps (e.g. automl step).

## Customer experience

- Users will be able to define dataset as the output of experiment (pythonscript, estimator, hyperdrive, pipelines)

- Users will be able to write back to Blob, ADLS Gen 1, ADLS Gen 2, FileShare via either upload or mount

- Users will be able to track the lineage between experiment and output dataset

## Terms of Use
This is a private preview feature of Azure Machine Learning and is subject to the [Azure Legal Terms](https://azure.microsoft.com/en-us/support/legal/?ranMID=24542&ranEAID=msYS1Nvjv4c&ranSiteID=msYS1Nvjv4c-pQVqGgzMLX3ysSdCWd8org&epi=msYS1Nvjv4c-pQVqGgzMLX3ysSdCWd8org&irgwc=1&OCID=AID2000142_aff_7593_1243925&tduid=%28ir__6kriqwk10wkftwnk0higqpq2m22xi0gd9xxevzpz00%29%287593%29%281243925%29%28msYS1Nvjv4c-pQVqGgzMLX3ysSdCWd8org%29%28%29&irclickid=_6kriqwk10wkftwnk0higqpq2m22xi0gd9xxevzpz00) and the [Supplemental Terms for Azure Previews](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/)<br>
