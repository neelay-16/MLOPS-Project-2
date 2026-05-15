Comet\_ml:

Points to remember:

* Get API Key,project\_name and workspace name from comet ml website and create a new project
* import comet\_ml at the top of python file only otherwise it might show some warnings
* initialize comet\_ml in constructor
* write code for whatever you want to be tracked in your experiments
* in comet\_ml's experimenet tracking you come to know about different graphs based on your model training, hyperparameters used, metrics of your model, code, confusion matric and histograms(if used via code) and many other things. 





DVC: (install dvc and dvc-gs python libraries)

* Should be connected to your cloud bucket.
* commands to be remembered: dvc init, dvc add artifacts/raw, dvc add artifacts/processed, dvc add artifacts/weights, dvc add artifacts/model, dvc add artifacts/model\_checkpoint (Make sure you add the .dvc files being created from these commands into your git hub repo. Not the actual folders, jsut the .dvc files)
* commands to be remembered: dvc status, dvc remote add -d myremote gs://my-dvc-bucket100/, dvc push
* in case you accidently deleted any data from artifacts, you can now restore it using the command dvc pull
* Note that, for storing the data into your cloud clucket through dvc, hashing algorithms are used from DSA. You might need to study those as well.
* In such projects where DVC is used, there is no need to use data ingestion from GCP as we have DVC now we can just make dvc pull in cmd.

