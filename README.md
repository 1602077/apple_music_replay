# Apple Music Replay - Recreated using BigQuery

Here I used GCP's BigQuery to recalculate my Apple Music listening statistics, allowing me to aggregrate my stats the previous 5 years of streams in comparison to the current year view that apple presents. The bulk of the processing is performed in ```apple_music_replay.ipynb```, so please have a look through that.

I have also included some very basics scripts that use the pandas library to remove the redudant columns from the two files which have then subsequently beeen upload into a GCP bucket. This was completely optionally, BigQuery is more than equipped to process datasets of orders of magnitude larger than those used for this analysis - It was more for my own convience so that I could easily keep track of all the columns in my tables.

### Getting your Data

You can obtain your equivalent data to reconstruct this analysis by submitted a data request [here](https://privacy.apple.com) for your Apple Media Services information data. This does unfortunately take some time to process - just over a week in my case. 

The two files are used for this analysis are stored in the follow directory of the downloaded data: ```Apple\ Media Services\ information/Apple_Media_Services/Apple\ Music\ Activity```.

I used ```Apple Music Play Activity.csv``` to obtain all my streaming data to calculate artist and genre popularity and then joined in ```Apple Music Library Tracks.json``` to calculate album popularity.

For the csv file I had no issue importing into a GCP Bucket and then converting to a table in BigQuery, although I struggled to upload the JSON file. GCP's BigQuery only accepts new-line delimited JSON, which means one complete JSON object per line. The current ```Apple Music Library Tracks.json``` is not in this format and I converted it as follows:

```
brew install jt

cat Apple\ Music\ Library\ Tracks.json | jt -c '.[]' | pbcopy

vim MusicLibrary.json
```

Pasting the resultant file in vim took longer than expected for me due to the ~13k songs in my library, it may have been more efficient to write a short python script to perform the parsing. However, this did not matter anyway as GCP still would not accept this as a valid json. To resolve this I converted the json to a csv and reuploaded. If you know a better way around this please let me know.

### Setting up environment

I decided to use a juypter notebook for this analysis so that I would not have to keep re-running previous queries just to get the result of the latest one. This can be set up using  ```conda``` as follows:
```
conda create --name bigQ
conda install pandas numpy seaborn matplotlib notebook google-cloud-bigquery 
conda activate bigQ
jupyter notebook
```

You will now need to import your data into a GCP bucket so that it can then be queried. There is a set of command line tools for this, although as there was only two files I needed to upload into a single bucket and then two tables to create in bigQuery I just used the online [console](https://console.cloud.google.com/) to do this.

You will then need to generate an API key from your project's service account to authenticate any calls you make - documentation on how to do this is given [here](https://cloud.google.com/docs/authentication/production). Once you have your private key downloaded move it to the directory where you are performing this analysis and then adjust cell 2 of the jupyter notebook this exports the api key as an environment variable - preventing you to do it manually each time when you open a new shell. N.B. You can only download your private key once, if you lose it you will have to generate a new set of keys. Do not share / publish your key as someone may be able to use it to make queries through your GCP account.
